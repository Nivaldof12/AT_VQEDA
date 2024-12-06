def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

import random
import time

precos_1k = [random.randint(1, 10000) for _ in range(1000)]
precos_10k = [random.randint(1, 10000) for _ in range(10000)]

inicio = time.time()
bubble_sort(precos_1k)
tempo_1k = time.time() - inicio
print(f"Tempo para ordenar 1 mil elementos: {tempo_1k:.2f} segundos")

inicio = time.time()
bubble_sort(precos_10k)
tempo_10k = time.time() - inicio
print(f"Tempo para ordenar 10 mil elementos: {tempo_10k:.2f} segundos")