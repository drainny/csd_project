import random as r

class Trajectory:
    """A 3-dimensional line created by particle source

    Line is parametrized by  x = kx * z + bx; y = ky * z + by
    """
    def __init__(self, xSlope, xIntercept, ySlope, yIntercept):
        self.kx, self.bx = xSlope, xIntercept
        self.ky, self.by = ySlope, yIntercept

    def hitPoints(self):
        """Calculate the hitpoints on sensors

        Returns a 5x2 array, for five hitpoints and each point has
        2 coordinates. If a sensor is not hit, the corresponding
        row is None
        """
        points = []
        for i in range(0, 4):
            x = self.kx * (1 + 0.1 * i) + self.bx
            y = self.ky * (1 + 0.1 * i) + self.by
            nx = x // 0.000025
            ny = y // 0.000025
            points[i] = [nx, ny] if max(abs(x), abs(y)) < 0.5 else None
        return points

def generate():
    """Generate a random trajectory that at least hit one sensor"""
    kx = r.uniform(-1, 1)
    bx = r.uniform(-0.5, 0.5)
    ky = r.uniform(-1, 1)
    by = r.uniform(-0.5, 0.5)
    # Only return when t.points[0] is not None
    while True:
        t = Trajectory(kx, bx, ky, by)
        if t.points[0] return t
