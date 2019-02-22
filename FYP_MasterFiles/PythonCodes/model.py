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
from keras.callbacks import History
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
from excelToNumpy import X_array, Y_array, X_array3U, Y_array3U, X_array_negGeometry, Y_array_negGeometry, X_array3U_negGeometry, Y_array3U_negGeometry
from helperFunctions import *


"""
class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []
    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
"""

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

    # Load weights
    if checkSaveExist() == 1:
        loadWeights(cnn)

    cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    #history = LossHistory()
    if checkSaveExist() == 0:
        cnnModel = cnn.fit(X_array3U_negGeometry[:50], Y_array3U[:50], validation_split=0.3, batch_size = 1, epochs = 100)

    # Serialize model to JSON
    model_json = cnn.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    cnn.save_weights("model.h5")
    print("Saved model to disk")

    y_predict = cnn.predict(np.reshape(X_array3U_negGeometry[50], (1, 128, 256, 3)))
    print(y_predict[:,:,:,0])
    plotArray(y_predict[:,:,:,0])
    plotLoss(cnnModel)

# For trial purposes
encoderDecoder()
#y_predict = cnn.predict(np.reshape(X_array3U[14],(1,128,256,3)))
