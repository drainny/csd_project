import random
import math
import numpy as np

class fit:
    """
    Linear regression with minimal sum of squared errors.
    """
    def __init__(self, y_n_max, y_n_min, x_n_max, x_n_min):
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
        self.k_y = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), y)[0]
        self.k_x = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), x)[0]

