# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:11:17 2023

@author: HumbertoPena
"""

# palabra reservada def para funciones
def saluda():
    print("Hola, como estas?")
    
saluda()    

# "Funcion con argumentos

def fms(nombre,idd):
    print(nombre + " Simpson ", idd)
    
b = "Bart"  
iddb = 4  
fms("Homero",1)    
fms("Lisa",2)
fms("March",3)
fms(b,iddb)







#Funciones 2
# args permite mandar una cantidad indefinida de argumentos    
# se pueden especificar cantidad de argumentos o con *args
def alumnos(materia,*args):
    print()
    print("El primer alumno es ", args[0], " y el ultimo es ", args[2], " Cursan la materia de ", materia)
    
    for x in args:
        print(x)
    
alumn = ["Jose","Juan","Pablo"]

alumnos("IA","Jose","Juan","Pablo")
# al mandar llamar la funcion, se pueden mandar tantos argumentos se deseen pero si es en variable debe
# ser por referencia
alumnos("IA",*alumn)  
    
    
    
    
    
    
    
    
    
    
    
# Funciones 3 diccionario en funciones

# funcion que recibe diccionario
def maestros(m1,m2,m3,m4):   
    print("Nombre maestro: "+ m1 + ".")
    
# funcion que recibe varios argumentos de un diccionario usando kwargs

def nmaestros(**kwargs):
    for x in kwargs:
        print("Nombre maestro: "+ kwargs[x] + ".")
    
    
#inicia el main del programa    

#Se manda diccionario a funcion
maestros(m1="Alan",m2="Gera",m3="Nacho",m4="Luis")   

mes={"m1" : "Alan",
     "m2" : "Gera",
     "m3" : "Nacho",
     "m4" : "Luis"}

#se manda diccionario por referencia cuando se manda cantidad no declarada de argmentos

nmaestros(**mes)

#se puede dejar funcion sin nada con pass

def funcionsinnada():
    pass 

# se puede mandar a llamar a la funcion con argumento o sin argumento

def funcionconosinargumentos(materia="IA"):
    print("Materia: "+ materia)

# se manda a llamar sin argumentos y tomara el declarado por default
funcionconosinargumentos()

# Se le manda argumento y sustituye al declarado

funcionconosinargumentos("VA")


