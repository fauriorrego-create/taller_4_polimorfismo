
from Vehiculo import Vehiculo
from VehiculoTurismo import VehiculoTurismo
from VehiculoFurgoneta import VehiculoFurgoneta
from VehiculoDeportivo import VehiculoDeportivo

def main():
    turismo = [
        VehiculoTurismo("1234ABC","Toyota","Corolla",4),

        VehiculoTurismo("354cfr","subaru","Impresa",4),

        VehiculoTurismo("934fas","Chevrolet","Camper",4)
    ]

    furgoneta = [
        VehiculoFurgoneta("5678DEF","Ford","Transit",1000),

        VehiculoFurgoneta("926glk","Chevrolet","Pickup",1000),

        VehiculoFurgoneta("109mkf","Renault","Suburban",1000)
    ]    

    deportivo = [
        VehiculoDeportivo("201cjs","Chevrolet","Camaro",6500,),

        VehiculoDeportivo("554bcv","Toyota","Supra",8000),

        VehiculoDeportivo("9101GHI","Nissan","Skileine",4500)
    ]    

    print("Datos de los Vehiculos Turismos:")
    for v in turismo:
        print(v.mostrar_datos())
        print("---------------------")

    print("\n Datos de los Vehiculos Furgonetas:")
    for x in furgoneta:
        print(x.mostrar_datos())
        print("---------------------")

    print("\n Datos de los Vehiculos Deportivos:")
    for y in deportivo:
        print(y.mostrar_datos())
        print("---------------------")
        

if __name__ == "__main__":
    main()
