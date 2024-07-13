from models.animal import Animal
from abc import abstractmethod, ABC


class AnimalExotico(Animal, ABC):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuestos = impuestos
        
    def calcular_flete(self) -> float:
        return self._peso * self._impuestos
    
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    def obtener_pais_origen(self) -> str:
        return self._pais_origen
    
    def obtener_impuestos(self) -> float:
        return self._impuestos