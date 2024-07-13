import unittest

from models.boa_constrictor import Boa_Constrictor

class TestBoa(unittest.TestCase):
    def test_hacer_sonido(self):
        boa1 = Boa_Constrictor('loki', 24.7, 3, 'colombia', 38300)
        self.assertEqual(boa1.hacer_sonido(), '¡Tsss!')
    
    def test_calcular_flete(self):
        boa1 = Boa_Constrictor('loki', 24.7, 3, 'colombia', 38300)
        self.assertEqual(boa1.calcular_flete(), (24.7*38300))
        
    def test_comer_ratones(self):
        boa1 = Boa_Constrictor('loki', 24.7, 3, 'colombia', 38300)
        self.assertEqual(boa1.obtener_ratones_comidos(),0)
        boa1.comer_ratones(3)
        self.assertEqual(boa1.obtener_ratones_comidos(), 3)
        boa1.comer_ratones(5)
        self.assertEqual(boa1.obtener_ratones_comidos(), 8)
        