import os
import numpy as np
import pandas as pd

wdir = os.chdir(os.getcwd()+'/AirfoilShape')



#X_airfoil = np.zeros((1, 128, 256))
Y_airfoil = np.zeros((1, 128, 256))
#X_airfoil3U = np.zeros((1, 128, 256, 3))
#Y_airfoil3U = np.zeros((1, 128, 256, 3))

X_airfoilXVelWPressure = np.zeros((1, 128, 256, 2))
Y_airfoilXVelWPressure = np.zeros((1, 128, 256, 2))
X_airfoilYVelWPressure = np.zeros((1, 128, 256, 2))
Y_airfoilYVelWPressure = np.zeros((1, 128, 256, 2))

# Open final iteration to get output array
os.chdir(os.getcwd()+'/postProcessing/sampleDict/500')
print(os.getcwd())
rawData = pd.read_csv('data_U.csv')

for x in range(len(rawData)):
    tempLine = rawData.iloc[x]
    #Y_airfoil3U[0, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3],tempLine[4],tempLine[5])
    Y_airfoil[0, int(tempLine[1]*10),int(tempLine[0]*10)] = tempLine[3]
    Y_airfoilXVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3], 0)
    Y_airfoilYVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[4], 0)
    
rawData = pd.read_csv('data_p.csv')
for x in range(len(rawData)):
    tempLine = rawData.iloc[x]
    Y_airfoilXVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
    Y_airfoilYVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
        
# Open first iteration to get input array
os.chdir('..')
os.chdir(os.getcwd()+'/0')
rawData2 = pd.read_csv('data_U.csv')
    
for x in range(len(rawData2)):
    tempLine = rawData2.iloc[x]
    #X_airfoil3U[0, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3],tempLine[4],tempLine[5])
    #X_airfoil[0, int(tempLine[1]*10),int(tempLine[0]*10)] = tempLine[3]    
    X_airfoilXVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[3], 0)
    X_airfoilYVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10)] = (tempLine[4], 0)

rawData = pd.read_csv('data_p.csv')
for x in range(len(rawData)):
    tempLine = rawData.iloc[x]
    X_airfoilXVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
    X_airfoilYVelWPressure[0, int(tempLine[1]*10),int(tempLine[0]*10),1] = (tempLine[3])
    
os.chdir('..')
os.chdir('..')
os.chdir('..')
os.chdir('..')


# Create new Y_array and X_array with geometry area as -1
#X_airfoil_negGeometry = X_airfoil
#Y_airfoil_negGeometry = Y_airfoil
#X_airfoil3U_negGeometry = X_airfoil3U
#Y_airfoil3U_negGeometry = Y_airfoil3U
X_airfoilXVelWPressure_negGeometry = X_airfoilXVelWPressure
X_airfoilYVelWPressure_negGeometry = X_airfoilYVelWPressure
Y_airfoilXVelWPressure_negGeometry = Y_airfoilXVelWPressure
Y_airfoilYVelWPressure_negGeometry = Y_airfoilYVelWPressure

for count in range(len(Y_airfoil)):
    for x in range(256):
        for y in range(128):
            if Y_airfoil[count, y, x] == 0:
                #Y_airfoil_negGeometry[count, y, x] = -1
                #X_airfoil_negGeometry[count, y, x] = -1
                #Y_airfoil3U_negGeometry[count, y, x] = (-1, -1, -1)
                #X_airfoil3U_negGeometry[count, y, x] = (-1, -1, -1)
                X_airfoilXVelWPressure_negGeometry[count, y, x] = (-1, -1)
                X_airfoilYVelWPressure_negGeometry[count, y, x] = (-1, -1)
                Y_airfoilXVelWPressure_negGeometry[count, y, x] = (-1, -1)
                Y_airfoilYVelWPressure_negGeometry[count, y, x] = (-1, -1)


