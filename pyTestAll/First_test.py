import pytest


# def func(x):
#     return x+5
#
# def test_method():
#     assert func(3) == 8
#
# def test_two():
#     x = 'hello'
#     assert hasattr(x, "c")


class test:

    def test1(self):
        a = 'yoyo'

    def test2(self):
        b = 'oyo'
        assert hasattr(test, 'a')
        print("worked fine")

@pytest.mark.example
def test_method4():
    assert False, "Test case failed due to data mismatch"
