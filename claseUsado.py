from claseVehiculo import Vehiculo


class Usado(Vehiculo):
    __marca=""
    __patente=""
    __año=0
    __kilometraje=0



    def __init__(self,marca,patente,año,kilometraje):
        self.__marca=marca
        self.__patente=patente
        self.__año=año
        self.__kilometraje=kilometraje



    def calcularImporte(self):
        año=input("ingrese el año actual")
        calculo=año-int(self.__año)
        porcentaje=(super().__precioBase*calculo)/100
        calculo2=0
        if self.__kilometraje>200000:
            calculo2=(super().__precioBase*2)/100

        impore=super().__precioBase-porcentaje-calculo2
        return impore



