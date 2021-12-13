import generator as gen
import pytest

@pytest.fixture
def trajectoryData():
    return gen.generate()

@pytest.fixture
def resultData(trajectoryData):
    return gen.Result(trajectoryData.kx, 1, trajectoryData.bx, 1, trajectoryData.ky, 1, trajectoryData.by, 1)

@pytest.mark.parametrize('execution_number', range(5))
def test_fitting(trajectoryData, resultData, execution_number):
    assert abs(trajectoryData.kx - resultData.kx) < resultData.ekx
    assert abs(trajectoryData.bx - resultData.bx) < resultData.ebx
    assert abs(trajectoryData.ky - resultData.ky) < resultData.eky
    assert abs(trajectoryData.by - resultData.by) < resultData.eby
