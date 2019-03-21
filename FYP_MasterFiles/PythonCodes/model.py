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
from airfoilShapeExtractor import X_airfoil, Y_airfoil, X_airfoil3U, Y_airfoil3U, X_airfoil_negGeometry, Y_airfoil_negGeometry, X_airfoil3U_negGeometry, Y_airfoil3U_negGeometry
from helperFunctions import *


"""
class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []
    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
"""

def encoderDecoder():
    name = 'EncoderDecoder'
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
    if checkSaveExist(name) == 1:
        loadWeights(cnn, name)

    cnnModel = cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    #history = LossHistory()
    if checkSaveExist(name) == 0:
        cnnModel = cnn.fit(X_array3U_negGeometry[:], Y_array3U[:], validation_split=0.3, batch_size = 10, epochs = 200)
        # Serialize model to JSON
        model_json = cnn.to_json()
        weightsFile = name + '.h5'
        jsonFile = name + '.json'
        with open(jsonFile, 'w') as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        cnn.save_weights(weightsFile)
        print("Saved model to disk as {}.".format(weightsFile))

    y_predict = cnn.predict(np.reshape(X_airfoil3U_negGeometry, (1, 128, 256, 3)))
    print('X velocity of predicted array is {}'.format(y_predict[:,:,:,0]))
    
    # Plot X velocity
    tempName = name + 'Xvelocity'
    plotArray(y_predict[0,:,:,0], tempName)
    
    # Plot Y velocity
    tempName = name + 'Yvelocity'
    plotArray(y_predict[0,:,:,1], tempName)
    
    # Plot Z velocity    
    tempName = name + 'Zvelocity'
    plotArray(y_predict[0,:,:,2], tempName)
    
    plotLoss(cnnModel, "test")

    
    return y_predict

# For trial purposes
y_predict=encoderDecoder()
y_predictX=y_predict[0:,:,:,0]
y_predictY=y_predict[0:,:,:,1]
y_predictZ=y_predict[0:,:,:,2]
#y_predict = cnn.predict(np.reshape(X_array3U[14],(1,128,256,3)))
