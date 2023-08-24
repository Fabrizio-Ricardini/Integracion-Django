"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia)"""


def creador_dict(cadena):
    lista = cadena.split()
    dict = {}
    for i in lista:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


lista = input("Ingrese la lista:")
dict1 = creador_dict(lista)
print(dict1)
