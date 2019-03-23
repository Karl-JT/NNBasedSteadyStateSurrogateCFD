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
#from excelToNumpy import X_array, Y_array, X_array3U, Y_array3U, X_array_negGeometry, Y_array_negGeometry, X_array3U_negGeometry, Y_array3U_negGeometry
#from excelToNumpy import X_arrayXVelWPressure_negGeometry, Y_arrayXVelWPressure_negGeometry, X_arrayYVelWPressure_negGeometry, Y_arrayYVelWPressure_negGeometry
#from airfoilShapeExtractor import X_airfoil, Y_airfoil, X_airfoil3U, Y_airfoil3U, X_airfoil_negGeometry, Y_airfoil_negGeometry, X_airfoil3U_negGeometry, Y_airfoil3U_negGeometry
#from airfoilShapeExtractor import X_airfoilXVelWPressure_negGeometry, X_airfoilYVelWPressure_negGeometry, Y_airfoilXVelWPressure_negGeometry, Y_airfoilYVelWPressure_negGeometry
from helperFunctions import *


"""
class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []
    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))
"""

def encoderDecoderXVelocity():
    name = 'EncoderDecoderXVel'
    cnn = Sequential()
    cnn.add(Conv2D(128, (8,16), padding='same', input_shape=(128, 256, 2), activation='relu'))
    cnn.add(Conv2D(512, (4,4), padding='same', activation='relu'))

    cnn.add(Conv2DTranspose(512, (8,8), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(256, (4,8), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(32, (2,2), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(2, (2,2), padding='same', activation='relu'))

    #cnn.add(MaxPooling2D(pool_size=(2, 2))) 
    #cnn.add(Flatten())

    # Load weights
    if checkSaveExist(name) == 1:
        loadWeights(cnn, name)

    cnnModel = cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    #history = LossHistory()
    if checkSaveExist(name) == 0:
        cnnModel = cnn.fit(X_arrayXVelWPressure_negGeometry[:], Y_arrayXVelWPressure_negGeometry[:], validation_split=0.3, batch_size = 1, epochs = 5)
        # Serialize model to JSON
        model_json = cnn.to_json()
        weightsFile = name + '.h5'
        jsonFile = name + '.json'
        with open(jsonFile, 'w') as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        cnn.save_weights(weightsFile)
        print("Saved model to disk as {}.".format(weightsFile))

    y_predictXVel = cnn.predict(np.reshape(X_airfoilXVelWPressure_negGeometry, (1, 128, 256, 2)))
    print('X velocity of predicted array is {}'.format(y_predictXVel[:,:,:,0]))
    
    # Plot X velocity
    tempName = name + 'Xvelocity'
    plotArray(y_predictXVel[0,:,:,0], tempName)
    
    
    plotLoss(cnnModel, "encoderDecoderXVelocityLoss")
    
    return y_predictXVel

def encoderDecoderYVelocity():
    name = 'EncoderDecoder'
    cnn = Sequential()
    cnn.add(Conv2D(128, (8,16), padding='same', input_shape=(128, 256, 2), activation='relu'))
    cnn.add(Conv2D(512, (4,4), padding='same', activation='relu'))

    cnn.add(Conv2DTranspose(512, (8,8), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(256, (4,8), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(32, (2,2), padding='same', activation='relu'))
    cnn.add(Conv2DTranspose(2, (2,2), padding='same', activation='relu'))

    #cnn.add(MaxPooling2D(pool_size=(2, 2))) 
    #cnn.add(Flatten())

    # Load weights
    if checkSaveExist(name) == 1:
        loadWeights(cnn, name)

    cnnModel = cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    #history = LossHistory()
    if checkSaveExist(name) == 0:
        cnnModel = cnn.fit(X_arrayYVelWPressure_negGeometry[:], Y_arrayYVelWPressure_negGeometry[:], validation_split=0.3, batch_size = 1, epochs = 5)
        # Serialize model to JSON
        model_json = cnn.to_json()
        weightsFile = name + '.h5'
        jsonFile = name + '.json'
        with open(jsonFile, 'w') as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        cnn.save_weights(weightsFile)
        print("Saved model to disk as {}.".format(weightsFile))

    y_predictYVel = cnn.predict(np.reshape(X_airfoilYVelWPressure_negGeometry, (1, 128, 256, 2)))
    print('X velocity of predicted array is {}'.format(y_predictYVel[:,:,:,1]))
       
    # Plot Y velocity
    tempName = name + 'Yvelocity'
    plotArray(y_predictYVel[0,:,:,1], tempName)
    
    plotLoss(cnnModel, "encoderDecoderYVelocityLoss")


    return y_predictYVel

# For trial purposes
y_predictXVelocity=encoderDecoderXVelocity()
y_predictYVelocity=encoderDecoderYVelocity()
#y_predict = cnn.predict(np.reshape(X_array3U[14],(1,128,256,3)))
