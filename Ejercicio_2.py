"""Escribir una función que calcule el mínimo común múltiplo entre dos números"""
import math

n1 = int(input("Ingrese un numero:"))
n2 = int(input("Ingrese otro numero:"))
lcm = math.lcm(n1, n2)
print("El mínimo común múltiplo entre los números es :", lcm)
