# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 04:00:25 2018

@author: Nigel
"""

import os
import numpy as np
import pandas as pd

os.chdir('..')
os.chdir('..')
wdir = os.chdir(os.getcwd()+'/LinkedFolder')


trainingCases = os.listdir(os.getcwd())
trainingCasesListLen = len(trainingCases)

X_array = np.zeros((trainingCasesListLen, 128, 256))
Y_array = np.zeros((trainingCasesListLen, 128, 256))
X_array3U = np.zeros((trainingCasesListLen, 128, 256, 3))
Y_array3U = np.zeros((trainingCasesListLen, 128, 256, 3))

for count in range(trainingCasesListLen):
    # Open final iteration to get output array
    os.chdir(os.getcwd()+'/'+trainingCases[count]+'/postProcessing/sampleDict/15')
    print(os.getcwd())
    rawData = pd.read_csv('data_U.csv')

    for x in range(len(rawData)):
        tempLine = rawData.iloc[x]
        Y_array3U[count, int(tempLine[1]),int(tempLine[0])] = (tempLine[3],tempLine[4],tempLine[5])
        Y_array[count, int(tempLine[1]*10),int(tempLine[0]*10)] = tempLine[3]
        
    # Open first iteration to get input array
    os.chdir('..')
    os.chdir(os.getcwd()+'/0')
    rawData2 = pd.read_csv('data_U.csv')
    
    for x in range(len(rawData2)):
        tempLine = rawData2.iloc[x]
        X_array3U[count, int(tempLine[1]),int(tempLine[0])] = (tempLine[3],tempLine[4],tempLine[5])
        X_array[count, int(tempLine[1]*10),int(tempLine[0]*10)] = tempLine[3]    
    
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')


# Create new Y_array and X_array with geometry area as -1
X_array_negGeometry = X_array
Y_array_negGeometry = Y_array
X_array3U_negGeometry = X_array3U
Y_array3U_negGeometry = Y_array3U
for count in range(len(Y_array)):
    for x in range(201):
        for y in range(101):
            if Y_array[count, y, x] == 0:
                Y_array_negGeometry[count, y, x] = -1
                X_array_negGeometry[count, y, x] = -1
                Y_array3U_negGeometry[count, y, x] = (-1, -1, -1)
                X_array3U_negGeometry[count, y, x] = (-1, -1, -1)

# Reset to Python Codes directory
os.chdir('..')
os.chdir(os.getcwd()+'/FYP_MasterFiles/PythonCodes')
