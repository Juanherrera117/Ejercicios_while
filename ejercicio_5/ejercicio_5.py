"""DETERMINAR LA CANTIDAD DE DIGITOS DEL NUMERO"""

print("-------------------------")
print("---CANTIDAD DE DIGITOS---")
print("-------------------------")

#input
n = int(input("Ingrese un numero: "))

count = 0

#processing
while n > 0:
    n //= 10
    count += 1

#output
print("El numero de digitos son:" + str(count))
