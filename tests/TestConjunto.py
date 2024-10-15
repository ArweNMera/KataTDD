
import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto (unittest.TestCase):
    def test_conjunto_Vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.asserIsNone(conjunto.promedio()




