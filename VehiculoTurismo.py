from Vehiculo import Vehiculo

class VehiculoTurismo(Vehiculo):
    def __init__(self, matricula, marca, modelo, Numero_puertas):
        super().__init__(matricula, marca, modelo)
        self._Numero_puertas = Numero_puertas

    def get_Numero_Puertas(self) -> int:
        return self._Numero_puertas
        
    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Numero de Puertas: {self._Numero_puertas}"