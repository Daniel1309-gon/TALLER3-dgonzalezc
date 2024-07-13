import unittest

from models.huron import Huron

class TestHuron(unittest.TestCase):
    def test_hacer_sonido(self):
        boa1 = Huron('martin', 4.7, 5, 'usa', 20400)
        self.assertEqual(boa1.hacer_sonido(), 'Eek eek')
    
    def test_calcular_flete(self):
        boa1 = Huron('martin', 4.7, 5, 'usa', 20400)
        self.assertEqual(boa1.calcular_flete(), (4.7*20400))