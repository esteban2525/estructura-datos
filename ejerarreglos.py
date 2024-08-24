
pares = []

for i in range(1, 101):
    if i % 2 == 0:
        pares.append(i)

print(pares)

n_filas= 10
for i in range(1, n_filas+1):
        print("*" * i)
        


import random
numeros = [random.randint(1, 100) for _ in range(10)]

promedio = sum(numeros) / len(numeros)

print("Números",numeros)
print("Promedio", promedio)