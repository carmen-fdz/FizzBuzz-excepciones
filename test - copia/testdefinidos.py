def fizzbuzz(numero):
    if not isinstance(numero, int):
        raise TypeError("El valor debe ser un número entero")
    if numero == 0:
        return "FizzBuzz"
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero


def test_divisible_por_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"


def test_divisible_por_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"


def test_divisible_por_3_y_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"


def test_no_divisible_por_3_ni_5():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(7) == 7


def test_valor_no_numerico():
    try:
        fizzbuzz("hola")
        assert False  
    except TypeError:
        assert True

    try:
        fizzbuzz([3])
        assert False
    except TypeError:
        assert True


def test_divisible_por_0():
    assert fizzbuzz(0) == "FizzBuzz"

