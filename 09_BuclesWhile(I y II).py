# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:59:46 2023

@author: HumbertoPena
"""

# Bucles 1
x = 1

# se incrementa x hasta que se cumpla la condicion
while x <= 10:
    print(x)
    x += 1
    
    # se declara la frase
frase = "Lo que escribas lo repito"
# se concatena 
frase += "\nIntroduce la palabra salir para finalizar\n"

mensaje = ""
 # se ejecuta bucle infinito hasta que el usuario decida salir 
while mensaje != "salir":
    mensaje = input(frase)
    print(mensaje)
    
# bucles 2    

# uso de break para salir del bucle cuando se deseé
x = 1

while x <= 10:
    print(x)
    if x == 5:
        break
    x += 1    
    # else en un while
else:
    print("sali del bucle while")    
    
# continue saltar un bucle y repetiir
x = 1
while x <= 10:
    x += 1   
    if x >= 5 and x <= 8:
        continue
    print(x)



    