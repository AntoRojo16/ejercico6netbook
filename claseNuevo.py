from claseVehiculo import Vehiculo

class Nuevo(Vehiculo):
    __version=""
    marca="Ford"


    def __init__(self,modelo,cant,color,precio,version):
        super().__init__(modelo,cant,color,precio)
        self.__version=version


    @classmethod
    def getMarca(cls):
        return cls.marca



    def calcularImporte(self):
        calculo=(super().getPrecioBase()*10)/100
        calculo2=0
        if self.__version=="full":
            calculo2=(super().getPrecioBase()*2)/100
        importe=super().__precioBase+calculo+calculo2

        return importe


    def mostrar(self):
        super().mostrar()
        print("Version {}".format(self.__version,))



