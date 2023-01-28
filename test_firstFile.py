
import pytest

@pytest.fixture()
def setup():
    print("Perform some setup!!!")

    yield

    print("At Last!!!")

@pytest.fixture(scope ="class")
def mainSetup():
    print("Start with this!!!")
    yield
    print("End with this!!!")


def test_firstCase():
    print("FirstPrint")

@pytest.mark.usefixtures("mainSetup", "setup")
def test_secondCase(mainSetup,setup):
    print("SecondPrint")