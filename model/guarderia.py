from model.boa_constrictor import Boa_Constrictor
from model.huron import Huron

class Guarderia():
    def __init__(self) -> None:
        self.boas = [Boa_Constrictor('loki', 24.7, 3, 'colombia', 38300),
                     Boa_Constrictor('isis', 34.7, 8, 'india', 90300)]
        self.hurones = [Huron("Huron1", 2.0, 3, "USA", 1000.0),
                        Huron("Huron2", 2.5, 4, "Canadá", 9020.0)]
        
    def alimentar_boa(self, boa: Boa_Constrictor):
        if not boa:
            return 'Esta boa no existe'
        try:
            resultado = boa.alimentar()
            return resultado
        except:
            return 'La boa está llena'
        
        
    
    