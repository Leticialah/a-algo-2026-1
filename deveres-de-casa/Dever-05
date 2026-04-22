import random
import math

# --------------------------------------------------
# 1) MERGE SORT
# Complexidade: O(n log n)
# --------------------------------------------------

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


# --------------------------------------------------
# 2) MULTIPLICAÇÃO DE MATRIZES
# Complexidade: O(n^3)
# --------------------------------------------------

def multiplicar_matrizes(A, B):
    n = len(A)

    # cria matriz resultado n x n preenchida com 0
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# --------------------------------------------------
# 3) RECORRÊNCIAS EM CÓDIGO
# --------------------------------------------------

# a) T(n) = 2T(n/4) + sqrt(n)
def recorrencia_a(n):
    if n <= 1:
        return 1
    return 2 * recorrencia_a(n // 4) + math.sqrt(n)

# b) T(n) = 2T(n/4) + n
def recorrencia_b(n):
    if n <= 1:
        return 1
    return 2 * recorrencia_b(n // 4) + n

# c) T(n) = 16T(n/4) + n^2
def recorrencia_c(n):
    if n <= 1:
        return 1
    return 16 * recorrencia_c(n // 4) + n**2


# --------------------------------------------------
# TESTES
# --------------------------------------------------

# Teste do Merge Sort
lista = [random.randint(0, 100) for _ in range(10)]
print("Lista original:", lista)
print("Lista ordenada com Merge Sort:", merge_sort(lista))

print("-" * 50)

# Teste da multiplicação de matrizes
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("Matriz A:")
for linha in A:
    print(linha)

print("Matriz B:")
for linha in B:
    print(linha)

C = multiplicar_matrizes(A, B)

print("Resultado A x B:")
for linha in C:
    print(linha)

print("-" * 50)

# Teste das recorrências
n = 16

print(f"Recorrência a para n={n}: {recorrencia_a(n)}")
print(f"Recorrência b para n={n}: {recorrencia_b(n)}")
print(f"Recorrência c para n={n}: {recorrencia_c(n)}")
