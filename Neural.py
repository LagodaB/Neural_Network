import numpy as np
import matplotlib


X = np.array(([3,5], [5,1], [10,2]), dtype=float)
y = np.array(([75],[82], [93]), dtype=float)
X = X/np.amax(X,axis=0)
y = y/100 #max test score is 100

print X.shape
print y.shape

class Neural_Network(object):
    def __init__(self):
        #Define HyperParameters
        self.inputLayersSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3

def sigmoid(z):
        #Apply sigmoid activation function
    return 1/(1+np.exp(-z))
testInput = np.arange(-6,6,0.01)
plot(testInput, sigmoid(testInput), linewidth=2)
grid(1)
