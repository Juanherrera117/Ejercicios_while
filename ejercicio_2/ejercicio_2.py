"""RANGO DE NUMEROS ENTEROS"""

from imaplib import Int2AP
from re import T

print("---------------")
print("---N ENTEROS---")
print("---------------")

#input
n = int(input("Ingrese un numero inicial: "))
i = int(input("Ingrese el numero final: "))

N = n + 1
T = i - n

#processing
for I in range(N, i):
    print(I)
if T == i - n:
    R = T - 1

#output
print("Los numeros que hay entre " + str(n) + " y " + str(i) + " son: " + str(R))