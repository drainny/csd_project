import generator as gen
import fitting as f
import main as m
import pytest

# Test if general fitting results lie in an approvable range
@pytest.fixture
def trajectoryData():
    traj = gen.Generator(2.5e-7)
    traj.generate()
    return traj

@pytest.fixture
def resultData(trajectoryData):
    x_n_max, x_n_min, y_n_max, y_n_min = trajectoryData.observe()
    cal = f.fit(x_n_max, x_n_min, y_n_max, y_n_min)
    cal.compute_observed()
    cal.linear_regression()
    return cal

@pytest.mark.parametrize('execution_number', range(100))
def test_fitting(trajectoryData, resultData, execution_number):
    assert m.isOk(trajectoryData, resultData, 1e-1)

# Test some special trajectories
# For example, a line of zero slopes
# @pytest.fixture
# def traj_zero_slope():
#     traj = gen.Generator(2.5e-7)
#     traj.kx = 0
#     traj.ky = 0
#  
# @pytest.fixture
# def result_zero_slope(traj_zero_slope):
#     x_n_max, x_n_min, y_n_max, y_n_min = traj_zero_slope.observe()
#     cal = f.fit(x_n_max, x_n_min, y_n_max, y_n_min)
#     cal.compute_observed()
#     cal.linear_regression()
#     return cal
# 
#def test_zero_slope(traj_zero_slope, result_zero_slope):
#    assert m.isOk(traj_zero_slope, result_zero_slope)
# 
# @pytest.fixture
# def traj_err_slope():
#     traj = gen.Generator(2.5e-7)
#     traj.kx = 0.1415785793306974
#     traj.ky = 0.4965192218296801
#  
# @pytest.fixture
# def result_err_slope(traj_err_slope):
#     x_n_max, x_n_min, y_n_max, y_n_min = traj_err_slope.observe()
#     cal = f.fit(x_n_max, x_n_min, y_n_max, y_n_min)
#     cal.compute_observed()
#     cal.linear_regression()
#     return cal
# 
# def test_fitting(traj_err_slope, result_err_slope):
#     assert m.isOk(traj_err_slope, result_err_slope, 1e-1)
