# Perceptron Algorithm Practice
#
# This shows that your previous implementation of the Perceptron algorithm works.
#
import numpy as np
import matplotlib.pyplot as mpl
from Perceptron import perceptron

X = np.arange(0,10,1)
mpl.axis([0, 10, 0, 10])

Y_3 = [1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

#data_ = np.transpose(data_l)

X_1 = np.concatenate((X, X))
X_2 = np.concatenate((2*X+1, 2*X-1))

#data_ = np.vstack((X_1, X_2))

#Y = perceptron(data_, Y_3, 1000)
#print(Y[0][0], Y[0][1], Y[1])

#mpl.plot(X, 2*X+1, 'r', 2*X-1, 'b'), (-1)*(Y[0][0])/Y[0][1]*X-(Y[1])/Y[0][1], 'g')
#mpl.show()

X_data = np.array([[0,4],[-5,0],[-6,1],[1,4],[4,5],[-3,2],[-2,5],[0,0],[1,0],[3,1],[5,2],[-1,-1],[-2,-3],[-5,-5]])
Y_data = np.array([1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1])

#print X_data.shape[0]
#print Y_data.shape[0]

#input format: X is a column
def linear_perceptron(X, Y, N):
    W = np.transpose([]*(X.shape[0]+1))
    print W
    X = np.transpose(np.concatenate(([1],X)))
    point_ct = X.shape[0]

    mispl_pts = 1

    while mispl_pts > 0:
        for t in range(0, point_ct):
            h = np.sign(W*X)
            if h < 1:
                mispl_pts += 1
                W = W + N*Y[t]*X[t]
            else:
                mispl_pts -= 1




linear_perceptron(X_data, Y_data, 0.2)
