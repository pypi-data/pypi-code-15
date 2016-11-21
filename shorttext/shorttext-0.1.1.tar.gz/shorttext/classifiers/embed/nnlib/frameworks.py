from keras.layers import Convolution1D, MaxPooling1D, Flatten, Dense, Dropout, LSTM
from keras.models import Sequential
from keras.regularizers import l2

from utils.classification_exceptions import UnequalArrayLengthsException

# Paper: Yoon Kim, "Convolutional Neural Networks for Sentence Classification," arXiv:1408.5882 (2014).
# ref: https://gist.github.com/entron/b9bc61a74e7cadeb1fec
# ref: http://cs231n.github.io/convolutional-networks/
def CNNWordEmbed(nb_labels,
                 nb_filters=1200,
                 n_gram=2,
                 maxlen=15,
                 vecsize=300,
                 cnn_dropout=0.0,
                 final_activation='softmax',
                 dense_wl2reg=0.0,
                 optimizer='adam'):
    """ Returns the convolutional neural network (CNN/ConvNet) for word-embedded vectors.

    Reference: Yoon Kim, "Convolutional Neural Networks for Sentence Classification,"
    *EMNLP* 2014, 1746-1751 (arXiv:1408.5882). [`arXiv
    <https://arxiv.org/abs/1408.5882>`_]

    :param nb_labels: number of class labels
    :param nb_filters: number of filters (Default: 1200)
    :param n_gram: n-gram, or window size of CNN/ConvNet (Default: 2)
    :param maxlen: maximum number of words in a sentence (Default: 15)
    :param vecsize: length of the embedded vectors in the model (Default: 300)
    :param cnn_dropout: dropout rate for CNN/ConvNet (Default: 0.0)
    :param final_activation: activation function. Options: softplus, softsign, relu, tanh, sigmoid, hard_sigmoid, linear. (Default: 'softmax')
    :param dense_wl2reg: L2 regularization coefficient (Default: 0.0)
    :param optimizer: optimizer for gradient descent. Options: sgd, rmsprop, adagrad, adadelta, adam, adamax, nadam. (Default: adam)
    :return: keras sequantial model for CNN/ConvNet for Word-Embeddings
    :type nb_labels: int
    :type nb_filters: int
    :type n_gram: int
    :type maxlen: int
    :type vecsize: int
    :type cnn_dropout: float
    :type final_activation: str
    :type dense_wl2reg: float
    :type optimizer: str
    :rtype: keras.model.Sequential
    """
    model = Sequential()
    model.add(Convolution1D(nb_filter=nb_filters,
                            filter_length=n_gram,
                            border_mode='valid',
                            activation='relu',
                            input_shape=(maxlen, vecsize)))
    if cnn_dropout > 0.0:
        model.add(Dropout(cnn_dropout))
    model.add(MaxPooling1D(pool_length=maxlen - n_gram + 1))
    model.add(Flatten())
    model.add(Dense(nb_labels,
                    activation=final_activation,
                    W_regularizer=l2(dense_wl2reg))
              )
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model

# two layers of CNN, maxpooling, dense
def DoubleCNNWordEmbed(nb_labels,
                       nb_filters_1=1200,
                       nb_filters_2=600,
                       n_gram=2,
                       filter_length_2=10,
                       maxlen=15,
                       vecsize=300,
                       cnn_dropout_1=0.0,
                       cnn_dropout_2=0.0,
                       final_activation='softmax',
                       dense_wl2reg=0.0,
                       optimizer='adam'):
    """ Returns the double-layered convolutional neural network (CNN/ConvNet) for word-embedded vectors.

    :param nb_labels: number of class labels
    :param nb_filters_1: number of filters for the first CNN/ConvNet layer (Default: 1200)
    :param nb_filters_2: number of filters for the second CNN/ConvNet layer (Default: 600)
    :param n_gram: n-gram, or window size of first CNN/ConvNet (Default: 2)
    :param filter_length_2: window size for second CNN/ConvNet layer (Default: 10)
    :param maxlen: maximum number of words in a sentence (Default: 15)
    :param vecsize: length of the embedded vectors in the model (Default: 300)
    :param cnn_dropout_1: dropout rate for the first CNN/ConvNet layer (Default: 0.0)
    :param cnn_dropout_2: dropout rate for the second CNN/ConvNet layer (Default: 0.0)
    :param final_activation: activation function. Options: softplus, softsign, relu, tanh, sigmoid, hard_sigmoid, linear. (Default: 'softmax')
    :param dense_wl2reg: L2 regularization coefficient (Default: 0.0)
    :param optimizer: optimizer for gradient descent. Options: sgd, rmsprop, adagrad, adadelta, adam, adamax, nadam. (Default: adam)
    :return: keras sequantial model for CNN/ConvNet for Word-Embeddings
    :type nb_labels: int
    :type nb_filters_1: int
    :type nb_filters_2: int
    :type n_gram: int
    :type filter_length_2: int
    :type maxlen: int
    :type vecsize: int
    :type cnn_dropout_1: float
    :type cnn_dropout_2: float
    :type final_activation: str
    :type dense_wl2reg: float
    :type optimizer: str
    :rtype: keras.model.Sequential
    """
    model = Sequential()
    model.add(Convolution1D(nb_filter=nb_filters_1,
                            filter_length=n_gram,
                            border_mode='valid',
                            activation='relu',
                            input_shape=(maxlen, vecsize)))
    if cnn_dropout_1 > 0.0:
        model.add(Dropout(cnn_dropout_1))
    model.add(Convolution1D(nb_filter=nb_filters_2,
                            filter_length=filter_length_2,
                            border_mode='valid',
                            activation='relu'))
    if cnn_dropout_2 > 0.0:
        model.add(Dropout(cnn_dropout_2))
    model.add(MaxPooling1D(pool_length=maxlen - n_gram -filter_length_2 + 1))
    model.add(Flatten())
    model.add(Dense(nb_labels,
                    activation=final_activation,
                    W_regularizer=l2(dense_wl2reg)))

    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model

# C-LSTM
# Chunting Zhou, Chonglin Sun, Zhiyuan Liu, Francis Lau,
# "A C-LSTM Neural Network for Text Classification", arXiv:1511.08630 (2015).
def CLSTMWordEmbed(nb_labels,
                   nb_filters=1200,
                   n_gram=2,
                   maxlen=15,
                   vecsize=300,
                   cnn_dropout=0.0,
                   nb_rnnoutdim=1200,
                   rnn_dropout=0.2,
                   final_activation='softmax',
                   dense_wl2reg=0.0,
                   optimizer='adam'):
    """ Returns the C-LSTM neural networks for word-embedded vectors.

    Reference: Chunting Zhou, Chonglin Sun, Zhiyuan Liu, Francis Lau,
    "A C-LSTM Neural Network for Text Classification,"
    (arXiv:1511.08630). [`arXiv
    <https://arxiv.org/abs/1511.08630>`_]

    :param nb_labels: number of class labels
    :param nb_filters: number of filters (Default: 1200)
    :param n_gram: n-gram, or window size of CNN/ConvNet (Default: 2)
    :param maxlen: maximum number of words in a sentence (Default: 15)
    :param vecsize: length of the embedded vectors in the model (Default: 300)
    :param cnn_dropout: dropout rate for CNN/ConvNet (Default: 0.0)
    :param nb_rnnoutdim: output dimension for the LSTM networks (Default: 1200)
    :param rnn_dropout: dropout rate for LSTM (Default: 0.2)
    :param final_activation: activation function. Options: softplus, softsign, relu, tanh, sigmoid, hard_sigmoid, linear. (Default: 'softmax')
    :param dense_wl2reg: L2 regularization coefficient (Default: 0.0)
    :param optimizer: optimizer for gradient descent. Options: sgd, rmsprop, adagrad, adadelta, adam, adamax, nadam. (Default: adam)
    :return: keras sequantial model for CNN/ConvNet for Word-Embeddings
    :type nb_labels: int
    :type nb_filters: int
    :type n_gram: int
    :type maxlen: int
    :type vecsize: int
    :type cnn_dropout: float
    :type nb_rnnoutdim: int
    :type rnn_dropout: float
    :type final_activation: str
    :type dense_wl2reg: float
    :type optimizer: str
    :rtype: keras.model.Sequential
    """
    model = Sequential()
    model.add(Convolution1D(nb_filter=nb_filters,
                            filter_length=n_gram,
                            border_mode='valid',
                            activation='relu',
                            input_shape=(maxlen, vecsize)))
    if cnn_dropout > 0.0:
        model.add(Dropout(cnn_dropout))
    model.add(MaxPooling1D(pool_length=maxlen - n_gram + 1))
    model.add(LSTM(nb_rnnoutdim))
    if rnn_dropout > 0.0:
        model.add(Dropout(rnn_dropout))
    model.add(Dense(nb_labels,
                    activation=final_activation,
                    W_regularizer=l2(dense_wl2reg)
                    )
              )
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model

def DenseWordEmbed(nb_labels,
                   dense_nb_nodes=[],
                   dense_actfcn=[],
                   vecsize=300,
                   reg_coef=0.1,
                   final_activiation='softmax',
                   optimizer='adam'):
    """ Return layers of dense neural network.

    Return layers of dense neural network. This assumes the input to be a rank-1 vector.

    :param nb_labels: number of class labels
    :param dense_nb_nodes: number of nodes in each later (Default: [])
    :param dense_actfcn: activation functions for each layer (Default: [])
    :param vecsize: length of the embedded vectors in the model (Default: 300)
    :param reg_coef: regularization coefficient (Default: 0.1)
    :param final_activiation: activation function of the final layer (Default: softmax)
    :param optimizer: optimizer for gradient descent. Options: sgd, rmsprop, adagrad, adadelta, adam, adamax, nadam. (Default: adam)
    :return: keras sequential model for dense neural network
    :type nb_labels: int
    :type dense_nb_nodes: list
    :type dense_actfcn: list
    :type vecsize: int
    :type reg_coef: float
    :type final_activiation: str
    :type optimizer: str
    :rtype: keras.models.Sequential
    """
    if len(dense_nb_nodes)!=len(dense_actfcn):
        raise UnequalArrayLengthsException(dense_nb_nodes, dense_actfcn)
    nb_layers = len(dense_nb_nodes)

    model = Sequential()
    if nb_layers==0:
        model.add(Dense(nb_labels, input_dim=vecsize, activation=final_activiation, W_regularizer=l2(reg_coef)))
    else:
        for nb_nodes, activation in zip(dense_nb_nodes, dense_actfcn):
            model.add(Dense(nb_nodes, activation=activation, W_regularizer=l2(reg_coef)))
        model.add(Dense(nb_labels, activation=final_activiation, W_regularizer=l2(reg_coef)))
    model.compile(loss='categorical_crossentropy', optimizer=optimizer)

    return model
