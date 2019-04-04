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
from keras.layers import Input, Reshape
from keras.models import Model

from excelToNumpy import X_array, Y_array, X_array3U, Y_array3U, X_array_negGeometry, Y_array_negGeometry, X_array3U_negGeometry, Y_array3U_negGeometry
#from excelToNumpy import X_arrayXVelWPressure_negGeometry, Y_arrayXVelWPressure_negGeometry, X_arrayYVelWPressure_negGeometry, Y_arrayYVelWPressure_negGeometry

from airfoilShapeExtractor import X_airfoil, Y_airfoil, X_airfoil3U, Y_airfoil3U, X_airfoil_negGeometry, Y_airfoil_negGeometry, X_airfoil3U_negGeometry, Y_airfoil3U_negGeometry
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
    
    #inputs = Input(shape=(128, 256, 1))
    
    #x1 = Conv2D(128, (8,16), padding='same', input_shape=(128, 256, 1), activation='relu')(inputs)
    #x2 = Conv2D(512, (4,4), padding='same', activation='relu')(x1)
    #x3 = Flatten()(x2)
    #x4 = Dense(512, activation='tanh')(x3)
    #x5 = Reshape((128, 256, 512))(x4)
    #x5 = np.reshape(x4, (128,256,512))
    #x6 = Conv2DTranspose(512, (8,8), padding='same', input_shape=(128, 256, 512), activation='relu')(x5)
    #x7 = Conv2DTranspose(256, (4,8), padding='same', activation='relu')(x6)
    #x8 = Conv2DTranspose(32, (2,2), padding='same', activation='relu')(x7)
    #x9 = Conv2DTranspose(1, (2,2), padding='same', activation='linear')(x8)
    
    #cnn = Model(inputs=inputs, outputs=x9)    
    
    cnn = Sequential()
    cnn.add(Conv2D(128, (8,16), strides= (8,16), input_shape=(128, 256, 1), activation='relu'))
    cnn.add(Conv2D(512, (4,4), strides= (4,4), activation='relu'))
    cnn.add(Flatten())
    cnn.add(Dense(1024, activation='tanh'))
    cnn.add(Reshape((1, 1, 1024), input_shape=(1024,)))
    cnn.add(Conv2DTranspose(512, (8,8), strides= (8,8), activation='relu'))
    cnn.add(Conv2DTranspose(256, (4,8), strides= (4,8), activation='relu'))
    cnn.add(Conv2DTranspose(32, (2,2), strides= (2,2), activation='relu'))
    cnn.add(Conv2DTranspose(1, (2,2), strides= (2,2), activation='linear'))

    #cnn.add(MaxPooling2D(pool_size=(2, 2))) 
    #cnn.add(Flatten())

    # Load weights
    if checkSaveExist(name) == 1:
        loadWeights(cnn, name)

    cnnModel = cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    #history = LossHistory()
    if checkSaveExist(name) == 0:
        len1 = len(X_array3U_negGeometry)
        input1 = np.reshape(X_array3U_negGeometry[:,:,:,0], (len1, 128, 256, 1))
        output1 = np.reshape(Y_array3U[:,:,:,0], (len1, 128, 256, 1))
        cnnModel = cnn.fit(input1, output1, validation_split=0.2, batch_size = 1, epochs = 100)
        # Serialize model to JSON
        model_json = cnn.to_json()
        weightsFile = name + '.h5'
        jsonFile = name + '.json'
        with open(jsonFile, 'w') as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        cnn.save_weights(weightsFile)
        print("Saved model to disk as {}.".format(weightsFile))

    y_predictXVel = cnn.predict(np.reshape(X_airfoil3U_negGeometry[0,:,:,0], (1, 128, 256, 1)))
    print('X velocity of predicted array is {}'.format(y_predictXVel[:,:,:,0]))
    
    # Plot X velocity
    tempName = name + 'Xvelocity'
    plotArray(y_predictXVel[0,:,:,0], tempName)
    
    print(cnn.summary())
    plotLoss(cnnModel, "encoderDecoderXVelocityLoss")
    
    return y_predictXVel

def encoderDecoderYVelocity():
    name = 'EncoderDecoderYVel'
    
    #inputs = Input(shape=(128, 256, 1))
    
    #x1 = Conv2D(128, (8,16), padding='same', input_shape=(128, 256, 1), activation='relu')(inputs)
    #x2 = Conv2D(512, (4,4), padding='same', activation='relu')(x1)
    #x3 = Flatten()(x2)
    #x4 = Dense(512, activation='tanh')(x3)
    #x5 = Reshape((128, 256, 512))(x4)
    #x5 = np.reshape(x4, (128,256,512))
    #x6 = Conv2DTranspose(512, (8,8), padding='same', input_shape=(128, 256, 512), activation='relu')(x5)
    #x7 = Conv2DTranspose(256, (4,8), padding='same', activation='relu')(x6)
    #x8 = Conv2DTranspose(32, (2,2), padding='same', activation='relu')(x7)
    #x9 = Conv2DTranspose(1, (2,2), padding='same', activation='linear')(x8)
    
    #cnn = Model(inputs=inputs, outputs=x9)
    
    cnn = Sequential()
    cnn.add(Conv2D(128, (8,16), strides= (8,16), input_shape=(128, 256, 1), activation='relu'))
    cnn.add(Conv2D(512, (4,4), strides= (4,4), activation='relu'))
    cnn.add(Flatten())
    cnn.add(Dense(1024, activation='tanh'))
    cnn.add(Reshape((1, 1, 1024), input_shape=(1024,)))
    cnn.add(Conv2DTranspose(512, (8,8), strides= (8,8), activation='relu'))
    cnn.add(Conv2DTranspose(256, (4,8), strides= (4,8), activation='relu'))
    cnn.add(Conv2DTranspose(32, (2,2), strides= (2,2), activation='relu'))
    cnn.add(Conv2DTranspose(1, (2,2), strides= (2,2), activation='linear'))

    #cnn.add(MaxPooling2D(pool_size=(2, 2))) 
    #cnn.add(Flatten())

    # Load weights
    if checkSaveExist(name) == 1:
        loadWeights(cnn, name)

    cnnModel = cnn.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    #history = LossHistory()
    if checkSaveExist(name) == 0:
        len2 = len(X_array3U_negGeometry)
        input2 = np.reshape(X_array3U_negGeometry[:,:,:,1], (len2, 128, 256, 1) )
        output2 = np.reshape(Y_array3U[:,:,:,1], (len2, 128, 256, 1))
        cnnModel = cnn.fit(input2, output2, validation_split=0.2, batch_size = 1, epochs = 100)
        # Serialize model to JSON
        model_json = cnn.to_json()
        weightsFile = name + '.h5'
        jsonFile = name + '.json'
        with open(jsonFile, 'w') as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        cnn.save_weights(weightsFile)
        print("Saved model to disk as {}.".format(weightsFile))

    y_predictYVel = cnn.predict(np.reshape(X_airfoil3U_negGeometry[0,:,:,1], (1, 128, 256, 1)))
    print('Y velocity of predicted array is {}'.format(y_predictYVel[:,:,:,0]))
       
    # Plot Y velocity
    tempName = name + 'Yvelocity'
    plotArray(y_predictYVel[0,:,:,0], tempName)
    
    plotLoss(cnnModel, "encoderDecoderYVelocityLoss")

    print(cnn.summary())
    return y_predictYVel

# For trial purposes
y_predictXVelocity=encoderDecoderXVelocity()
y_predictYVelocity=encoderDecoderYVelocity()
#y_predict = cnn.predict(np.reshape(X_array3U[14],(1,128,256,3)))
