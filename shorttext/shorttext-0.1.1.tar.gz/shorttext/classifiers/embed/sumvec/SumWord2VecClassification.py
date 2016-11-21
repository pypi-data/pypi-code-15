import pickle
from collections import defaultdict

import numpy as np
from nltk import word_tokenize
from scipy.spatial.distance import cosine

# from ... import classification_exceptions as e
import utils.classification_exceptions as e

class SumEmbeddedVecClassifier:
    """
    This is a supervised classification algorithm for short text categorization.
    Each class label has a few short sentences, where each token is converted
    to an embedded vector, given by a pre-trained word-embedding model (e.g., Google Word2Vec model).
    They are then summed up and normalized to a unit vector for that particular class labels.
    To perform prediction, the input short sentences is converted to a unit vector
    in the same way. The similarity score is calculated by the cosine similarity.

    A pre-trained Google Word2Vec model can be downloaded `here
    <https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit>`_.

    Examples

    >>> # load the Word2Vec model
    >>> from gensim.models import Word2Vec
    >>> wvmodel = Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    >>>
    >>> # load the training data
    >>> import shorttext.data.data_retrieval as ret
    >>> trainclassdict = ret.subjectkeywords()
    >>>
    >>> # initialize the classifier and train
    >>> import shorttext.classifiers.embed.sumvec.SumWord2VecClassification as sumwv
    >>> classifier = sumwv.SumEmbeddedVecClassifier(wvmodel)
    >>> classifier.train(trainclassdict)
    >>>
    >>> # making predictions
    >>> classifier.score('artificial intelligence')
    {'mathematics': 0.34012238902405745,
     'physics': 0.34134023723026496,
     'theology': 0.2157201054314255}
    """

    def __init__(self, wvmodel, vecsize=300):
        """ Initialize the classifier.

        :param wvmodel: Word2Vec model
        :param vecsize: length of the embedded vectors in the model (Default: 300)
        :type wvmodel: gensim.models.word2vec.Word2Vec
        :type vecsize: int
        """
        self.wvmodel = wvmodel
        self.vecsize = vecsize
        self.trained = False

    def train(self, classdict):
        """ Train the classifier.

        If this has not been run, or a model was not loaded by :func:`~loadmodel`,
        a `ModelNotTrainedException` will be raised.

        :param classdict: training data
        :return: None
        :type classdict: dict
        """
        self.addvec = defaultdict(lambda : np.zeros(self.vecsize))
        for classtype in classdict:
            for shorttext in classdict[classtype]:
                self.addvec[classtype] += self.shorttext_to_embedvec(shorttext)
            self.addvec[classtype] /= np.linalg.norm(self.addvec[classtype])
        self.addvec = dict(self.addvec)
        self.trained = True

    def savemodel(self, nameprefix):
        """ Save the trained model into files.

        Given the prefix of the file paths, save the model into files, with name given by the prefix,
        and add "_embedvecdict.pickle" at the end. If there is no trained model, a `ModelNotTrainedException`
        will be thrown.

        :param nameprefix: prefix of the file path
        :return: None
        :type nameprefix: str
        :raise: ModelNotTrainedException
        """
        if not self.trained:
            raise e.ModelNotTrainedException()
        pickle.dump(self.addvec, open(nameprefix+'_embedvecdict.pickle', 'w'))

    def loadmodel(self, nameprefix):
        """ Load a trained model from files.

        Given the prefix of the file paths, load the model from files with name given by the prefix
        followed by "_embedvecdict.pickle".

        If this has not been run, or a model was not trained by :func:`~train`,
        a `ModelNotTrainedException` will be raised.

        :param nameprefix: prefix of the file path
        :return: None
        :type nameprefix: str
        """
        self.addvec = pickle.load(open(nameprefix+'_embedvecdict.pickle', 'r'))
        self.trained = True

    def shorttext_to_embedvec(self, shorttext):
        """ Convert the short text into an averaged embedded vector representation.

        Given a short sentence, it converts all the tokens into embedded vectors according to
        the given word-embedding model, sums
        them up, and normalize the resulting vector. It returns the resulting vector
        that represents this short sentence.

        :param shorttext: a short sentence
        :return: an embedded vector that represents the short sentence
        :type shorttext: str
        :rtype: numpy.ndarray
        """
        vec = np.zeros(self.vecsize)
        tokens = word_tokenize(shorttext)
        for token in tokens:
            if token in self.wvmodel:
                vec += self.wvmodel[token]
        norm = np.linalg.norm(vec)
        if norm!=0:
            vec /= np.linalg.norm(vec)
        return vec

    def score(self, shorttext):
        """ Calculate the scores for all the class labels for the given short sentence.

        Given a short sentence, calculate the classification scores for all class labels,
        returned as a dictionary with key being the class labels, and values being the scores.
        If the short sentence is empty, or if other numerical errors occur, the score will be `numpy.nan`.
        If neither :func:`~train` nor :func:`~loadmodel` was run, it will raise `ModelNotTrainedException`.

        :param shorttext: a short sentence
        :return: a dictionary with keys being the class labels, and values being the corresponding classification scores
        :type shorttext: str
        :rtype: dict
        :raise: ModelNotTrainedException
        """
        if not self.trained:
            raise e.ModelNotTrainedException()
        vec = self.shorttext_to_embedvec(shorttext)
        scoredict = {}
        for classtype in self.addvec:
            try:
                scoredict[classtype] = 1 - cosine(vec, self.addvec[classtype])
            except ValueError:
                scoredict[classtype] = np.nan
        return scoredict