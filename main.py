from claseColeccionVehiculos import Coleccion
from claseVehiculo import Vehiculo
from claseNuevo import Nuevo
from claseUsado import Usado
if __name__=="__main__":
    unVehiculoUsado=Usado("Focus",4,"rojo",2000000,"ford","123ale",2011,5000)
    unVehiculoNuevo=Nuevo("Palio",3,"negro mate",30000000,"base")
    listaVehiculos=Coleccion()
    listaVehiculos.agregarVehiculo(unVehiculoUsado)
    listaVehiculos.insertarElemento(unVehiculoNuevo)
    listaVehiculos.mostrarDatos()
