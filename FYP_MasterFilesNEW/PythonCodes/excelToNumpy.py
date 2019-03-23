import os
import numpy as np
import pandas as pd

os.chdir('..')
os.chdir('..')
wdir = os.chdir(os.getcwd()+'/LinkedFolderNEW')


trainingCases = os.listdir(os.getcwd())
trainingCasesListLen = len(trainingCases)

#X_array = np.zeros((trainingCasesListLen, 128, 256))
Y_array = np.zeros((trainingCasesListLen, 128, 256))
#X_array3U = np.zeros((trainingCasesListLen, 128, 256, 3))
#Y_array3U = np.zeros((trainingCasesListLen, 128, 256, 3))

X_arrayXVelWPressure = np.zeros((trainingCasesListLen, 128, 256, 2))
Y_arrayXVelWPressure = np.zeros((trainingCasesListLen, 128, 256, 2))
X_arrayYVelWPressure = np.zeros((trainingCasesListLen, 128, 256, 2))
Y_arrayYVelWPressure = np.zeros((trainingCasesListLen, 128, 256, 2))

for count in range(trainingCasesListLen):
    # Open final iteration to get output array
    os.chdir(os.getcwd()+'/'+trainingCases[count]+'/postProcessing/sampleDict/500')
    print(os.getcwd())
    rawData = pd.read_csv('data_U.csv')

    for x in range(len(rawData)):
        tempLine = rawData.iloc[x]
        #Y_array3U[count, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3],tempLine[4],tempLine[5])
        Y_array[count, int(tempLine[1]*10),int(tempLine[0]*10)] = tempLine[3]
        Y_arrayXVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3], 0)
        Y_arrayYVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[4], 0)
    
    rawData = pd.read_csv('data_p.csv')
    for x in range(len(rawData)):
        tempLine = rawData.iloc[x]
        Y_arrayXVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
        Y_arrayYVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
        
    # Open first iteration to get input array
    os.chdir('..')
    os.chdir(os.getcwd()+'/0')
    rawData2 = pd.read_csv('data_U.csv')
    
    for x in range(len(rawData2)):
        tempLine = rawData2.iloc[x]
        #X_array3U[count, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3],tempLine[4],tempLine[5])
        #X_array[count, int(tempLine[1]*10),int(tempLine[0]*10)] = tempLine[3]    
        X_arrayXVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3], 0)
        X_arrayYVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[4], 0)

    rawData = pd.read_csv('data_p.csv')
    for x in range(len(rawData)):
        tempLine = rawData.iloc[x]
        X_arrayXVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
        X_arrayYVelWPressure[count, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
        
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')


# Create new Y_array and X_array with geometry area as -1
#X_array_negGeometry = X_array
Y_array_negGeometry = Y_array
#X_array3U_negGeometry = X_array3U
#Y_array3U_negGeometry = Y_array3U
X_arrayXVelWPressure_negGeometry = X_arrayXVelWPressure
X_arrayYVelWPressure_negGeometry = X_arrayYVelWPressure
Y_arrayXVelWPressure_negGeometry = Y_arrayXVelWPressure
Y_arrayYVelWPressure_negGeometry = Y_arrayYVelWPressure

for count in range(len(Y_array)):
    for x in range(256):
        for y in range(128):
            if Y_array[count, y, x] == 0:
                #Y_array_negGeometry[count, y, x] = -1
                #X_array_negGeometry[count, y, x] = -1
                #Y_array3U_negGeometry[count, y, x] = (-1, -1, -1)
                #X_array3U_negGeometry[count, y, x] = (-1, -1, -1)
                X_arrayXVelWPressure_negGeometry[count, y, x] = (-1, -1)
                X_arrayYVelWPressure_negGeometry[count, y, x] = (-1, -1)
                Y_arrayXVelWPressure_negGeometry[count, y, x] = (-1, -1)
                Y_arrayYVelWPressure_negGeometry[count, y, x] = (-1, -1)

# Reset to Python Codes directory
os.chdir('..')
os.chdir(os.getcwd()+'/FYP_MasterFilesNEW/PythonCodes')
