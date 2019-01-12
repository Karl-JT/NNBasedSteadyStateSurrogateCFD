# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:59:08 2019

@author: Nigel
"""

import matplotlib.pyplot as plt

def plotLoss(historyDict):
    lossValues = historyDict.history['loss']
    valLossValues = historyDict.history['val_loss']

    epochs = range(1, len(lossValues)+1)

    plt.plot(epochs, lossValues, 'bo', label='Training Loss')
    plt.plot(epochs, valLossValues, 'b', label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
    return

def checkSaveExist():
    import os
    listDir = os.listdir(os.getcwd())
    if "model.h5" in listDir:
        print("A saved model exists. Loading saved model...")
        return 1
    else:
        return 0

def loadWeights(model):
    model.load_weights("model.h5")
    return
