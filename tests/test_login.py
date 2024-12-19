import pytest

# @pytest.mark.sanity
# @pytest.fixture
# def testsetUp():
#     print("Launch Browser")
#     print("Login")
#     print("Browse Products")
#     yield
#     print("Log Off")
#     print("Close Browser")


def testAddItemToCart(testsetUp):
    print("Add Item Sucessful")


# @pytest.mark.regression
def testRemoveItemFromCart(testsetUp):
    print("Remove Item Sucessful")


# @pytest.mark.sanity
def testCalculation():
    assert 2 + 2 == 4
