# Codificacion para imprimir acentos 
# -*- coding: utf-8 -*- 
"""
Created on Sat Sep 16 11:46:42 2023

@author: HumbertoPena
"""

# Imprimir en pantalla
print("Imprimirmos texto en comillas dobles")
print('Imprimimos texto en comllias simples')

# Guardar texto en una variable
texto0 = "José Humberto Peña Torres"
texto = 'Ingenieria Mecatrónica'
print(texto0 + "\n" + texto)

# Englobar texto en diferentes "tipos de comillas" para poder imprimir la viceversa
print("Para escribir comillas 'simples' se engloba el string en comillas dobles (\")")
print('Para escribir comillas "dobles", se engloba el string en comillas simples (\')')
# AGREGANDO, TAQMBIEN SE PUEDEN USAR SECUENCIAS DE ESCAPE
print("O tambien se puede utilizar la misma comillas usando secuencias de escape gg")

#Concatenar cadena de carcteres

# Se declaran variables
V1 = "José Humberto"
V2 = "Peña torres"
# Se almacena concatenación en otra variable
NombreCompleto = V1 + " " + V2 + "."
# Se imprime la varibale donde se almacenó
print(NombreCompleto)
#Se concateca mismo tipo de dato al momento de imprimir
print(NombreCompleto + "\nMecatrónica")


