# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:33:07 2023

@author: HumbertoPena
"""
# diccionarios 1

#diccionarios listas o colecciones desordenas, modificables, indexables se añanden elementos ya tributos 

M1 = {
    "Semestre": "Sexto",
    "Materia": "IA",
    "Calificacion": "100"  
    }
M2 = {
    "Semestre": "Sexto",
    "Materia": "VA",
    "Calificacion": "99"  
    }

consulta = M1["Materia"],M1["Calificacion"],M2["Materia"],M2["Calificacion"]
print(consulta)

# DICT PARA MOSTRAR DICCIONARIO

MuestraMateria = dict(M1)
print(MuestraMateria)

#diccionarios 2
# imprimir diccionario completo otra formacls
print(M1)

# get para obtener algun valor del diccionario

consultaa = M1.get("Calificacion")
print(consultaa)

# modificar valor
print(M2)
M2["Calificacion"] = "100"

print(M2)

# FOR EN DICCIONARIOS
# muestra elementos sin valor
for x in M1:
    print(x)
    
for x in M1:
    print(M1[x])    
    
    # funcion values para mostrar valores
for x in M1.values():
    print(x)
    
  # consultar categoria y valor

for x,y in M1.items():
    print(x,": ",y)
    
    
#DICCIONARIOS 3

print(len(M1) + len(M2))  

# metodo .pop() en diccionario

M2.pop("Semestre")
print(M2)

# del para eliminar elementos con del

del M2["Calificacion"]
print(M2)

# vaciar diccionario con .clear 
M2.clear()
print(M2)
# elimiar diccionario con del
del M2

   
#Añadir elemento en diccionario

M1["Status"] = "Regular"
print(M1)


#crear copia exacta con metodo copy()

copia = M1.copy()

print(copia)

#dict tambien es contrsuctor de diccionarios

copia2 = dict(M1)

print(copia2)
#constructor
copia3 = dict(Semestre = "Sexto",
              Materia = "PLCS",
              Status = "Regular")

print(copia3)
    
# fromkeys para agregar valores y atributos en diccionario
# si no se le asigna valor se toma como nulo
copia4 = ("Semestre","Materia","Calificacion","Status")    
elem = "vacio"

copia4 = dict.fromkeys(copia4,elem)
print(copia4)
copia4 = dict.fromkeys(copia4,"sin nada")
print(copia4)


#elementos sin atributos

VistaMateria = M1.keys()
print(VistaMateria)


#actualizar elementos 

copia3.update({"Materia" : "PLC"})
print(copia3)

#Buscar con if elemento

if "Calificacion" in M1:
    print("La materia: ",M1["Materia"]," tiene calificacion registrada")
else:
    print("No se ha registrado calificacion para: ",M1["Materia"])    

if "Calificacion" in copia3:
    print("La materia: ",copia3["Materia"]," tiene calificacion registrada")
else:
    print("No se ha registrado calificacion para: ",copia3["Materia"])   
    
#ANIDAR DICCIONARIOS

materias = {
    "M1" : {
        "Semestre": "Sexto",
        "Materia": "IA",
        "Calificacion": "100"  
        },
    "M2" : {
        "Semestre": "Sexto",
        "Materia": "VA",
        "Calificacion": "99"  
        }
    }    

print(materias)

# cantidad de diccionarios dentro

print(len(materias))
    