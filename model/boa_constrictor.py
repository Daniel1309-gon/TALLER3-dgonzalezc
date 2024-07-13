from model.animal_exotico import AnimalExotico

class Boa_Constrictor(AnimalExotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0
        
    def hacer_sonido(self) -> None:
        return '¡Tsss!'
    
    def comer_ratones(self, ratones: int) -> None:
        if self.__ratones_comidos + ratones > 10:
            raise ValueError('Demasiados ratones!')
        else:
            self.__ratones_comidos += ratones
    
    def obtener_ratones_comidos(self) -> int:
        return self.__ratones_comidos
    
    def alimentar(self) -> str:
        try:
            self.comer_ratones(1)
            return "Éxito"
        except Exception as e:
            return str(e)
    