# Plot Practice
#
#
#
import matplotlib.pyplot as mpl
import numpy as np

#points info

# (1) Generate points
X = np.arange(-7, 7, 0.2)

# (2) Plot points
#X_data_no = np.array([[2.7810836,2.550537003], [1.465489372,2.362125076], [3.396561688,4.400293529], [1.38807019,1.850220317], [3.06407232,3.005305973]])
#X_data_yes = np.array([[7.627531214,2.759262235], [5.332441248,2.088626775], [6.922596716,1.77106367], [8.675418651,-0.242068655], [7.673756466,3.508563011]])
#X_data_no = np.array([[0,0],[1,0],[3,1],[5,2],[-1,-1],[-2,-3],[-5,-5]])
#X_data_yes = np.array([[0,4],[-5,0],[-6,1],[1,4],[4,5],[-3,2],[-2,5]])
X_data_yes = np.array([[1,1],[-2,1],[1.5,-0.5]])
X_data_no = np.array([[2,-2],[-1,-1.5]])

#Y_data = [-1,-1,-1,-1,-1,1,1,1,1,1]
#Y_data = [1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1]
Y_data = [1,-1,-1,1,1]

x_no, y_no = zip(*X_data_no)
x_yes, y_yes = zip(*X_data_yes)

mpl.scatter(x_no,y_no,c='r')
mpl.scatter(x_yes,y_yes,c='b')

# (3) Plot lines
mpl.plot(X, -0.500000*X-0.50000, 'g')

# (4) Display everything
mpl.show()
