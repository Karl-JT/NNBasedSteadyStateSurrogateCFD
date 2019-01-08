# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 02:24:55 2018

@author: Nigel
"""

import numpy as np
import pandas as pd
import os

path = 'C:\\Users\\Nigel\\Documents\\NTUFYP2019\\LinkedFolder\\TrainingData\\X_input'
os.chdir(path)
print(os.getcwd())
dirList = os.listdir(os.getcwd())


dirListLen = len(dirList)
X_array = np.zeros((dirListLen, 101, 201))


for count in range(dirListLen):
    
    rawData = pd.read_csv(dirList[count])
    #print(rawData)
    rawData.columns = ['UX', 'UY', 'UZ', 'P', 'X', 'Y', 'Z']
    
    z0_data = rawData[rawData.Z == 0]
    
    #emptyArray = np.zeros((101,201,2))
    
    for x in range(len(z0_data)):
        tempLine = z0_data.iloc[x]
        if ((tempLine[4]*100)%100==0) and ((tempLine[5]*10)%10==0):
            X_array[count, int(tempLine[5]),int(tempLine[4])] = tempLine[0]

path2 = 'C:\\Users\\Nigel\\Documents\\NTUFYP2019\\LinkedFolder\\TrainingData\\Y_output'
os.chdir(path2)
print(os.getcwd())
dirList2 = os.listdir(os.getcwd())


dirListLen2 = len(dirList2)
Y_array = np.zeros((dirListLen2, 101, 201))


for count in range(dirListLen2):
    
    rawData2 = pd.read_csv(dirList2[count])
    #print(rawData2)
    rawData2.columns = ['UX', 'UY', 'UZ', 'P', 'X', 'Y', 'Z']
    
    z0_data2 = rawData2[rawData2.Z == 0]
    
    
    for x in range(len(z0_data2)):
        tempLine2 = z0_data2.iloc[x]
        if ((tempLine2[4]*100)%100==0) and ((tempLine2[5]*10)%10==0):
            Y_array[count, int(tempLine2[5]),int(tempLine2[4])] = tempLine2[0]





