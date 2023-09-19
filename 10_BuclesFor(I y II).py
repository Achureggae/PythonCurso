# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:16:36 2023

@author: HumbertoPena
"""

# bulces 1

clases = ("IA","VA","PLCS","Teoria","Vibraciones")

#recorrer lista o tupla
for x in clases:
    print(x)
    
#continue en ciclo for   y break para salir del ciclo o detenerlo y repetirlo 
    
for x in clases:
    if(x == "VA"):
        continue
    if(x == "Teoria"):
        break
    print(x)
    
#bucle for vacio con pass

for x in []:
    pass

#bucle for 2

#se le puede agregar en el valor que inicia, el valor de paro y el incremento en ese orden
for x in range(5,15,2)    :
    print(x)
    
    # se pueden anidar funciones en range
    
for x in range(len(clases)):
    print(clases[x])
    # else en el for para cuando termine
else:
    print("Se acabó el for")    
    
# se pueden anidar bucles

num1 = ["1","2","3","4","5"]    
num2 = "0"
num3 = "7"

for x in num1:
    for y in num2:
        for z in num3:
            print(x+y+z)
        
    
    
    
    