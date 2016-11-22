# -*- generated by 1.0.4 -*-
import da
PatternExpr_377 = da.pat.TuplePattern([da.pat.ConstantPattern('AppendEntries'), da.pat.FreePattern('term'), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)])
PatternExpr_444 = da.pat.TuplePattern([da.pat.ConstantPattern('RequestVoteReply'), da.pat.BoundPattern('_BoundPattern447_'), da.pat.ConstantPattern(True)])
PatternExpr_452 = da.pat.FreePattern('p')
PatternExpr_507 = da.pat.TuplePattern([da.pat.ConstantPattern('AppendEntries'), da.pat.FreePattern('term'), da.pat.FreePattern('leader'), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)])
PatternExpr_644 = da.pat.TuplePattern([da.pat.ConstantPattern('RequestVote'), da.pat.FreePattern('term'), da.pat.FreePattern('candidateId'), da.pat.FreePattern('lastLogIndex'), da.pat.FreePattern('lastLogTerm')])
PatternExpr_701 = da.pat.TuplePattern([da.pat.ConstantPattern('RequestVoteReply'), da.pat.FreePattern('term'), da.pat.ConstantPattern(False)])
PatternExpr_716 = da.pat.TuplePattern([da.pat.ConstantPattern('AppendEntries'), da.pat.FreePattern('term'), da.pat.FreePattern('leaderId'), da.pat.FreePattern('prevLogIndex'), da.pat.FreePattern('prevLogTerm'), da.pat.FreePattern('entries'), da.pat.FreePattern('leaderCommit')])
PatternExpr_833 = da.pat.TuplePattern([da.pat.ConstantPattern('AppendEntriesReply'), da.pat.FreePattern('term'), da.pat.FreePattern('success'), da.pat.FreePattern('updatedIndex')])
PatternExpr_844 = da.pat.FreePattern('server')
PatternExpr_876 = da.pat.TuplePattern([da.pat.ConstantPattern('ClientRequest'), da.pat.FreePattern('serial')])
PatternExpr_883 = da.pat.FreePattern('client')
PatternExpr_1068 = da.pat.TuplePattern([da.pat.ConstantPattern('NotLeader'), da.pat.BoundPattern('_BoundPattern1071_'), da.pat.FreePattern('leader')])
PatternExpr_1105 = da.pat.TuplePattern([da.pat.ConstantPattern('Reply'), da.pat.BoundPattern('_BoundPattern1108_'), da.pat.FreePattern(None)])
PatternExpr_1281 = da.pat.TuplePattern([da.pat.ConstantPattern('Done')])
PatternExpr_1286 = da.pat.BoundPattern('_BoundPattern1287_')
PatternExpr_1288 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern1294_')]), da.pat.TuplePattern([da.pat.ConstantPattern('Done')])])
_config_object = {}
import sys
import random

class Role():
    pass

class Follower(Role):
    pass

class Candidate(Role):
    pass

class Leader(Role):
    pass

class LogEntry():
    'Fictional log entries.'

    def __init__(self, term, client, command):
        self.term = term
        self.client = client
        self.command = command

    def __str__(self):
        sl = ['LogEntry', str(self.term), str(self.client), str(self.command)]
        return ':'.join(sl)

class Server(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ServerReceivedEvent_0 = []
        self._ServerReceivedEvent_1 = []
        self._ServerReceivedEvent_2 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_0', PatternExpr_377, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_1', PatternExpr_444, sources=[PatternExpr_452], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_2', PatternExpr_507, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_3', PatternExpr_644, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_643]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_4', PatternExpr_701, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_700]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_5', PatternExpr_716, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_715]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_6', PatternExpr_833, sources=[PatternExpr_844], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_832]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ServerReceivedEvent_7', PatternExpr_876, sources=[PatternExpr_883], destinations=None, timestamps=None, record_history=None, handlers=[self._Server_handler_875])])

    def setup(self, peers, maxTimeout, **rest_1303):
        super().setup(peers=peers, maxTimeout=maxTimeout, **rest_1303)
        self._state.peers = peers
        self._state.maxTimeout = maxTimeout
        self._state.currentRole = Follower
        self._state.currentTerm = 0
        self._state.votedFor = None
        self._state.log = [LogEntry(term=0, client=None, command=None)]
        self._state.commitIndex = 0
        self._state.lastApplied = 0
        self._state.nextIndex = dict(((p, 1) for p in self._state.peers))
        self._state.matchIndex = dict(((p, 0) for p in self._state.peers))
        self._state.last_seen_leader = None
        self._state._dispatch_table = {Follower: self.follower_term, Candidate: self.candidate_term, Leader: self.leader_term}

    def run(self):
        while True:
            if (self._state.commitIndex > self._state.lastApplied):
                self._state.lastApplied += 1
                self.commit_to_state_machine()
            termTimeout = (random.randint(int((self._state.maxTimeout / 2)), self._state.maxTimeout) / 1000)
            self._state._dispatch_table[self._state.currentRole](termTimeout)

    def follower_term(self, termTimeout):
        super()._label('_st_label_374', block=False)
        term = None

        def ExistentialOpExpr_375():
            nonlocal term
            for (_, _, (_ConstantPattern397_, term, _, _, _, _, _)) in self._ServerReceivedEvent_0:
                if (_ConstantPattern397_ == 'AppendEntries'):
                    if (term >= self._state.currentTerm):
                        return True
            return False
        _st_label_374 = 0
        self._timer_start()
        while (_st_label_374 == 0):
            _st_label_374 += 1
            if ExistentialOpExpr_375():
                for attr in dir(self):
                    if (attr.find('ReceivedEvent_') != (- 1)):
                        getattr(self, attr).clear()
                _st_label_374 += 1
            elif self._timer_expired:
                self.output('Heartbeat timeout, transitioning to Candidate state.')
                self._state.currentRole = Candidate
                _st_label_374 += 1
            else:
                super()._label('_st_label_374', block=True, timeout=termTimeout)
                _st_label_374 -= 1

    def candidate_term(self, termTimeout):
        super()._label('start_election', block=False)
        self._state.currentTerm += 1
        self.RequestVoteRPC(target=self._state.peers, term=self._state.currentTerm, candidateId=self._id, lastLogIndex=(len(self._state.log) - 1), lastLogTerm=self._state.log[(- 1)].term)
        super()._label('_st_label_439', block=False)
        leader = term = None

        def ExistentialOpExpr_505():
            nonlocal leader, term
            for (_, _, (_ConstantPattern528_, term, leader, _, _, _, _)) in self._ServerReceivedEvent_2:
                if (_ConstantPattern528_ == 'AppendEntries'):
                    if (term >= self._state.currentTerm):
                        return True
            return False
        _st_label_439 = 0
        self._timer_start()
        while (_st_label_439 == 0):
            _st_label_439 += 1
            if (len({p for (_, (_, _, p), (_ConstantPattern463_, _BoundPattern465_, _ConstantPattern466_)) in self._ServerReceivedEvent_1 if (_ConstantPattern463_ == 'RequestVoteReply') if (_BoundPattern465_ == self._state.currentTerm) if (_ConstantPattern466_ == True)}) > (len(self._state.peers) / 2)):
                self.output('Transitioning to Leader.')
                self._state.currentRole = Leader
                self._state.nextIndex = dict(((p, len(self._state.log)) for p in self._state.peers))
                self._state.matchIndex = dict(((p, 0) for p in self._state.peers))
                _st_label_439 += 1
            elif ExistentialOpExpr_505():
                self.output('Elected leader:', leader, 'Reverting to Follower.')
                self._state.currentTerm = term
                self._state.currentRole = Follower
                _st_label_439 += 1
            elif self._timer_expired:
                self.output('Election term', self._state.currentTerm, 'timeout, restarting.')
                _st_label_439 += 1
            else:
                super()._label('_st_label_439', block=True, timeout=termTimeout)
                _st_label_439 -= 1

    def leader_term(self, termTimeout):
        for (server, index) in self._state.nextIndex.items():
            self.AppendEntriesRPC(target=server, term=self._state.currentTerm, leaderId=self._id, prevLogIndex=(index - 1), prevLogTerm=self._state.log[(index - 1)].term, entries=self._state.log[index:], leaderCommit=self._state.commitIndex)
        super()._label('_st_label_589', block=False)
        _st_label_589 = 0
        self._timer_start()
        while (_st_label_589 == 0):
            _st_label_589 += 1
            if (not (self._state.currentRole is Leader)):
                return
                _st_label_589 += 1
            elif self._timer_expired:
                n = i = None

                def ExistentialOpExpr_600():
                    nonlocal n, i
                    for n in range((len(self._state.log) - 1)):
                        if ((n > self._state.commitIndex) and (len({i for i in self._state.matchIndex if (self._state.matchIndex[i] >= n)}) > (len(self._state.peers) / 2)) and (self._state.log[n].term == self._state.currentTerm)):
                            return True
                    return False
                if ExistentialOpExpr_600():
                    self._state.commitIndex = n
                _st_label_589 += 1
            else:
                super()._label('_st_label_589', block=True, timeout=(termTimeout / 2))
                _st_label_589 -= 1

    def update_term(self, term):
        if (self._state.currentTerm < term):
            self._state.currentTerm = term
            self._state.votedFor = None
            self._state.currentRole = Follower

    def is_up_to_date(self, lastLogIndex, lastLogTerm):
        return ((lastLogTerm, lastLogIndex) >= (self._state.log[(- 1)].term, (len(self._state.log) - 1)))

    def commit_to_state_machine(self):
        entry = self._state.log[self._state.lastApplied]
        self.output(entry, ' at index', self._state.lastApplied, 'applied to state machine.')
        if (self._state.currentRole is Leader):
            self.send(('Reply', entry.command, self._id), to=entry.client)

    def AppendEntriesRPC(self, target, term, leaderId, prevLogIndex, prevLogTerm, entries, leaderCommit):
        self.send(('AppendEntries', term, leaderId, prevLogIndex, prevLogTerm, entries, leaderCommit), to=target)

    def AppendEntriesReply(self, target, term, success, updatedIndex=None):
        self.send(('AppendEntriesReply', term, success, updatedIndex), to=target)

    def RequestVoteRPC(self, target, term, candidateId, lastLogIndex, lastLogTerm):
        self.send(('RequestVote', term, candidateId, lastLogIndex, lastLogTerm), to=target)

    def RequestVoteReply(self, target, term, voteGranted):
        self.send(('RequestVoteReply', term, voteGranted), to=target)

    def _Server_handler_643(self, term, candidateId, lastLogIndex, lastLogTerm):
        self.update_term(term)
        if (term < self._state.currentTerm):
            self.RequestVoteReply(target=candidateId, term=self._state.currentTerm, voteGranted=False)
        elif (((self._state.votedFor is None) or (self._state.votedFor == candidateId)) and self.is_up_to_date(lastLogIndex, lastLogTerm)):
            self._state.votedFor = candidateId
            self.RequestVoteReply(target=candidateId, term=self._state.currentTerm, voteGranted=True)
        else:
            self.RequestVoteReply(target=candidateId, term=self._state.currentTerm, voteGranted=False)
    _Server_handler_643._labels = None
    _Server_handler_643._notlabels = None

    def _Server_handler_700(self, term):
        self.update_term(term)
    _Server_handler_700._labels = None
    _Server_handler_700._notlabels = None

    def _Server_handler_715(self, term, leaderId, prevLogIndex, prevLogTerm, entries, leaderCommit):
        self.update_term(term)
        if (term < self._state.currentTerm):
            self.AppendEntriesReply(target=leaderId, term=self._state.currentTerm, success=False)
        elif (not ((len(self._state.log) > prevLogIndex) and (self._state.log[prevLogIndex].term == prevLogTerm))):
            self.AppendEntriesReply(target=leaderId, term=self._state.currentTerm, success=False)
        else:
            self._state.last_seen_leader = leaderId
            for (idx, entry) in enumerate(entries):
                idx += (prevLogIndex + 1)
                if (len(self._state.log) <= idx):
                    self._state.log.append(entry)
                elif (not (self._state.log[idx].term == entry.term)):
                    del self._state.log[idx:]
            last_new_index = (prevLogIndex + len(entries))
            if (leaderCommit > self._state.commitIndex):
                self._state.commitIndex = min(leaderCommit, last_new_index)
            self.AppendEntriesReply(target=leaderId, term=self._state.currentTerm, success=True, updatedIndex=last_new_index)
    _Server_handler_715._labels = None
    _Server_handler_715._notlabels = None

    def _Server_handler_832(self, term, success, updatedIndex, server):
        self.update_term(term)
        if (self._state.currentRole is Leader):
            if success:
                self._state.nextIndex[server] = (updatedIndex + 1)
                self._state.matchIndex[server] = updatedIndex
            else:
                self._state.nextIndex[server] -= 1
    _Server_handler_832._labels = None
    _Server_handler_832._notlabels = None

    def _Server_handler_875(self, serial, client):
        if (not (self._state.currentRole is Leader)):
            self.send(('NotLeader', serial, self._state.last_seen_leader), to=client)
        else:
            self._state.log.append(LogEntry(self._state.currentTerm, client, serial))
    _Server_handler_875._labels = None
    _Server_handler_875._notlabels = None

class Client(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ClientReceivedEvent_0 = []
        self._ClientReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_1068, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_1', PatternExpr_1105, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, servers, nrequests, timeout, **rest_1303):
        super().setup(servers=servers, nrequests=nrequests, timeout=timeout, **rest_1303)
        self._state.servers = servers
        self._state.nrequests = nrequests
        self._state.timeout = timeout
        pass

    def run(self):
        target = random.choice(self._state.servers)
        req = 0
        while (req < self._state.nrequests):
            self.send(('ClientRequest', req), to=target)
            super()._label('_st_label_1065', block=False)
            leader = None

            def ExistentialOpExpr_1066():
                nonlocal leader
                for (_, _, (_ConstantPattern1084_, _BoundPattern1086_, leader)) in self._ClientReceivedEvent_0:
                    if (_ConstantPattern1084_ == 'NotLeader'):
                        if (_BoundPattern1086_ == req):
                            if (not (leader is None)):
                                return True
                return False

            def ExistentialOpExpr_1103():
                for (_, _, (_ConstantPattern1120_, _BoundPattern1122_, _)) in self._ClientReceivedEvent_1:
                    if (_ConstantPattern1120_ == 'Reply'):
                        if (_BoundPattern1122_ == req):
                            if True:
                                return True
                return False
            _st_label_1065 = 0
            self._timer_start()
            while (_st_label_1065 == 0):
                _st_label_1065 += 1
                if ExistentialOpExpr_1066():
                    self.debug('Wrong server, changing to', leader)
                    target = leader
                    for attr in dir(self):
                        if (attr.find('ReceivedEvent_') != (- 1)):
                            getattr(self, attr).clear()
                    _st_label_1065 += 1
                elif ExistentialOpExpr_1103():
                    self.output('Request', (req + 1), 'complete.')
                    req += 1
                    _st_label_1065 += 1
                elif self._timer_expired:
                    self.debug('Timeout, new random.')
                    target = random.choice(self._state.servers)
                    _st_label_1065 += 1
                else:
                    super()._label('_st_label_1065', block=True, timeout=(self._state.timeout / 1000))
                    _st_label_1065 -= 1
            else:
                if (_st_label_1065 != 2):
                    continue
            if (_st_label_1065 != 2):
                break
        self.send(('Done',), to=self.parent())

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._Node_ReceivedEvent_0 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_Node_ReceivedEvent_0', PatternExpr_1281, sources=[PatternExpr_1286], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def run(self):
        nservers = (int(sys.argv[1]) if (len(sys.argv) > 1) else 5)
        nclients = (int(sys.argv[2]) if (len(sys.argv) > 2) else 3)
        nrequests = (int(sys.argv[3]) if (len(sys.argv) > 3) else 3)
        maxtimeout = (int(sys.argv[4]) if (len(sys.argv) > 4) else 3000)
        send_failrate = (float(sys.argv[5]) if (len(sys.argv) > 5) else 0.0)
        servers = self.new(Server, num=nservers, send=send_failrate)
        self._setup(servers, (servers, maxtimeout))
        clients = self.new(Client, num=nclients)
        self._setup(clients, (list(servers), nrequests, maxtimeout))
        self._start(servers)
        self._start(clients)
        super()._label('_st_label_1272', block=False)
        c = None

        def UniversalOpExpr_1273():
            nonlocal c
            for c in clients:
                if (not PatternExpr_1288.match_iter(self._Node_ReceivedEvent_0, _BoundPattern1294_=c)):
                    return False
            return True
        _st_label_1272 = 0
        while (_st_label_1272 == 0):
            _st_label_1272 += 1
            if UniversalOpExpr_1273():
                _st_label_1272 += 1
            else:
                super()._label('_st_label_1272', block=True)
                _st_label_1272 -= 1
        self.output('All clients done.')
        self.end(servers)
