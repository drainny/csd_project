import generator as gen
import main

def isOk(traj, res):
    """Compare a result with a trajectory"""
    comp = [abs(traj.kx - res.kx) < res.kxe, abs(traj.bx - res.bx) < res.bxe, abs(traj.ky - res.ky) < res.kye, abs(traj.by - res.by) < res.bye]
    warnstr = ["kx ", "bx ", "ky ", "by "]
    warn = ""
    for i in range(0,3):
        if not comp[i]:
            warn += warnstr[i]
    if warn:
        print("Warning: " + warn + "out of range")

for i in range(0, 1000):
    t = gen.generate()
    res = main.calculate(t.hitPoints())
    isOk(t, res)

