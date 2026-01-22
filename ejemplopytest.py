""" ejemplo de uso de pytest"""
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 1) == -1
if __name__ == "__main__":
    import pytest
    pytest.main()