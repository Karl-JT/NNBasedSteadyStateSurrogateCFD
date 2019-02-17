# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:59:08 2019

@author: Nigel
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

def plotLoss(historyDict):
    # Plots training loss and validation loss
    lossValues = historyDict.history['loss']
    valLossValues = historyDict.history['val_loss']

    epochs = range(1, len(lossValues)+1)

    plt.plot(epochs, lossValues, 'bo', label='Training Loss')
    plt.plot(epochs, valLossValues, 'b', label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    saveAsPNG('Loss')
    plt.show()
    return

def checkSaveExist():
    # Checks if model.h5 file exists in directory
    listDir = os.listdir(os.getcwd())
    if "model.h5" in listDir:
        print("A saved model exists. Loading saved model...")
        return 1
    else:
        return 0

def loadWeights(model):
    # Load model weights from h5py file
    model.load_weights("model.h5")
    print("Weights are loaded from saved model.")
    return

def plotArray(array):
    # Takes in array and displays array as image with colourbar
    img = plt.imshow(array, interpolation='nearest')
    plt.colorbar(img, shrink = 0.62)
    plt.axis([0,256, 0, 128])
    plt.ylabel('Y')
    plt.xlabel('X')
    saveAsPNG('Contour')
    plt.show()
    return

def saveAsPNG(name):
    # Saves plot as PNG file
    os.chdir(os.getcwd()+'/plotImages')
    numImages = len(os.listdir(os.getcwd()))
    idx = numImages + 1
    plt.savefig(name+str(idx)+'.png')
    os.chdir('..')
    return