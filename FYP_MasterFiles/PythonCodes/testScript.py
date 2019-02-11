# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 15:56:50 2019

@author: Nigel
"""

# This file is for testing the implementation of new functions

import matplotlib.pyplot as plt
import numpy as np


xx = plt.imshow(Y_array[0], interpolation='nearest')
plt.colorbar(xx, shrink = 0.62)
plt.axis([0,256, 0, 128])
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
