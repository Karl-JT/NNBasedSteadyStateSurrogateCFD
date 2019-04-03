# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:56:50 2019

@author: Nigel
"""

# This file is for testing the implementation of new functions

import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image

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

testX = Y_airfoil3U[:,:,:,0]
testY = Y_airfoil3U[:,:,:,1]
plotArray(testX[0,:,:], 'testX')
plotArray(testY[0,:,:], 'testY')