import random
import math
import numpy as np

class fit:
    """
    Linear regression with minimal sum of squared errors.
    """
    def __init__(self, x_n_max=None, x_n_min=None, y_n_max=None, y_n_min=None, filename=None):
        if filename:
            f = open(filename, 'r')
            line = f.readline()
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace(',', '')
            numbers = line.split(' ')[:-1]
            self.y_n_max = [None for i in range(5)]
            self.y_n_min = [None for i in range(5)]
            self.x_n_max = [None for i in range(5)]
            self.x_n_min = [None for i in range(5)]
            for i in range(0, 5):
                num_x_n = int(float(numbers[2*i]))
                num_y_n = int(float(numbers[2*i+1]))
                self.x_n_max[i] = (num_x_n + 1) * 2.5e-7
                self.x_n_min[i] = num_x_n * 2.5e-7
                self.y_n_max[i] = (num_y_n + 1) * 2.5e-7
                self.y_n_min[i] = num_y_n * 2.5e-7
            f.close()
            return
        self.y_n_max = y_n_max
        self.y_n_min = y_n_min
        self.x_n_max = x_n_max
        self.x_n_min = x_n_min
        self.kx, self.ky = 0, 0
        self.x_n, self.y_n, self.z_n = 0, 0, 0

    def compute_observed(self):
        """
        First compute observed x, y and z
        """
        self.y_n = [(self.y_n_max[i]+self.y_n_min[i])/2 for i in range(5)]
        self.x_n = [(self.x_n_max[i]+self.x_n_min[i])/2 for i in range(5)]
        self.z_n = [(i*0.1+1) for i in range(5)]

    def linear_regression(self):
        """
        Linear regression.
        """

        A = np.vstack([self.z_n, np.ones(len(self.z_n))]).T
        y = np.array(self.y_n)[:, np.newaxis]
        x = np.array(self.x_n)[:, np.newaxis]
        self.ky = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)[0][0]
        self.kx = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), x)[0][0]

