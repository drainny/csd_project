from generator import Generator
from fitting import fit

def isOk(traj, res, error = 0.1):
    """Compare a result with a trajectory"""
    print(traj.kx, res.kx, traj.ky, res.ky)
    comp = [abs((traj.kx - res.kx)/traj.kx) < error, abs((traj.ky - res.ky)/traj.ky) < error]
    warnstr = ["kx ", "ky "]
    warn = ""
    for i in range(0,2):
        if not comp[i]:
            warn += warnstr[i]
    if warn:
        print("Warning: " + warn + "out of range")


for i in range(0, 1):
    generator = Generator(rsl = 2.5e-7)
    x_n_max, x_n_min, y_n_max, y_n_min = generator.observe()
    error = 1e-5
    cal1 = fit(x_n_max, x_n_min, y_n_max, y_n_min)
    cal1.compute_observed()
    cal1.linear_regression()
    # Write the generated result to file, read form that file
    # and calculate again
    generator.write("test.txt")
    cal2 = fit(filename="test.txt")
    cal2.compute_observed()
    cal2.linear_regression()
    isOk(generator, cal1, error)
    isOk(generator, cal2, error)

