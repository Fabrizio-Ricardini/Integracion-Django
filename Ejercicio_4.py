"""Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia"""


def crear_dict(cadena):
    lista = cadena.split()
    dict = {}
    for i in lista:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


def contador_dict(diccionario):
    palabra_repetida = ""
    cantidad = 0
    for keys, values in diccionario.items():
        if values > cantidad:
            cantidad = values
            palabra_repetida = keys
    return palabra_repetida, cantidad


lista = input("Ingrese la lista:")
dict1 = crear_dict(lista)
print(dict1)
x, y = contador_dict(dict1)
print("La palabra mas frecuente es:", x, ",y se repite", y, "veces")
