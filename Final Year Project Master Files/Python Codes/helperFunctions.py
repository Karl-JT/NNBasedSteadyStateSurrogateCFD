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
