import pytest


@pytest.mark.sanity
@pytest.fixture(autouse=True)
def testsetUp():
    print("Launch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("Log Off")
    print("Close Browser")
