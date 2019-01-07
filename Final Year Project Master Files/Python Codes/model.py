# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 00:45:31 2018

@author: Nigel
"""

from keras.models import Sequential
from keras.layers import Conv2D, Conv1D, Conv2DTranspose
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import LeakyReLU
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
from excelToNumpy import X_array, Y_array, Y_array3U, X_array_negGeometry, Y_array_negGeometry, X_array3U_negGeometry, Y_array3U_negGeometry


def encoderDecoder():
    cnn = Sequential()
    cnn.add(Conv2D(128, (8,16), padding='same', input_shape=(128, 256, 3), activation='relu'))
    cnn.add(Conv2D(512, (4,4), padding='same', activation='relu'))

    cnn.add(Conv2DTranspose(512, (8,8), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(256, (4,8), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(32, (2,2), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(3, (2,2), padding='same', activation='relu'))
    
    #cnn.add(MaxPooling2D(pool_size=(2, 2)))
    #cnn.add(Flatten())

    cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    
    cnn.fit(X_array3U_negGeometry[:14], Y_array3U[:14], batch_size = 1, epochs = 1000)

# For trial purposes
encoderDecoder()
y_predict = cnn.predict(np.reshape(X_array3U[14],(1,128,256,3)))
