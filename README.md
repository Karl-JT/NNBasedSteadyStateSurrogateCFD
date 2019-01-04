# NNBasedSteadyStateSurrogateCFD
ConvNN based Steady State Surrogate CFD solver

LinkedFolder contains the case files with the simulations completed and velocity and pressure values extracted.

The commands I used are below:

cd LinkedFolder
cd TestSetXX
blockMesh
checkMesh
icoFoam
postProcess -func sampleDict

The Master Files folder contains the python codes and the clean case files (I will change here, then copy over to the LinkedFolder to run the simulation)

FYP Master Files > Python Codes > models.py contains the model
