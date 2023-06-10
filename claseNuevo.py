from claseVehiculo import Vehiculo

class Nuevo(Vehiculo):
    __version=""
    marca="Ford"


    def __init__(self,version):
        self.__version=version


    @classmethod
    def getMarca(cls):
        return cls.marca



    def calcularImporte(self):
        calculo=(super().__precioBase*10)/100
        calculo2=0
        if self.__version=="full":
            calculo2=(super().__precioBase*2)/100
        importe=super().__precioBase+calculo+calculo2

        return importe



