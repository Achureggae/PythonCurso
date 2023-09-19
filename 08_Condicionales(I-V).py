# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:43:25 2023

@author: HumbertoPena
"""
import os

# Conicionales I

n1 = 10
n2 = 20
n3 = 30

if n1 == n2:
    print("Se ejecutó el if")
if n2 != n3:
    print("Se ejecutó el segundo if")
    
# Condicionales 2 else

# Mayor que no concidera el numero
if n2>20:
    print("Si es mayor")
else:
    print("Es menor")    
        
#mayor o igual que     
    
if n2>=20:
    print("Si es mayor")
else:
    print("Es menor") 
    
# condicionales 3 

# Se solicita datos en consola y se almacena en una variable
edad = int(input("Cual es tu edad?:  "))

if edad<=0:
    print("Edad no posible")
elif edad >= 1 and edad<= 17 :
    print("Menor de edad")    
elif edad<=100:
    print("Mayor de edad")
else:
    print("eres god")
    
    
# condicionales 4


equipos = ["atlas","chivas","america","puebla"]    

#Solicitar datos 
equipoo = input("Cual es el mejor equipo del mundo?:    ")
if equipoo in equipos and equipoo == "atlas":
    print("El mejor equipo")
else:
    print("Ese equipo es chico")
    
    
#Condicionales 5 
# Multiples condiciones

while(True):
    os.system("cls")
    print("\n\n\t\tSelecione la opcion que desee\n\n"
          "1.- Mandar saludo\n"
          "2.- Mandar despedida\n"
          "3.- Salir\n\n"
          "Ingrese el numero de la opcion que desee:  ")
    accion=[1,2]
    
    
    if 0 in accion or accion == []:
        print("\nIngrese una opción valida\n")
    if 1 in accion:
        print("\nHola como estas?\n")
    if 2 in accion:
        print("\nAdios, que te vaya bien\n")
    elif 3 in accion:
        break    
    else:
        print("\nIngrese una opción valida\n")

    res = int(input("presione 0 para regresar 3 para salir\n"))
    if res==0:
        continue
    if res==3:
        break
        
    

# Condicionales 6

