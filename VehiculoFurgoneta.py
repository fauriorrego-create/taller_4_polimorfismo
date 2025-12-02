from Vehiculo import Vehiculo

class VehiculoFurgoneta(Vehiculo):
    def __init__(self,matricula,marca,modelo,Carga):
        super().__init__(matricula,marca,modelo)
        self._Carga = Carga 

def get_Carga(self) -> int:
    return self._Carga

def mostrar_datos(self) ->str:
    return super().mostrar_datos() + f"\n Carga: {self._Carga}"
