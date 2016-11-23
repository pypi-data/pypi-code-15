from tf_core.document_corpus import DocumentCorpus
from tagging_common import universal_sentence_tagger_hub
#from tagging_common_parallel import universal_sentence_tagger_hub
#from nltk.tag.simplify   import (simplify_brown_tag, simplify_wsj_tag,
#                                 simplify_indian_tag, simplify_alpino_tag,
#                                 simplify_tag)
from nltk.tag.sequential import (DefaultTagger, NgramTagger, AffixTagger,
                                 RegexpTagger, #<--TODO
                                 ClassifierBasedPOSTagger)
import nltk.tag.brill
from nltk.tag.brill      import BrillTagger
from nltk.tag.brill_trainer import BrillTaggerTrainer
from nltk.tag.tnt        import TnT
from nltk.tag.hunpos     import HunposTagger
from nltk.tag.stanford   import StanfordTagger
#from nltk.tag.crf        import MalletCRF
from django.conf import settings
from nltk.corpus import brown, treebank, nps_chat
from nltk.tag.stanford import StanfordPOSTagger
import os
import re


def pos_tagger_hub(input_dict):
    if input_dict['pos_tagger'].__class__.__name__=="LatinoObject": #check if this is a latino object
        from ...latino.library_gen import latino_pos_tag
        adc= executeFunction.apply_async([latino_pos_tag,input_dict],queue="windows").wait()['adc'] \
            if settings.USE_WINDOWS_QUEUE else latino_pos_tag(input_dict)
    else:
        adc= universal_sentence_tagger_hub(input_dict)['adc']

    number_of_letters=int(input_dict['num_of_letters'])
    if number_of_letters!=-1:
        element_annotation_name = input_dict['element_annotation']
        output_annotation_name = input_dict['output_feature']
        for doc in adc.documents:
            for annotation in doc.get_annotations(element_annotation_name):
                if not output_annotation_name in annotation.features:
                    print input_dict['pos_tagger'],annotation.features
                    print doc.features
                else:
                    annotation.features[output_annotation_name]=annotation.features[output_annotation_name][0:number_of_letters]

    return {'adc': adc }


def extract_pos_tagger_name(input_dict):
    tagger=input_dict['pos_tagger']
    tagger_name=tagger['object'].__class__.__name__ if not tagger.__class__.__name__=="LatinoObject" else tagger.name
    tagger_name=re.search(r'[A-Za-z\.0-9]+',tagger_name).group() #extracts valid characters
    if not tagger.__class__.__name__=="LatinoObject" and 'pretrained' in tagger:
        if tagger['pretrained']:
            if tagger_name == 'ClassifierBasedPOSTagger':
                tagger_name = 'MaxentPosTagger-pretrained'
            else:
                tagger_name = 'PerceptronTagger-pretrained'
        
    return {'pos_tagger_name': tagger_name}


def corpus_reader(corpus, chunk):
    if type(corpus)==DocumentCorpus:
        raise NotImplementedError
    else:
        tagged_posts = getattr(corpus, "tagged_posts", None)
        reverse = False
        if chunk[0] == '^':
            reverse = True
            chunk = chunk[1:]
        if callable(tagged_posts):
            if chunk[-1] == '%':
                index = (float(chunk[:-1])/100) * len(corpus.tagged_posts())
            else:
                index = int(chunk)
            if reverse:
                return corpus.tagged_posts()[int(index):]
            return corpus.tagged_posts()[:int(index)]
        else:
            if chunk[-1] == '%':
                index = (float(chunk[:-1])/100) * len(corpus.tagged_sents())
            else:
                index = int(chunk)
            if reverse:
                return corpus.tagged_sents()[int(index):]
            return corpus.tagged_sents()[:int(index)]


def nltk_default_pos_tagger(input_dict):
    """
    A tagger that assigns the same tag to every token.

        >>> from nltk.tag.sequential import DefaultTagger
        >>> default_tagger = DefaultTagger('NN')
        >>> default_tagger.tag('This is a test'.split())
        [('This', 'NN'), ('is', 'NN'), ('a', 'NN'), ('test', 'NN')]

    This tagger is recommended as a backoff tagger, in cases where
    a more powerful tagger is unable to assign a tag to the word
    (e.g. because the word was not seen during training).

    :param default_tag: The default tag "%(default)s". Set this to a different tag, such as "NN",
            to change the default tag.

    :returns pos_tagger: A python dictionary containing the POS tagger
        object and its arguments.
    """
    from nltk.tag import DefaultTagger
    return {'pos_tagger': {
        'function':'tag_sents',
        'object': DefaultTagger(input_dict.get('default_tag','-None-'))
        }
    }

#SEQUENTIAL TAGGERS
def nltk_affix_pos_tagger(input_dict):
    """
    A tagger that chooses a token's tag based on a leading or trailing
    substring of its word string.  (It is important to note that these
    substrings are not necessarily "true" morphological affixes).  In
    particular, a fixed-length substring of the word is looked up in a
    table, and the corresponding tag is returned.  Affix taggers are
    typically constructed by training them on a tagged corpus.

    :param training_corpus: A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta,
        or an Annotated Document Corpus in the standard TextFlows' adc format
    :param backoff_tagger: A backoff tagger, to be used by the new
        tagger if it encounters an unknown context.
    :param affix_length: The length of the affixes that should be
        considered during training and tagging.  Use negative
        numbers for suffixes.
    :param min_stem_length: Any words whose length is less than
        min_stem_length+abs(affix_length) will be assigned a
        tag of None by this tagger.

    :returns pos_tagger: A python dictionary containing the POS tagger object and its arguments.
    """
    chunk = input_dict['training_corpus']['chunk']
    corpus = input_dict['training_corpus']['corpus']
    training_corpus=corpus_reader(corpus, chunk)
    backoff_tagger=input_dict['backoff_tagger']['object'] if input_dict['backoff_tagger'] else DefaultTagger('-None-')
    affix_length=int(input_dict['affix_length'])
    min_stem_length=int(input_dict['min_stem_length'])
    cutoff=int(input_dict['cutoff']) #default 0


    return {'pos_tagger': {
                'function':'tag_sents',
                'object': AffixTagger(training_corpus, affix_length=affix_length, cutoff=cutoff,
                         min_stem_length=min(min_stem_length, 2), backoff=backoff_tagger)
        }
    }



def nltk_ngram_pos_tagger(input_dict):
    """
    A tagger that chooses a token's tag based on its word string and
    on the preceding n word's tags.  In particular, a tuple
    (tags[i-n:i-1], words[i]) is looked up in a table, and the
    corresponding tag is returned.  N-gram taggers are typically
    trained on a tagged corpus.

    Train a new NgramTagger using the given training data or
    the supplied model.  In particular, construct a new tagger
    whose table maps from each context (tag[i-n:i-1], word[i])
    to the most frequent tag for that context.  But exclude any
    contexts that are already tagged perfectly by the backoff
    tagger.

    :param training_corpus: A tagged corpus included with NLTK, such as treebank, brown, cess_esp, floresta,
        or an Annotated Document Corpus in the standard TextFlows' adc format
    :param backoff_tagger: A backoff tagger, to be used by the new
        tagger if it encounters an unknown context.
    :param cutoff: If the most likely tag for a context occurs
        fewer than *cutoff* times, then exclude it from the
        context-to-tag table for the new tagger.
    :param n:  N-gram is a contiguous sequence of n items from a given sequence of text or speech.

    :returns pos_tagger: A python dictionary containing the POS tagger object and its arguments.
    """
    chunk = input_dict['training_corpus']['chunk']
    corpus = input_dict['training_corpus']['corpus']
    training_corpus=corpus_reader(corpus, chunk)
    backoff_tagger=input_dict['backoff_tagger']['object'] if input_dict['backoff_tagger'] else DefaultTagger('-None-')
    n=int(input_dict['n']) #default 2
    cutoff=int(input_dict['cutoff']) #default 0

    return {'pos_tagger': {
                'function':'tag_sents',
                'object': NgramTagger(n, train=training_corpus, model=None,
                 backoff=backoff_tagger, cutoff=0)
            }
    }


# CLASSIFIER TAGGERS
def nltk_phonetic_classifier_based_pos_tagger(input_dict):
    raise NotImplementedError

def nltk_classifier_based_pos_tagger(input_dict):
    """
    A sequential tagger that uses a classifier to choose the tag for
    each token in a sentence.  The featureset input for the classifier
    is generated by a feature detector function::

        feature_detector(tokens, index, history) -> featureset

    Where tokens is the list of unlabeled tokens in the sentence;
    index is the index of the token for which feature detection
    should be performed; and history is list of the tags for all
    tokens before index.

    Construct a new classifier-based sequential tagger.

    :param training_corpus: A tagged corpus consisting of a list of tagged
        sentences, where each sentence is a list of (word, tag) tuples.
    :param backoff_tagger: A backoff tagger, to be used by the new tagger
        if it encounters an unknown context.

TODO: odloci se katerega se obdrzi od naslednjih dveh

    :param classifier_builder: A function used to train a new
        classifier based on the data in *train*.  It should take
        one argument, a list of labeled featuresets (i.e.,
        (featureset, label) tuples).
    :param classifier: The classifier that should be used by the
        tagger.  #This is only useful if you want to manually
        construct the classifier; normally, you would use *train*
        instead.
    :param backoff_tagger: A backoff tagger, used if this tagger is
        unable to determine a tag for a given token.
    :param cutoff_prob: If specified, then this tagger will fall
        back on its backoff tagger if the probability of the most
        likely tag is less than *cutoff_prob*.

    :returns pos_tagger: A python dictionary containing the POS tagger
        object and its arguments.
    """
    chunk = input_dict['training_corpus']['chunk']
    corpus = input_dict['training_corpus']['corpus']
    training_corpus=corpus_reader(corpus, chunk)
    backoff_tagger=input_dict['backoff_tagger']['object'] if input_dict['backoff_tagger'] else DefaultTagger('-None-')
    classifier=None #(input_dict['classifier'])
    cutoff_prob=int(input_dict['cutoff_prob']) if input_dict['cutoff_prob'] else None

    import nltk
    tagger_object=ClassifierBasedPOSTagger(train=training_corpus, classifier=classifier,
                 backoff=backoff_tagger, cutoff_prob=cutoff_prob)
    return {'pos_tagger': {
                'function':'tag_sents',
                'object': tagger_object
            }
    }

#BRILL TAGGERS
def nltk_brill_pos_tagger(input_dict):
    """Brill's transformational rule-based tagger.  Brill taggers use an
    initial tagger (such as ``tag.DefaultTagger``) to assign an initial
    tag sequence to a text; and then apply an ordered list of
    transformational rules to correct the tags of individual tokens.
    These transformation rules are specified by the ``BrillRule``
    interface.

    Brill taggers can be created directly, from an initial tagger and
    a list of transformational rules; but more often, Brill taggers
    are created by learning rules from a training corpus, using either
    ``BrillTaggerTrainer`` or ``FastBrillTaggerTrainer``.

    :param training_corpus: A tagged corpus consisting of a list of tagged
        sentences, where each sentence is a list of (word, tag) tuples.
    :param initial_tagger: The initial tagger. Brill taggers use an initial
        tagger (such as ``DefaultTagger``) to assign an initial tag
        sequence to a text.
    :param max_rules: The maximum number of transformations to be created
    :param min_score: The minimum acceptable net error reduction
        that each transformation must produce in the corpus.
    :param deterministic: If true, then choose between rules that
        have the same score by picking the one whose __repr__
        is lexicographically smaller.  If false, then just pick the
        first rule we find with a given score -- this will depend
        on the order in which keys are returned from dictionaries,
        and so may not be the same from one run to the next.  If
        not specified, treat as true iff trace > 0.
    :param templates: templates to be used in training

    :returns pos_tagger: A python dictionary containing the POS tagger
        object and its arguments.
    """
    chunk = input_dict['training_corpus']['chunk']
    corpus = input_dict['training_corpus']['corpus']
    training_corpus = corpus_reader(corpus, chunk)
    initial_tagger = input_dict['initial_tagger']['object'] if input_dict['initial_tagger'] else DefaultTagger('-None-')
    max_rules = int(input_dict['max_rules']) #default 200
    min_score = int(input_dict['min_score']) #default 2
    deterministic = True

    templates = getattr(nltk.tag.brill,input_dict['templates'])()

    trainer = BrillTaggerTrainer(initial_tagger, templates, deterministic=deterministic, trace=settings.DEBUG)
    brill_tagger = trainer.train(training_corpus, max_rules=max_rules, min_score=min_score) #return BrillTagger(self._initial_tagger, rules)

    if settings.DEBUG:
        for rule in brill_tagger.rules():
            print(str(rule))

    return {'pos_tagger': {
                'function':'tag_sents',
                'object': brill_tagger
            }
    }

import time, os
import re
from collections import defaultdict

from nltk import TaggerI, FreqDist, untag, config_megam
from nltk.classify.maxent import MaxentClassifier
                  

class MaxentPosTagger(TaggerI):

    """
    MaxentPosTagger is a part-of-speech tagger based on Maximum Entropy models.
    """
    def train(self, train_sents, algorithm='megam', rare_word_cutoff=5,
              rare_feat_cutoff=5, uppercase_letters='[A-Z]', trace=3,
              **cutoffs):
        self.uppercase_letters = uppercase_letters
        self.word_freqdist = self.gen_word_freqs(train_sents)
        self.featuresets = self.gen_featsets(train_sents,
                rare_word_cutoff)
        self.features_freqdist = self.gen_feat_freqs(self.featuresets)
        self.cutoff_rare_feats(self.featuresets, rare_feat_cutoff)

        t1 = time.time()
        self.classifier = MaxentClassifier.train(self.featuresets, algorithm,
                                                 trace, **cutoffs)
        t2 = time.time()
        if trace > 0:
            print "time to train the classifier: {0}".format(round(t2-t1, 3))

    def gen_feat_freqs(self, featuresets):
        features_freqdist = defaultdict(int)
        for (feat_dict, tag) in featuresets:
            for (feature, value) in feat_dict.items():
                features_freqdist[ ((feature, value), tag) ] += 1
        return features_freqdist

    def gen_word_freqs(self, train_sents):
        word_freqdist = FreqDist()
        for tagged_sent in train_sents:
            for (word, _tag) in tagged_sent:
                word_freqdist[word] += 1
        return word_freqdist

    def gen_featsets(self, train_sents, rare_word_cutoff):
        featuresets = []
        for tagged_sent in train_sents:
            history = []
            untagged_sent = untag(tagged_sent)
            for (i, (_word, tag)) in enumerate(tagged_sent):
                featuresets.append( (self.extract_feats(untagged_sent, i,
                    history, rare_word_cutoff), tag) )
                history.append(tag)
        return featuresets


    def cutoff_rare_feats(self, featuresets, rare_feat_cutoff):
        never_cutoff_features = set(['w','t'])

        for (feat_dict, tag) in featuresets:
            for (feature, value) in feat_dict.items():
                feat_value_tag = ((feature, value), tag)
                if self.features_freqdist[feat_value_tag] < rare_feat_cutoff:
                    if feature not in never_cutoff_features:
                        feat_dict.pop(feature)


    def extract_feats(self, sentence, i, history, rare_word_cutoff=5):
        features = {}
        hyphen = re.compile("-")
        number = re.compile("\d")
        uppercase = re.compile(self.uppercase_letters)

        #get features: w-1, w-2, t-1, t-2.
        #takes care of the beginning of a sentence
        if i == 0: #first word of sentence
            features.update({"w-1": "<START>", "t-1": "<START>",
                             "w-2": "<START>", "t-2 t-1": "<START> <START>"})
        elif i == 1: #second word of sentence
            features.update({"w-1": sentence[i-1], "t-1": history[i-1],
                             "w-2": "<START>",
                             "t-2 t-1": "<START> %s" % (history[i-1])})
        else:
            features.update({"w-1": sentence[i-1], "t-1": history[i-1],
                "w-2": sentence[i-2],
                "t-2 t-1": "%s %s" % (history[i-2], history[i-1])})

        #get features: w+1, w+2. takes care of the end of a sentence.
        for inc in [1, 2]:
            try:
                features["w+%i" % (inc)] = sentence[i+inc]
            except IndexError:
                features["w+%i" % (inc)] = "<END>"

        if self.word_freqdist[sentence[i]] >= rare_word_cutoff:
            #additional features for 'non-rare' words
            features["w"] = sentence[i]

        else: #additional features for 'rare' or 'unseen' words
            features.update({"suffix(1)": sentence[i][-1:],
                "suffix(2)": sentence[i][-2:], "suffix(3)": sentence[i][-3:],
                "suffix(4)": sentence[i][-4:], "prefix(1)": sentence[i][:1],
                "prefix(2)": sentence[i][:2], "prefix(3)": sentence[i][:3],
                "prefix(4)": sentence[i][:4]})
            if hyphen.search(sentence[i]) != None:
                #set True, if regex is found at least once
                features["contains-hyphen"] = True
            if number.search(sentence[i]) != None:
                features["contains-number"] = True
            if uppercase.search(sentence[i]) != None:
                features["contains-uppercase"] = True

        return features


    def tag(self, sentence, rare_word_cutoff=5):
        history = []
        for i in xrange(len(sentence)):
            featureset = self.extract_feats(sentence, i, history,
                                               rare_word_cutoff)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

    def tag_sents(self, sentences):
        return [self.tag(sent) for sent in sentences]


def nltk_maxent_pos_tagger(input_dict):
    if not input_dict['training_corpus']:
        maxent_tagger = nltk.data.load('taggers/maxent_treebank_pos_tagger/english.pickle')
        pretrained = True
    else:
        pretrained = False
        nltk.config_megam(settings.MEGAM_EXECUTABLE_PATH)

        maxent_tagger = MaxentPosTagger()
        chunk = input_dict['training_corpus']['chunk']
        corpus = input_dict['training_corpus']['corpus']
        training_corpus=corpus_reader(corpus, chunk)
        if training_corpus:
            maxent_tagger.train(training_corpus)
        else:
            raise AttributeError

    return {'pos_tagger': {
                'function':'tag_sents',
                'object': maxent_tagger,
                'pretrained': pretrained
            }
    }

from nltk.tag.perceptron import PerceptronTagger

def nltk_perceptron_pos_tagger(input_dict):
    if not input_dict['training_corpus']:
        perceptron_tagger = PerceptronTagger()
        pretrained = True
    else: 
        pretrained = False   
        perceptron_tagger = PerceptronTagger(load=False)
        chunk = input_dict['training_corpus']['chunk']
        corpus = input_dict['training_corpus']['corpus']
        training_corpus=corpus_reader(corpus, chunk)
        perceptron_tagger.train(list(training_corpus))

    return {'pos_tagger': {
                'function':'tag_sents',
                'object': perceptron_tagger,
                'pretrained': pretrained
            }
    }

def stanford_pos_tagger(input_dict):
    tagger = StanfordPOSTagger(model_filename=settings.STANFORD_POS_TAGGER_MODEL, path_to_jar=settings.STANFORD_POS_TAGGER_JAR, java_options='-mx4000m')
    return {'pos_tagger': {
                'function':'tag_sents',
                'object': tagger
            }
    }



