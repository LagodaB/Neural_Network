import numpy as np


X = np.array(([3,5], [5,1], [10,2]), dtype=float)
y = np.array(([75],[82], [93]), dtype=float)
X = X/np.amax(X,axis=0)
y = y/100 #max test score is 100

print X
print y

class Neural_Network(object):
    def __init__(self):
        #Define HyperParameters
        self.inputLayersSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

        
