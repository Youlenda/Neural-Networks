# -*- coding: utf-8 -*-
"""hw2-q2-pca.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N7qOcf-LaBB626UHHHIFE39iZrpGZJqf
"""

from keras.datasets import mnist
from keras.utils import np_utils

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test  = x_test.reshape (10000, 784)

x_train = x_train.astype('float32')
x_test  = x_test.astype ('float32')

x_train /= 255
x_test  /= 255

y_train = np_utils.to_categorical(y_train)
y_test  = np_utils.to_categorical(y_test)

from sklearn.decomposition import PCA
import numpy as np

pca = PCA(n_components=100)
x_train_pca = pca.fit_transform(x_train)
x_test_pca  = pca.transform(x_test)
explained_var = pca.explained_variance_ratio_
np.sum(explained_var[0:100])
pca_out = explained_var[0:100]

from keras.models import Sequential
from keras.layers import Dense

net = Sequential()
net.add(Dense(512, activation  = 'relu', input_shape = (100,)))
net.add(Dense(512, activation  = 'relu'))
net.add(Dense(10 , activation  = 'softmax'))

from keras import optimizers

sgd = optimizers.SGD(lr=0.01)
net.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
net.summary()

import timeit

start = timeit.default_timer()

trained_model = net.fit(x_train_pca, y_train, batch_size = 32, epochs = 30, validation_split = 0.2)
history = trained_model.history

stop = timeit.default_timer()
print('Time: ', stop - start)