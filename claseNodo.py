class Nodo:
    __vehiclo=None
    __siguiente=None


    def __init__(self,vehiculo):
        self.__vehiclo=vehiculo
        self.__siguiente=None


    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getSiguiente(self):
        return self.__siguiente
    
