# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:24:23 2023

@author: HumbertoPena
"""

# tuplas como listas pero en parentesis, lista puede variar y tupla no

tupla =  (("Inteligencia artificial",100),("Visión artificial",100),("Teoria de control",98),("PLCS",100))

print(tupla)

# para llamar elkemento usar corchetes 

print(tupla[0])
#imprimir diferentes tipos y usando operadores 
print(tupla[-1][-2],": ",tupla[-1][-1] - 1)


#Convertir tupla a lista y viceversa

Lista = list(tupla)

print(Lista)
# print(tupla)

Tuplan = tuple(Lista)
print(Tuplan)