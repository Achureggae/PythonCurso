# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:09:50 2023

@author: HumbertoPena
"""


# .title método para cambiar a mayúscula  la primera letra de cada palabra del string
nombre = "variable en minusculas"
# Se aplica el metodo a la variable
Nombre = nombre.title()

# Se imprimen variables
print(nombre)
print(Nombre)
# Se puede aplicar el metodo dentro de otro
print(nombre.title() + " desde el print")


# .upper método para cambiar todo a mayusculas 

NMayu = nombre.upper()

#  .lower metodo para cambiar todo a minusculas
NMinu = NMayu.lower()

print("Se cambia de minusculas a mayusculas")
print(NMayu)
print("De mayusculas a minusculas")
print(NMinu)


# Saltos de linea y tabulaciones 
# Saltos de linea
print("José Humberto Peña Torres\nMecatrónica")
# Tabulaciones
print("\tJosé Humberto Peña Torres\n\t\tMecatrónica\n\t\t\t6E")