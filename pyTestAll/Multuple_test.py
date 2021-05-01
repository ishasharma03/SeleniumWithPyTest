import pytest


# start with test
# end with test

@pytest.mark.example
def test_method1():
    x = 5
    y = 10
    assert x == y


def test_method2():
    x = 14
    y = 20
    assert x + 6 == y

@pytest.mark.example
def test_method3():
    name = 'selenium'
    assert name.upper() == 'SELENIUM', "Test case failed due to data mismatch"


def test_method4():
    assert True


def test_method5():
    assert False, "Test case failed due to data mismatch"

@pytest.mark.example
def test_method6():
    assert 'admin' == 'admin123', "failed coz not equal"