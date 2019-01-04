# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 00:45:31 2018

@author: Nigel
"""

from keras.models import Sequential
from keras.layers import Conv2D, Conv1D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import LeakyReLU
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
from excelToNumpy import X_array, Y_array, X_array_negGeometry, Y_array_negGeometry


cnn = Sequential()
cnn.add(Conv1D(201, (1), input_shape=(101, 201), activation='relu'))

#cnn.add(Conv2D(32, (1, 1), activation='relu'))
#cnn.add(Conv2D(32, (1, 1), activation='relu'))
#cnn.add(MaxPooling2D(pool_size=(2, 2)))
#cnn.add(Flatten())
#cnn.add(Dense(units=10, activation='linear'))
#cnn.add(Dense(units=1, activation='sigmoid'))
cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

cnn.fit(X_array_negGeometry[:8], Y_array[:8], batch_size = 1, nb_epoch = 1000)


y_predict = cnn.predict(np.reshape(X_array[8],(1,101,201)))
