# Plot Practice
#

import matplotlib.pyplot as mpl
import numpy as np
from perceptron import Perceptron 

#points info

# (1) Generate points
X = np.arange(0, 20, 0.2)
# data

X_data = [(2,2),(2,4),(4,3),(6,8),(8,2),(8,10),(10,4),(10,10),(11,4),(12,2),(12,12),(16,12)]


# data "Y"
labels = [-1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1]

# (2) Plot points
X_data_yes = np.array([(2,4),(6,8),(8,10),(10,10),(12,12),(16,12)])

X_data_no = np.array([(2,2),(4,3),(8,2),(10,4),(11,4),(12,2)])

Y_data = [-1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, 1]

x_no, y_no = zip(*X_data_no)
x_yes, y_yes = zip(*X_data_yes)

mpl.scatter(x_no, y_no, c='r')
mpl.scatter(x_yes, y_yes, c='b')

# (3) Plot lines
# [ 0.34614926 -0.59964468  0.74115285]

#mpl.plot(X, 0.761912 + 0.663298*X, 'g')

perceptron = Perceptron() # creates instance of Perceptron class

print perceptron.traincycle(X_data, labels)


# (4) Display everything
mpl.show()
