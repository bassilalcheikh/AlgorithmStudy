# "Perceptron Algorithm" by Bassil Alcheikh, 08/31/16

# INPUT:
#       * data_matrix: data to learn from
#       * Y: rules that correlate to the data, either -1 (for false) or 1 (for true)
#       * iter_ : the number of desired iterations
#
# OUTPUT:
#       * a series of weights/coefficients to be used in a polynomial
#
# Note: data going into the algorithm should be the transpose of a standard matrix
# You might want to fix this when the algo is finished
#

import numpy # numpy is already installed; use it!

data_m = numpy.array([[2.7810836,2.550537003],
	[1.465489372,2.362125076],
	[3.396561688,4.400293529],
	[1.38807019,1.850220317],
	[3.06407232,3.005305973],
	[7.627531214,2.759262235],
	[5.332441248,2.088626775],
	[6.922596716,1.77106367],
	[8.675418651,-0.242068655],
	[7.673756466,3.508563011]])

data_n = numpy.array([[1,3],[2,5],[3,7],[4,9],[5,11],[6,13],[7,15],[8,17],[9,19],[10,21]])

data_l = numpy.array([[1,3],[2,5],[3,7],[4,9],[5,11],[6,13],[7,15],[8,17],[9,19],[10,21],[1,1],[2,3],[3,5],[4,7],[5,9],[6,11],[7,13],[8,15],[9,17],[10,19]])

Y_1 = [-1,-1,-1,-1,-1,1,1,1,1,1]
Y_2 = [1,1,1,1,1,1,1,1,1,1]
Y_3 = [1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]


iter_ = 1000

data_ = numpy.transpose(data_l)
def perceptron(data_matrix, Y, iter_):
    a = 0 # threshold
    b = 0 # bias
    d = data_matrix.shape[0] # dimension (number of rows)
    N = data_matrix.shape[1] # points quantity (number of columns)

    W = numpy.array([0,0]) # weights, initialized to 0

    for j in range(0, iter_):
        k = j%N # IMPORTANT STEP
        a = sum(data_matrix[:,k]*numpy.transpose(W))+b   # <--- convert to Python

        if a*Y[k] <= 0: # test for miscl.
            for i in range(0,d):
                W[i]=W[i]+Y[k]*data_matrix[i][k]
            b += Y[k]

    return (W,b)

#print(perceptron(data_, Y_, iter_))
#print(perceptron(data_, Y_2, iter_))
#print(perceptron(data_, Y_3, iter_))


"""
    function [W,b]=Perceptron(data,Y,iter)

        d = size(data,1); // dimension (number of rows)
        N = size(data,2); // points quantity (number of columns)
        W = zeros(1,d); //weights, initialized to 0
        b = 1; //bias
        a=1; //threshold

        for j=1:iter
            k=modulo(j,N); //THIS IS THE JEWEL
            a = sum(data(:,k+1).*W')+b;
            if a*Y(k+1) <= 0  then // test for miscl.
                for i =1:d
                    W(i)=W(i)+Y(k+1)*data(i,k+1);
                end
                b=b+Y(k+1);
            end
        end
    endfunction
"""
