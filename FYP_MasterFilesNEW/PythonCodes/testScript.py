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

def plotArray(array):
    # Takes in array and displays array as image with colourbar
    img = plt.imshow(array, interpolation='nearest')
    plt.colorbar(img, shrink = 0.62)
    plt.axis([0,256, 0, 128])
    plt.ylabel('Y')
    plt.xlabel('X')
    saveAsJPG('Contour')
    plt.show()
    return

def saveAsJPG(name):
    # Saves plot as JPEG file
    os.chdir(os.getcwd()+'/plotImages')
    numImages = len(os.listdir(os.getcwd()))
    idx = numImages + 1
    plt.savefig(name+str(idx)+'.png')
    os.chdir('..')
    return

xx = Y_array[0]
plotArray(xx)
