# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:38:38 2023

@author: HumbertoPena
"""

#Las listas en python son los arrays (Coleccion de elementos)

Materias = ["Inteligencia artificial", "Visión artificial", "Teoria de control", "PLCS"]
# Imprimir elemento referenciando la posicion del datos según la dimension que haya
print(Materias[0])

# Lista de listas
MateriasCalificación = [["Inteligencia artificial",100],["Visión artificial",100],["Teoria de control",98],["PLCS",100]]
#Imprimir haciendo referencia en su doble dimension 
print(MateriasCalificación[0][0],": ",MateriasCalificación[0][1])



#Referencias negativas
# se puede acceder a los ultimos elementos de alguna lista utili<zando numeros negativos 
# el -1 seria para el ultimo y ase de manera decremental

print(MateriasCalificación[-1][-2],": ",MateriasCalificación[-1][-1])


#Eliminar elementos de lista del()

# borrará todo el ultimo elemento
print(MateriasCalificación)
del MateriasCalificación[-1]
print(MateriasCalificación)
#borrar ultimo elemento de la lista del primer elemento
del MateriasCalificación[0][-1]
print(MateriasCalificación)

#Eliminar elemento con nombre .remove()

MateriasCalificación[0].remove("Inteligencia artificial")
print(MateriasCalificación)
del MateriasCalificación[0]

#Eliminar de lista elemento y guardarlo en variable  .pop()

Guardalista = MateriasCalificación.pop(0)
print(MateriasCalificación)
print(Guardalista)


#Añadir elementos nuevos al final de la lista .append()

MateriasCalificación.append(["Inteligencia Artificial",100])
print(MateriasCalificación)


# Agregar elementos el en lugar deseado con .insert()

MateriasCalificación.insert(1,["Visión artificial",99])
print(MateriasCalificación)

#Ordenar elementos de lista  .sort() ordenamiento alfabetico

MateriasCalificación.sort()
print(MateriasCalificación)

#Ordenar elementos de lista  .sort() ordenamiento alfabetico inversocon reverse = true de manera permanente

MateriasCalificación.sort(reverse=True)
print(MateriasCalificación)

#metodo sorted() para usarse sobre un print y que no haga acciones en la lista 

print(sorted(MateriasCalificación))
print(MateriasCalificación)

# Contar elementos de lista len()
# Imprime el numero de elementos 
print(len(MateriasCalificación))

