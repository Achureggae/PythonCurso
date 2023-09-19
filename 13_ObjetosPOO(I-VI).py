# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:13:12 2023

@author: HumbertoPena
"""

# objetos1

class carros():
    llantas = 4
    color = "Rojo"
    Encendido = False
    Combustible = True
    
    def encender(self):
        self.Encendido = True
        print("Encendio el carro")
        
# Se crea la instancia

carro1 = carros()        

#Se manda a llamar su funcion
carro1.encender()
#Se crea una segunda instancia del mismo tipo    
carros2 = carros()

carros2.encender()

class nave():
#Se utiliza __init__ como contructor del objeto

    def __init__(yo,nombre):
        # se inicializan variables
        yo.nombre=nombre

    def presentacion(yo):
        print("Hola, mi nombre es: " + yo.nombre)
    
        
     # se crea la instancia del objeto con parametro solicitado por contructor
     # y se manda llamar la funcon del mismo   
nave1=nave("José")        
nave1.presentacion()

# se puede cambiar los atributos
nave1.nombre="Pedro"

nave1.presentacion()



# objetos 4
# clase vacia

class sinada:
    pass

# eliminar propiedad con del

del nave1.nombre

# eliminar objeto
del nave1



# objetos 5   HERENCIA

# clase hijo
#hereda la clase carros
class ford(carros):
    
    def __init__(yo,nombre):
        yo.nombre = nombre
        
    def apagar(yo):
        yo.Encendido=False
        print("Se apagó el carro")
        
#instancia on herencia tendra sus funciones mas las heredadas    
nuevo=ford("LUIS")   

nuevo.encender()
nuevo.apagar()



#objetos6   heredar propuiedades y tener propias

class Nave4(nave):
    
    def __init__(yo,tipo,nombre):
        nave.__init__(yo,nombre)
        yo.tipo = tipo
        
    def apagar(yo):
        yo.Encendido=False
        print("Se apagó el carro")
        
    def saludo(yo):
        yo.presentacion()
        print(" Y soy tipo: " + yo.tipo)

n4 = Nave4("Guerra", "Juan")

n4.saludo()



 

    





