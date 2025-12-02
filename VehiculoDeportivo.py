from Vehiculo import Vehiculo

class VehiculoDeportivo(Vehiculo):
    def __init__(self,matricula,marca,modelo,Cilindrada):
        super().__init__(matricula,marca,modelo)
        self._Cilindrada = Cilindrada 

def get_Cilindrada(self) -> int:
    return self._Cilindrada

def mostrar_datos(self) ->str:
    return super().mostrar_datos() + f"\n Cilindrada: {self._Cilindrada}"