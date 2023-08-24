"""Escribir una función que calcule el máximo común divisor entre dos números"""
import math

n1 = int(input("Ingrese un numero:"))
n2 = int(input("Ingrese otro numero:"))
mcm = math.gcd(n1, n2)
print("El máximo común divisor entre los números es :", mcm)
