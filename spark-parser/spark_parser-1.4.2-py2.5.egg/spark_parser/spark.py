"""
Copyright (c) 2015-2016 Rocky Bernstein
Copyright (c) 1998-2002 John Aycock

  Permission is hereby granted, free of charge, to any person obtaining
  a copy of this software and associated documentation files (the
  "Software"), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so, subject to
  the following conditions:

  The above copyright notice and this permission notice shall be
  included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
# from __future__ import print_function

import os, re
def _namelist(instance):
    namelist, namedict, classlist = [], {}, [instance.__class__]
    for c in classlist:
        for b in c.__bases__:
            classlist.append(b)
        for name in list(c.__dict__.keys()):
            if name not in namedict:
                namelist.append(name)
                namedict[name] = 1
    return namelist

class _State:
    '''
    Extracted from GenericParser and made global so that [un]picking works.
    '''
    def __init__(self, stateno, items):
        self.T, self.complete, self.items = [], [], items
        self.stateno = stateno

# DEFAULT_DEBUG = {'rules': True, 'transition': True, 'reduce' : True,
#                  'errorstack': 'full' }
# DEFAULT_DEBUG = {'rules': False, 'transition': False, 'reduce' : True,
#                  'errorstack': 'plain' }
DEFAULT_DEBUG = {'rules': False, 'transition': False, 'reduce': False,
                 'errorstack': None, 'context': True}

class GenericParser(object):
    '''
    An Earley parser, as per J. Earley, "An Efficient Context-Free
    Parsing Algorithm", CACM 13(2), pp. 94-102.  Also J. C. Earley,
    "An Efficient Context-Free Parsing Algorithm", Ph.D. thesis,
    Carnegie-Mellon University, August 1968.  New formulation of
    the parser according to J. Aycock, "Practical Earley Parsing
    and the SPARK Toolkit", Ph.D. thesis, University of Victoria,
    2001, and J. Aycock and R. N. Horspool, "Practical Earley
    Parsing", unpublished paper, 2001.
    '''

    def __init__(self, start, debug=DEFAULT_DEBUG):
        self.rules = {}
        self.rule2func = {}
        self.rule2name = {}

        # When set, shows additional debug output
        self.debug = debug

        self.collectRules()
        self.augment(start)
        self.ruleschanged = True


        # The entries here should be tuples of LHS string name
        # and a function to call that can perform additonal checks
        # on the reduction. That function is passed (self, lhs, sets)
        self.check_reduce = []

    _NULLABLE = '\e_'
    _START = 'START'
    _BOF = '|-'

    #
    #  When pickling, take the time to generate the full state machine;
    #  some information is then extraneous, too.  Unfortunately we
    #  can't save the rule2func map.
    #
    def __getstate__(self):
        if self.ruleschanged:
            #
            #  XXX - duplicated from parse()
            #
            self.computeNull()
            self.newrules = {}
            self.new2old = {}
            self.makeNewRules()
            self.ruleschanged = False
            self.edges, self.cores = {}, {}
            self.states = {0: self.makeState0()}
            self.makeState(0, self._BOF)
        #
        #  XXX - should find a better way to do this..
        #
        changes = 1
        while changes:
            changes = 0
            for k, v in list(self.edges.items()):
                if v is None:
                    state, sym = k
                    if state in self.states:
                        self.goto(state, sym)
                        changes = 1
        rv = self.__dict__.copy()
        for s in list(self.states.values()):
            del s.items
        del rv['rule2func']
        del rv['nullable']
        del rv['cores']
        return rv

    def __setstate__(self, D):
        self.rules = {}
        self.rule2func = {}
        self.rule2name = {}
        self.collectRules()
        start = D['rules'][self._START][0][1][1]  # Blech.
        self.augment(start)
        D['rule2func'] = self.rule2func
        D['makeSet'] = self.makeSet_fast
        self.__dict__ = D

    #
    #  A hook for GenericASTBuilder and GenericASTMatcher.  Mess
    #  thee not with this; nor shall thee toucheth the _preprocess
    #  argument to addRule.
    #
    def preprocess(self, rule, func):
        return rule, func

    def addRule(self, doc, func, _preprocess=True):
        """Add a grammar rules to self.rules, self.rule2func and self.rule2name"""
        fn = func

        # remove blanks lines and comment lines, e.g. lines starting with "#"
        doc = os.linesep.join([s for s in doc.splitlines() if s and not re.match("^\s*#", s)])

        rules = doc.split()

        index = []
        for i in range(len(rules)):
            if rules[i] == '::=':
                index.append(i-1)
        index.append(len(rules))

        for i in range(len(index)-1):
            lhs = rules[index[i]]
            rhs = rules[index[i]+2:index[i+1]]
            rule = (lhs, tuple(rhs))

            if _preprocess:
                rule, fn = self.preprocess(rule, func)

            if lhs in self.rules:
                if rule in self.rules[lhs]:
                    if self.debug['rules']:
                        print("Duplicate rule\n\t:%s ::= %s" %
                              (rule[0], ' '.join(rule[1])))
                    continue
                self.rules[lhs].append(rule)
            else:
                self.rules[lhs] = [ rule ]
            self.rule2func[rule] = fn
            self.rule2name[rule] = func.__name__[2:]
        self.ruleschanged = True

    def collectRules(self):
        for name in _namelist(self):
            if name[:2] == 'p_':
                func = getattr(self, name)
                doc = func.__doc__
                self.addRule(doc, func)

    def augment(self, start):
        rule = '%s ::= %s %s' % (self._START, self._BOF, start)
        self.addRule(rule, lambda args: args[1], 0)

    def computeNull(self):
        self.nullable = {}
        tbd = []

        for rulelist in list(self.rules.values()):
            lhs = rulelist[0][0]
            self.nullable[lhs] = 0
            for rule in rulelist:
                rhs = rule[1]
                if len(rhs) == 0:
                    self.nullable[lhs] = 1
                    continue
                #
                #  We only need to consider rules which
                #  consist entirely of nonterminal symbols.
                #  This should be a savings on typical
                #  grammars.
                #
                for sym in rhs:
                    if sym not in self.rules:
                        break
                else:
                    tbd.append(rule)
        changes = 1
        while changes:
            changes = 0
            for lhs, rhs in tbd:
                if self.nullable[lhs]:
                    continue
                for sym in rhs:
                    if not self.nullable[sym]:
                        break
                else:
                    self.nullable[lhs] = 1
                    changes = 1

    def makeState0(self):
        s0 = _State(0, [])
        for rule in self.newrules[self._START]:
            s0.items.append((rule, 0))
        return s0

    def finalState(self, tokens):
        #
        #  Yuck.
        #
        if len(self.newrules[self._START]) == 2 and len(tokens) == 0:
            return 1
        start = self.rules[self._START][0][1][1]
        return self.goto(1, start)

    def makeNewRules(self):
        worklist = []
        for rulelist in list(self.rules.values()):
            for rule in rulelist:
                worklist.append((rule, 0, 1, rule))

        for rule, i, candidate, oldrule in worklist:
            lhs, rhs = rule
            n = len(rhs)
            while i < n:
                sym = rhs[i]
                if (sym not in self.rules or
                    not self.nullable[sym]):
                        candidate = 0
                        i = i + 1
                        continue

                newrhs = list(rhs)
                newrhs[i] = self._NULLABLE+sym
                newrule = (lhs, tuple(newrhs))
                worklist.append((newrule, i+1,
                                 candidate, oldrule))
                candidate = 0
                i = i + 1
            else:
                if candidate:
                    lhs = self._NULLABLE+lhs
                    rule = (lhs, rhs)
                if lhs in self.newrules:
                    self.newrules[lhs].append(rule)
                else:
                    self.newrules[lhs] = [rule]
                self.new2old[rule] = oldrule

    def typestring(self, token):
        return None

    def error(self, tokens, index):
        print("Syntax error at or near token %d: `%s'" % (index, tokens[index]))

        if 'context' in self.debug and self.debug['context']:
            if index - 2 >= 0:
                start = index - 2
            else:
                start = 0
            tokens = [str(tokens[i]) for i in range(start, index+1)]
            print("Token context:\n\t%s" % ("\n\t".join(tokens)))
        raise SystemExit

    def errorstack(self, full=False):
        """Show the stacks of completed symbols.
        We get this by inspecting the current transitions
        possible and from that extracting the set of states
        we are in, and from there we look at the set of
        symbols before the "dot". If full is True, we
        show the entire rule with the dot placement.
        Otherwise just the rule up to the dot.
        """
        print()
        print("-- Stacks of completed symbols:")
        states = [s for s in self.edges.values() if s]
        # States now has the set of states we are in
        state_stack = set()
        for state in states:
            # Find rules which can follow, but keep only
            # the part before the dot
            for rule, dot in self.states[state].items:
                lhs, rhs = rule
                if dot > 0:
                    if full:
                        state_stack.add(' '.join(rhs[:dot]) + ' . ' + ' '.join(rhs[dot:]))
                    else:
                        state_stack.add(' '.join(rhs[:dot]))
                    pass
                pass
            pass
        for stack in sorted(state_stack):
            print(stack)

    def parse(self, tokens, debug=None):
        """This is the main entry point from outside.

        Passing in a debug dictionary changes the default debug
        setting.
        """

        if debug:
            self.debug = debug

        sets = [ [(1, 0), (2, 0)] ]
        self.links = {}

        if self.ruleschanged:
            self.computeNull()
            self.newrules = {}
            self.new2old = {}
            self.makeNewRules()
            self.ruleschanged = False
            self.edges, self.cores = {}, {}
            self.states = { 0: self.makeState0() }
            self.makeState(0, self._BOF)

        for i in range(len(tokens)):
            sets.append([])

            if sets[i] == []:
                break
            self.makeSet(tokens, sets, i)
        else:
            sets.append([])
            self.makeSet(None, sets, len(tokens))

        finalitem = (self.finalState(tokens), 0)
        if finalitem not in sets[-2]:
            if len(tokens) > 0:
                if self.debug['errorstack']:
                    self.errorstack(str(self.debug['errorstack']) == 'full')
                self.error(tokens, i-1)
            else:
                self.error(None, None)

        return self.buildTree(self._START, finalitem,
                    tokens, len(sets)-2)

    def isnullable(self, sym):
        #  For symbols in G_e only.
        return sym.startswith(self._NULLABLE)

    def skip(self, xxx_todo_changeme, pos=0):
        (lhs, rhs) = xxx_todo_changeme
        n = len(rhs)
        while pos < n:
            if not self.isnullable(rhs[pos]):
                break
            pos = pos + 1
        return pos

    def makeState(self, state, sym):
        assert sym is not None
        # print(sym) # debug
        #
        #  Compute \epsilon-kernel state's core and see if
        #  it exists already.
        #
        kitems = []
        for rule, pos in self.states[state].items:
            lhs, rhs = rule
            if rhs[pos:pos+1] == (sym,):
                kitems.append((rule, self.skip(rule, pos+1)))

        tcore = tuple(sorted(kitems))
        if tcore in self.cores:
            return self.cores[tcore]
        #
        #  Nope, doesn't exist.  Compute it and the associated
        #  \epsilon-nonkernel state together; we'll need it right away.
        #
        k = self.cores[tcore] = len(self.states)
        K, NK = _State(k, kitems), _State(k+1, [])
        self.states[k] = K
        predicted = {}

        edges = self.edges
        rules = self.newrules
        for X in K, NK:
            worklist = X.items
            for item in worklist:
                rule, pos = item
                lhs, rhs = rule
                if pos == len(rhs):
                    X.complete.append(rule)
                    continue

                nextSym = rhs[pos]
                key = (X.stateno, nextSym)
                if nextSym not in rules:
                    if key not in edges:
                        edges[key] = None
                        X.T.append(nextSym)
                else:
                    edges[key] = None
                    if nextSym not in predicted:
                        predicted[nextSym] = 1
                        for prule in rules[nextSym]:
                            ppos = self.skip(prule)
                            new = (prule, ppos)
                            NK.items.append(new)
            #
            #  Problem: we know K needs generating, but we
            #  don't yet know about NK.  Can't commit anything
            #  regarding NK to self.edges until we're sure.  Should
            #  we delay committing on both K and NK to avoid this
            #  hacky code?  This creates other problems..
            #
            if X is K:
                edges = {}

        if NK.items == []:
            return k

        #
        #  Check for \epsilon-nonkernel's core.  Unfortunately we
        #  need to know the entire set of predicted nonterminals
        #  to do this without accidentally duplicating states.
        #
        tcore = tuple(sorted(predicted.keys()))
        if tcore in self.cores:
            self.edges[(k, None)] = self.cores[tcore]
            return k

        nk = self.cores[tcore] = self.edges[(k, None)] = NK.stateno
        self.edges.update(edges)
        self.states[nk] = NK
        return k

    def goto(self, state, sym):
        key = (state, sym)
        if key not in self.edges:
            #
            #  No transitions from state on sym.
            #
            return None

        rv = self.edges[key]
        if rv is None:
            #
            #  Target state isn't generated yet.  Remedy this.
            #
            rv = self.makeState(state, sym)
            self.edges[key] = rv
        return rv

    def gotoT(self, state, t):
        if self.debug['rules']:
            print("Terminal", t, state)
        return [self.goto(state, t)]

    def gotoST(self, state, st):
        if self.debug['transition']:
            print("GotoST", st, state)
        rv = []
        for t in self.states[state].T:
            if st == t:
                rv.append(self.goto(state, t))
        return rv

    def add(self, set, item, i=None, predecessor=None, causal=None):
        if predecessor is None:
            if item not in set:
                set.append(item)
        else:
            key = (item, i)
            if item not in set:
                self.links[key] = []
                set.append(item)
            self.links[key].append((predecessor, causal))

    def makeSet(self, tokens, sets, i):
        cur, next = sets[i], sets[i+1]

        if tokens is not None:
            token = tokens[i]
            ttype = self.typestring(token)
        else:
            ttype = None
            token = None
        if ttype is not None:
            fn, arg = self.gotoT, ttype
        else:
            fn, arg = self.gotoST, token

        for item in cur:
            ptr = (item, i)
            state, parent = item
            add = fn(state, arg)
            for k in add:
                if k is not None:
                    self.add(next, (k, parent), i+1, ptr)
                    nk = self.goto(k, None)
                    if nk is not None:
                        self.add(next, (nk, i+1))

            if parent == i:
                continue

            for rule in self.states[state].complete:
                lhs, rhs = rule
                if lhs in self.check_reduce:
                    if not self.reduce_check[lhs](self, lhs, sets):
                        continue
                    pass
                if self.debug['reduce']:
                    print("%s ::= %s" % (lhs, ' '.join(rhs)))
                for pitem in sets[parent]:
                    pstate, pparent = pitem
                    k = self.goto(pstate, lhs)
                    if k is not None:
                        why = (item, i, rule)
                        pptr = (pitem, parent)
                        self.add(cur, (k, pparent),
                                i, pptr, why)
                        nk = self.goto(k, None)
                        if nk is not None:
                            self.add(cur, (nk, i))

    def makeSet_fast(self, token, sets, i):
        #
        #  Call *only* when the entire state machine has been built!
        #  It relies on self.edges being filled in completely, and
        #  then duplicates and inlines code to boost speed at the
        #  cost of extreme ugliness.
        #
        cur, next = sets[i], sets[i+1]
        ttype = token is not None and self.typestring(token) or None

        for item in cur:
            ptr = (item, i)
            state, parent = item
            if ttype is not None:
                k = self.edges.get((state, ttype), None)
                if k is not None:
                    # self.add(next, (k, parent), i+1, ptr)
                    # INLINED --------v
                    new = (k, parent)
                    key = (new, i+1)
                    if new not in next:
                        self.links[key] = []
                        next.append(new)
                    self.links[key].append((ptr, None))
                    # INLINED --------^
                    # nk = self.goto(k, None)
                    nk = self.edges.get((k, None), None)
                    if nk is not None:
                        # self.add(next, (nk, i+1))
                        # INLINED -------------v
                        new = (nk, i+1)
                        if new not in next:
                            next.append(new)
                        # INLINED ---------------^
            else:
                add = self.gotoST(state, token)
                for k in add:
                    if k is not None:
                        self.add(next, (k, parent), i+1, ptr)
                        # nk = self.goto(k, None)
                        nk = self.edges.get((k, None), None)
                        if nk is not None:
                            self.add(next, (nk, i+1))

            if parent == i:
                continue

            for rule in self.states[state].complete:
                lhs, rhs = rule
                for pitem in sets[parent]:
                    pstate, pparent = pitem
                    # k = self.goto(pstate, lhs)
                    k = self.edges.get((pstate, lhs), None)
                    if k is not None:
                        why = (item, i, rule)
                        pptr = (pitem, parent)
                        # self.add(cur, (k, pparent), i, pptr, why)
                        # INLINED ---------v
                        new = (k, pparent)
                        key = (new, i)
                        if new not in cur:
                            self.links[key] = []
                            cur.append(new)
                        self.links[key].append((pptr, why))
                        # INLINED ----------^
                        # nk = self.goto(k, None)
                        nk = self.edges.get((k, None), None)
                        if nk is not None:
                            # self.add(cur, (nk, i))
                            # INLINED ---------v
                            new = (nk, i)
                            if new not in cur:
                                cur.append(new)
                            # INLINED ----------^

    def predecessor(self, key, causal):
        for p, c in self.links[key]:
            if c == causal:
                return p
        assert 0

    def causal(self, key):
        links = self.links[key]
        if len(links) == 1:
            return links[0][1]
        choices = []
        rule2cause = {}
        for p, c in links:
            rule = c[2]
            choices.append(rule)
            rule2cause[rule] = c
        return rule2cause[self.ambiguity(choices)]

    def deriveEpsilon(self, nt):
        if len(self.newrules[nt]) > 1:
            rule = self.ambiguity(self.newrules[nt])
        else:
            rule = self.newrules[nt][0]
        # print(rule) # debug

        rhs = rule[1]
        attr = [None] * len(rhs)

        for i in range(len(rhs)-1, -1, -1):
            attr[i] = self.deriveEpsilon(rhs[i])
        return self.rule2func[self.new2old[rule]](attr)

    def buildTree(self, nt, item, tokens, k):
        if self.debug['rules']:
            print("NT", nt)
        state, parent = item

        choices = []
        for rule in self.states[state].complete:
            if rule[0] == nt:
                choices.append(rule)
        rule = choices[0]
        if len(choices) > 1:
            rule = self.ambiguity(choices)
        # print(rule) # debug

        rhs = rule[1]
        attr = [None] * len(rhs)

        for i in range(len(rhs)-1, -1, -1):
            sym = rhs[i]
            if sym not in self.newrules:
                if sym != self._BOF:
                    attr[i] = tokens[k-1]
                    key = (item, k)
                    item, k = self.predecessor(key, None)
            # elif self.isnullable(sym):
            elif self._NULLABLE == sym[0:len(self._NULLABLE)]:
                attr[i] = self.deriveEpsilon(sym)
            else:
                key = (item, k)
                why = self.causal(key)
                attr[i] = self.buildTree(sym, why[0],
                            tokens, why[1])
                item, k = self.predecessor(key, why)
        return self.rule2func[self.new2old[rule]](attr)

    def ambiguity(self, rules):
        #
        #  XXX - problem here and in collectRules() if the same rule
        #  appears in >1 method.  Also undefined results if rules
        #  causing the ambiguity appear in the same method.
        #
        sortlist = []
        name2index = {}
        for i in range(len(rules)):
            lhs, rhs = rule = rules[i]
            name = self.rule2name[self.new2old[rule]]
            sortlist.append((len(rhs), name))
            name2index[name] = i
        sortlist.sort()
        list = [a_b[1] for a_b in sortlist]
        return rules[name2index[self.resolve(list)]]

    def resolve(self, list):
        '''
        Resolve ambiguity in favor of the shortest RHS.
        Since we walk the tree from the top down, this
        should effectively resolve in favor of a "shift".
        '''
        return list[0]

    def dumpGrammar(self):
        '''
        Print grammar rules
        '''
        import collections
        for lhs, rhs in collections.OrderedDict(sorted(self.rule2name.items())):
            print("%s ::= %s" % (lhs, ' '.join(rhs)))
            pass
        return

    def checkGrammar(self):
        '''
        Check grammar
        '''
        lhs, rhs, tokens, right_recursive = self.checkSets()
        if len(lhs) > 0:
            print("LHS symbols not used on the RHS:")
            print(sorted(lhs))
        if len(rhs) > 0:
            print("RHS symbols not used on the LHS:")
            print(sorted(rhs))
        if len(right_recursive) > 0:
            print("Right recursive rules:")
            for rule in right_recursive:
                print("%s ::= %s" % (rule[0], ' '.join(rule[1])))
                pass
            pass

    def checkSets(self):
        '''
        Check grammar
        '''
        lhs_set = set()
        rhs_set = set()
        token_set = set()
        right_recursive = []
        for lhs in self.rules:
            rules_for_lhs = self.rules[lhs]
            lhs_set.add(lhs)
            for rule in rules_for_lhs:
                rhs = rule[1]
                for sym in rhs:
                    # We assume any symbol starting with an uppercase letter is
                    # terminal, and anything else is a nonterminal
                    if re.match("^[A-Z]", sym):
                        token_set.add(sym)
                    else:
                        rhs_set.add(sym)
                if len(rhs) > 0 and lhs == rhs[-1]:
                    right_recursive.append([lhs, rhs])
                pass
            pass

        lhs_set.remove(self._START)
        rhs_set.remove(self._BOF)
        missing_lhs = lhs_set - rhs_set
        missing_rhs = rhs_set - lhs_set
        return (missing_lhs, missing_rhs, token_set, right_recursive)

#
#
#  GenericASTBuilder automagically constructs a concrete/abstract syntax tree
#  for a given input.  The extra argument is a class (not an instance!)
#  which supports the "__setslice__" and "__len__" methods.
#
#  XXX - silently overrides any user code in methods.
#

class GenericASTBuilder(GenericParser):
    def __init__(self, AST, start, debug=DEFAULT_DEBUG):
        GenericParser.__init__(self, start, debug=debug)
        self.AST = AST

    def preprocess(self, rule, func):
        rebind = lambda lhs, self=self: \
                lambda args, lhs=lhs, self=self: \
                self.buildASTNode(args, lhs)
        lhs, rhs = rule
        return rule, rebind(lhs)

    def buildASTNode(self, args, lhs):
        children = []
        for arg in args:
            if isinstance(arg, self.AST):
                children.append(arg)
            else:
                children.append(self.terminal(arg))
        return self.nonterminal(lhs, children)

    def terminal(self, token):
        return token

    def nonterminal(self, type, args):
        rv = self.AST(type)
        rv[:len(args)] = args
        return rv
