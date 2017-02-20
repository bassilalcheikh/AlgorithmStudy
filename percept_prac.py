# Perceptron Algorithm Practice
#
# This shows that your previous implementation of the Perceptron algorithm works.
#
import numpy as np
import matplotlib.pyplot as mpl

#X_data = np.array([[2.7810836,2.550537003], [1.465489372,2.362125076], [3.396561688,4.400293529], [1.38807019,1.850220317], [3.06407232,3.005305973], [7.627531214,2.759262235], [5.332441248,2.088626775], [6.922596716,1.77106367], [8.675418651,-0.242068655], [7.673756466,3.508563011]])
#X_data = np.array([[0,4],[-5,0],[-6,1],[1,4],[4,5],[-3,2],[-2,5],[0,0],[1,0],[3,1],[5,2],[-1,-1],[-2,-3],[-5,-5]])
#X_data = np.array([[1,1],[2,-2],[-1,-1.5],[-2,1],[1.5,-0.5]])
#Y_data = [-1,-1,-1,-1,-1,1,1,1,1,1]
#Y_data = [1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1]
#Y_data = [1,-1,-1,1,1]
x, y = zip(*X_data)

def linear_form2(weights):
    # input: weights a,b,c such that a+bx+cy = 0
    # returns coefficients a,b such that y = ax+b
    a = float(-weights[1])/weights[2]
    b = float(-weights[0])/weights[2]
    return [a,b]

#input format: X is a column
def linear_perceptron(X, Y, r): # inputs: X = learning points, Y = binary values, r = learning rate
    d = X.shape[1] #dimensions
    N = X.shape[0] # number of points
    W = np.transpose(np.insert(([0.5]*d),d,1)) # weights
    X = np.insert(X, 0, 1, axis=1) # insert '1' into x_0
    sign = lambda x: 1 if x>0  else -1
    correct_guesses = 0
    while correct_guesses < N:
        for t in range(0,N):
            h = sign(np.dot(W, X[t]))
            if h != Y[t]:
                W = W + r*np.dot(Y[t],X[t])
            else:
                correct_guesses += 1
    return W

#w_ = linear_perceptron(X_data, Y_data, 0.1)

#print(linear_form2(w_))
