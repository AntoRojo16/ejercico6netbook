class Vehiculo:
    __modelo=""
    __cantPuertas=0
    __color=""
    __precioBase=0



    def __init__(self,modelo,cant,color,precio):
        self.__modelo=modelo
        self.__cantPuertas=cant
        self.__color=color
        self.__precioBase=precio


    def calcularImporte(self):
        pass


    def getPrecioBase(self):
        return int(self.__precioBase)


    def modificarP(self, precio):
        self.__precioBase=precio


    def mostrar(self):
        print("Modelo {}, cantidad de puertas {}, color {}, precion base {}".format(self.__modelo,self.__cantPuertas,self.__color,self.__precioBase))

