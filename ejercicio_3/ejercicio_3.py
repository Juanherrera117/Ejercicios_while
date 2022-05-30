"""OBTENER LA CANTIDAD DE NUMEROS PARES"""

print("-------------------")
print("---NUMEROS PARES---")
print("-------------------")

#input
n = int(input("Ingrese un numero inicial: "))
i = int(input("Ingrese el numero final: "))

T = i - n
X = T

#processing
if T == i - n:
     R = T
if R == T:
    X = R // 2 + 1
    while n <= i:
        if n % 2 == 0:
                print(n)
        n = n + 1

#output
print("Los numeros pares son: " + str(X))