from claseNodo import Nodo
from claseinterfaz import Interfaz
from claseNuevo import Nuevo
from claseUsado import Usado
import os

class Coleccion(Interfaz):
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0



    def __init__(self):
        self.__comienzo=None
        self.__actual=None


    def agregarVehiculo(self,vehiculo):
        if(type(vehiculo)==Usado or type(vehiculo)==Nuevo):
            nodo=Nodo(vehiculo)
            if(self.__comienzo==None):

                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__actual=nodo
                self.__tope+=1
            else:
                aux=self.__comienzo
                while(aux.getSiguiente()!=None):
                    aux=aux.getSiguiente()
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                self.__tope+=1
                os.system('cls')
                print ("*** VEHICULO AGREGADO CON EXITO ***")


    def InsertarVehiculo(self,pos,elemento):
        if(pos>=0 and pos<=self.__tope):
            nodo=Nodo(elemento)
            if(pos==0):
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__tope+=1
            else:
                num=1
                aux=self.__comienzo
                while(num<pos):
                    aux=aux.getSiguiente()
                    num+=1
                nodo.setSiguiente(aux.getSiguiente())
                aux.setSiguiente(nodo)
                self.__tope+=1


    def mostrarElemno(self, posicion):

