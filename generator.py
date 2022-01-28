import random as r
import numpy as np


class data:
    def __init__(self, x_n=None, y_n=None, filename=None):
        if filename:
            f = open(filename, 'r')
            line = f.readline()
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace(',', '')
            numbers = line.split(' ')[:-1]
            self.x_n = np.array([])
            self.y_n = np.array([])
            for i in range(0, len(numbers) // 2):
                self.x_n = np.append(self.x_n, int(numbers[2 * i]))
                self.y_n = np.append(self.y_n, int(numbers[2 * i + 1]))
            f.close()
            return
        self.x_n = x_n
        self.y_n = y_n

    def write(self, filename):
        f = open(filename, 'a')
        writestring = ''
        for i in range(0, len(self.x_n)):
            writestring += ('('
                            + str(self.x_n[i])
                            + ", "
                            + str(self.y_n[i])
                            + ") ")
        f.write(writestring)
        f.close()


class track:

    def __init__(self, kx, bx, ky, by):
        self.kx = kx
        self.bx = bx
        self.ky = ky
        self.by = by

    def hitPoints(self):
        """Calculate the hitpoints on sensors

        Returns a 5x2 array, for five hitpoints and each point has
        2 coordinates. If a sensor is not hitted, the corresponding
        row is None
        """
        x_n = np.array([], int)
        y_n = np.array([], int)
        for i in range(5):
            x = self.kx * (i * 0.1 + 1)
            y = self.ky * (i * 0.1 + 1)
            if max(abs(x), abs(y)) > 0.5:
                break
            x_n = np.append(x_n, int(x // 2.5e-7))
            y_n = np.append(y_n, int(y // 2.5e-7))
        return data(x_n, y_n)


class track:

    def __init__(self, r, k, phi):
        self.r = r
        self.k = k
        self.phi = phi

    def hitPoints(self):
        """Calculate the hitpoints on sensors

        Returns a 5x2 array, for five hitpoints and each point has
        2 coordinates. If a sensor is not hitted, the corresponding
        row is None
        """
        x_n = np.array([], int)
        y_n = np.array([], int)
        for i in range(5):
            x = self.r * (np.sin(self.phi - self.k * (0.1 * i + 1))
                          - np.sin(self.phi))
            y = self.r * (np.cos(self.phi - self.k * (0.1 * i + 1))
                          - np.cos(self.phi))
            if max(abs(x), abs(y)) > 0.5:
                break
            x_n = np.append(x_n, int(x // 2.5e-7))
            y_n = np.append(y_n, int(y // 2.5e-7))
        return data(x_n, y_n)


class generator:
    """A 3-dimensional line created by particle source

    Line is parametrized by  x = kx * z + bx; y = ky * z + by
    """

    def __init__(self, rsl):
        self.rsl = rsl
        self.kx, self.bx, self.ky, self.by = 0, 0, 0, 0

    def generate(self):
        """Generate a random trajectory that at least hit one sensor"""
        return track(r.uniform(-0.5, 0.5),
                     r.uniform(-0.5, 0.5),
                     r.uniform(-0.5, 0.5),
                     r.uniform(-0.5, 0.5))

    def generate(self):
        """Generate a random trajectory that at least hit one sensor"""
        return track(r.uniform(0.1, 0.2),
                     r.uniform(0.8, 2),
                     r.uniform(-np.pi, np.pi))

#    def observe(self):
#        """From the sensor side, calculate observed ranges of hit points. """
#
#        self.hitPoints()
#
#        # Determin the number
#        self._num_x_n = [self._x_n[i] // self.rsl for i in range(5)]
#        self._num_y_n = [self._y_n[i] // self.rsl for i in range(5)]
#
#        # Max and min values of x and y
#        x_n_max = [(self._num_x_n[i] + 1) * self.rsl for i in range(5)]
#        x_n_min = [(self._num_x_n[i]) * self.rsl for i in range(5)]
#        y_n_max = [(self._num_y_n[i] + 1) * self.rsl for i in range(5)]
#        y_n_min = [(self._num_y_n[i]) * self.rsl for i in range(5)]
#
#        return x_n_max, x_n_min, y_n_max, y_n_min
