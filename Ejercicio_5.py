"""Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva."""


def get_int():
    flag = True
    while flag:
        try:
            n = int(input("Ingrese un valor: "))
            flag = False
        except ValueError:
            print("Valor inválido. Ingrese un numero entero :")
    return n


print(get_int())
