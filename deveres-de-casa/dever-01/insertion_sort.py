import random
import time


# Implementação do Insertion Sort O(n²)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


# tamanhos das listas
tamanhos = [1000, 5000, 10000, 20000, 50000]

for n in tamanhos:

    # gera lista aleatória
    lista = [random.randint(0, 100000) for _ in range(n)]

    # cópia para usar nos dois algoritmos
    lista_insertion = lista.copy()
    lista_sorted = lista.copy()

    # mede tempo do insertion sort
    inicio = time.time()
    insertion_sort(lista_insertion)
    fim = time.time()
    tempo_insertion = fim - inicio

    # mede tempo do sorted()
    inicio = time.time()
    sorted(lista_sorted)
    fim = time.time()
    tempo_sorted = fim - inicio

    print(f"Tamanho da lista: {n}")
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
    print(f"Python sorted(): {tempo_sorted:.6f} segundos")
    print("-" * 40)
