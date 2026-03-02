# A Barreira do n²

# Comparar empiricamente a eficiência de dois métodos de ordenação e indentificar o "ponto de ruptura" onde a teoria assinttótica se torna visível na prática.
# Implementar o algoritmo Insertion Sort O(n²)
# Utilizar a função do nativa do Python sorted() (Que usa o Timsort, O(n log n)) para fins de comparação.
# Gere listas aleatórias de tamanhos n = [1000, 5000, 10000, 20000, 50000].
# Meça os tempos de execução dos dois algoritmos para cada tamanho n de lista gerando a saída no terminal para cada um deles
# Usar a biblioteca time.

import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time
sizes = [1000, 5000, 10000, 20000, 50000]
for size in sizes:
    random_list = [random.randint(1, 100000) for _ in range(size)]
    
    insertion_time = measure_time(insertion_sort, random_list.copy())
    
    sorted_time = measure_time(sorted, random_list.copy())
    
    print(f"Size: {size} - Insertion Sort Time: {insertion_time:.6f} seconds - Sorted() Time: {sorted_time:.6f} seconds")

