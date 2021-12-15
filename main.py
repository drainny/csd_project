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
        return False
    return True


for i in range(0, 1):
    generator = Generator(rsl = 2.5e-7)
    x_n_max, x_n_min, y_n_max, y_n_min = generator.observe()
    print(generator.kx, generator.ky)
    error = 1e-1
    calculate = fit(x_n_max, x_n_min, y_n_max, y_n_min)
    calculate.compute_observed()
    calculate.linear_regression()
    isOk(generator, calculate, error)

