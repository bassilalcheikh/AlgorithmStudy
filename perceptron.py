# Perceptron Algorithm
#
# Bassil Alcheikh, 2018
#
import numpy as np 

class Perceptron(object): 

    def __init__(self, learning_rate = 0.05):
        self.eta = learning_rate

    def activation(self, weights, point_data):
        #we "adjust the point" to include the "1" term for the w_0/"bias" term
        adj_point = (1,)+point_data
        val = np.dot(weights, adj_point)
        return (-1)**(int(val >= 0)+1)

    def traincycle(self, data, labels):
        weights = list(np.random.rand( len(data[0]) +1)) # initial weights also include w_0/"bias"
        successes = 0
        data_ct = len(data)
        while successes < data_ct:
            successes = 0
            for point in xrange(0, data_ct):
                phi = self.activation(weights, data[point])
                if phi == labels[point]:
                    successes += 1
                else:
                    weights = np.add(weights, np.dot(self.eta*(labels[point]-phi), (1,)+data[point]))
        return weights

'''
if __name__ == '__main__':
    xdata = input("enter x data: ")
    ylabels =  input("enter y data: ")
    p = Perceptron()
    print p.traincycle(xdata, ylabels)
'''


    
        
