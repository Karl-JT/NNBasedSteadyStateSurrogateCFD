import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

def plotLoss(historyDict, name):
    # Plots training loss and validation loss
    lossValues = historyDict.history['loss']
    valLossValues = historyDict.history['val_loss']

    epochs = range(1, len(lossValues)+1)

    plt.plot(epochs, lossValues, 'bo', label='Training Loss')
    plt.plot(epochs, valLossValues, 'b', label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    imageName = name + 'Loss'
    saveAsPNG(imageName)
    plt.show()
    return

def checkSaveExist(name):
    # Checks if model.h5 file exists in directory
    listDir = os.listdir(os.getcwd())
    weightsFile = name + '.h5'
    if weightsFile in listDir:
        print('A saved model {} exists. Loading saved model...'.format(weightsFile))
        return 1
    else:
        return 0

def loadWeights(model, name):
    # Load model weights from h5py file
    weightsFile = name + '.h5'
    model.load_weights(weightsFile)
    print('Weights are loaded from saved model {}.'.format(weightsFile))
    return

def plotArray(array, name):
    # Takes in array and displays array as image with colourbar
    img = plt.imshow(array, interpolation='nearest')
    plt.colorbar(img, shrink = 0.62)
    plt.axis([0,256, 0, 128])
    plt.ylabel('Y')
    plt.xlabel('X')
    imageName = name + 'Contour'
    saveAsPNG(imageName)
    plt.show()
    return

def saveAsPNG(name):
    # Saves plot as PNG file
    numImages = len(os.listdir(os.getcwd()))
    idx = numImages + 1
    plt.savefig(name+str(idx)+'.png')
    return