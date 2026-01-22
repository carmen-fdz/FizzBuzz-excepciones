"""ejemplo de uso de unittest"""
import unittest
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(0, 1), -1)
if __name__ == "__main__":
    unittest.main()
    
    def raiz_cuadrada(x) :
        """Calcula la raiz cuadrada de un numero con unit test"""
        if x < 0 :
            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo")
        return x ** 0.5
