import numpy as np
from generator import data
from generator import track
from scipy.optimize import minimize


class fit:
    """
    Linear regression with minimal sum of squared errors.
    """

#    def __init__(self, x_n=None, y_n=None, filename=None):
#        self.z_n = [(i * 0.1 + 1) for i in range(5)]
#        if filename:
#            f = open(filename, 'r')
#            line = f.readline()
#            line = line.replace('(', '')
#            line = line.replace(')', '')
#            line = line.replace(',', '')
#            numbers = line.split(' ')[:-1]
#            self.y_n = [None for i in range(5)]
#            self.x_n = [None for i in range(5)]
#            for i in range(0, 5):
#                self.x_n = [(int(float(numbers[2 * i]))
#                             + 0.5) * 2.5e-7 for i in range(0, 5)]
#                self.y_n = [(int(float(numbers[2 * i + 1]))
#                             + 0.5) * 2.5e-7 for i in range(0, 5)]
#            f.close()
#            return
#        self.x_n = [(x_n[i] + 0.5) * 2.5e-7 for i in range(5)]
#        self.y_n = [(y_n[i] + 0.5) * 2.5e-7 for i in range(5)]

    def linear_regression(self, dat):
        """Linear regression.
        """
        x_n = (dat.x_n + 0.5) * 2.5e-7
        y_n = (dat.y_n + 0.5) * 2.5e-7
        z_n = np.array([0.1 * i + 1 for i in range(len(x_n))])

        def error(x):
            err = 0
            err += np.sum((x[0] * (np.sin(x[2] - x[1] * z_n) - np.sin(x[2])) - x_n)**2)
            err += np.sum((x[0] * (np.cos(x[2] - x[1] * z_n) - np.cos(x[2])) - y_n)**2)
            return err
        r,k,phi = minimize(error, [0.5, 0.5, 0], bounds=((0.1, 0.2), (0.8, 2), (-np.pi, np.pi))).x


        #self.z_n = [(i * 0.1 + 1) for i in range(len(dat.x_n))]
        #A = np.vstack([self.z_n, np.ones(len(self.z_n))]).T
        #y = np.array(self.y_n)[:, np.newaxis]
        #x = np.array(self.x_n)[:, np.newaxis]
        #ky = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)[0][0]
        #kx = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), x)[0][0]
        return track(r,k,phi)
