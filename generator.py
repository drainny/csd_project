import random as r

class Generator:
    """A 3-dimensional line created by particle source

    Line is parametrized by  x = kx * z + bx; y = ky * z + by
    """
    def __init__(self, rsl):
        self.rsl = rsl
        self.kx, self.bx, self.ky, self.by = 0, 0, 0, 0
        self._x_n, self._y_n = 0, 0

    def generate(self):
        """Generate a random trajectory that at least hit one sensor"""
        self.kx = r.uniform(-0.5, 0.5)
        self.bx = r.uniform(-0.5, 0.5)
        self.ky = r.uniform(-0.5, 0.5)
        self.by = r.uniform(-0.5, 0.5)


    def hitPoints(self):
        """Calculate the hitpoints on sensors

        Returns a 5x2 array, for five hitpoints and each point has
        2 coordinates. If a sensor is not hitted, the corresponding
        row is None
        """
        # Generate
        self.generate()
        self._x_n = [self.kx * (i * 0.1 + 1) for i in range(5)]
        self._y_n = [self.ky * (i * 0.1 + 1) for i in range(5)]
        for i in range(5):
            if max(self._x_n[i], self._y_n[i])>0.5:
                self._x_n[i] = 0
                self._y_n[i] = 0

    def observe(self):
        """From the sensor side, calculate observed ranges of hit points. """

        self.hitPoints()

        # Determin the number
        _num_x_n = [self._x_n[i] // self.rsl for i in range(5)]
        _num_y_n = [self._y_n[i] // self.rsl for i in range(5)]

        # Max and min values of x and y
        x_n_max = [(_num_x_n[i] + 1) * self.rsl for i in range(5)]
        x_n_min = [(_num_x_n[i]) * self.rsl for i in range(5)]
        y_n_max = [(_num_y_n[i] + 1) * self.rsl for i in range(5)]
        y_n_min = [(_num_y_n[i]) * self.rsl for i in range(5)]

        return x_n_max, x_n_min, y_n_max, y_n_min







