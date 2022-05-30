"""OBTENER LA CANTIDAD DE LOS N PRIMEROS MULTIPLOS DE 5"""

print("-------------------------------")
print("---N PRIMEROS MULTIPLOS DE 5---")
print("-------------------------------")

#input
n1 = int(input("Ingrese la cantidad de multiplos: "))
n = 5

#processing and output
for i in range(n, (n*n1)+1, n):
    print(str(i)), ", "
