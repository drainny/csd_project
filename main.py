from generator import generator, track, data
from fitting import fit
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


def isOk(traj, res, error=0.1):
    """Compare a result with a trajectory"""
    print(traj.kx, res.kx, traj.ky, res.ky)
    comp = [abs((traj.kx - res.kx)/traj.kx) < error, abs((traj.ky - res.ky)/traj.ky) < error]
    warnstr = ["kx ", "ky "]
    warn = ""
    for i in range(0, 2):
        if not comp[i]:
            warn += warnstr[i]
    if warn:
        print("Warning: " + warn + "out of range")


for i in range(0, 1):
    generator = generator(rsl=2.5e-7)
    traj = generator.generate()
    error = 1e-5
    data1 = traj.hitPoints()
    data1.write("test.txt")
    data2 = data(filename="test.txt")
    result1 = fit().linear_regression(data1)
    # Write the generated result to file, read form that file
    # and calculate again
    result2 = fit().linear_regression(data2)
    #isOk(traj, result1, error)
    #isOk(traj, result2, error)
    print(traj.r)
    print(traj.k)
    print(traj.phi)
    print(result1.r)
    print(result1.k)
    print(result1.phi)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    z = np.linspace(0, 1.4, 100)
    x = result1.r * (np.sin(result1.phi - result1.k * z) - np.sin(result1.phi))
    y = result1.r * (np.cos(result1.phi - result1.k * z) - np.cos(result1.phi))
    ax.plot3D(x, y, z)
    plt.show()
    plt.savefig("test.jpg")

