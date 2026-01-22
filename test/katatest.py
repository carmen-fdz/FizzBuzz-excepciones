"""En esta kata, se solicita al usuario un numero, si este es:
- Divisible entre 3, el programa debe imprimir "Fizz"
- Divisible entre 5, el programa debe imprimit "Buzz"
- Divisible entre 3 y entre 5, el programa debe imprimir "FizzBuzz"
- Si no es divisible ni entre 3 ni entre 5, debe imprimir el número"""
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return str(numero)
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado = fizzbuzz(numero)
    print(resultado)