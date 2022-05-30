"""CANTIDAD DE VECES QUE SALE EL NUMERO 3 AL LANZAR N VECES UN DADO"""

print("-------------------")
print("----10 VECES------")
print("-------------------")

import random
I = 1
N = 0
#processing
while I <= 10:
    numero = random.randint(1,6)
    print(str(numero))
    I = I + 1 
    if numero / 3 == 1:
        N = N + 1
        

print("Las veces que sale el numero 3 es : " + str(N))
