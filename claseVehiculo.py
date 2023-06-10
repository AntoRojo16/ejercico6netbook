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


