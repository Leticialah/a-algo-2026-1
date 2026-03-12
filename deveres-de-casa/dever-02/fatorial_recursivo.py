import time
import sys

# aumentando o limite de recursão
sys.setrecursionlimit(3000)


def fatorial(n):

    # caso base
    if n == 0 or n == 1:
        return 1

    # chamada recursiva
    return n * fatorial(n - 1)


valores = [10, 100, 500, 1000]

for n in valores:

    inicio = time.time()

    resultado = fatorial(n)

    fim = time.time()

    tempo_execucao = fim - inicio

    print("\nValor de n:", n)
    print("Fatorial de", n, "calculado.")
    print("Tempo de execução:", tempo_execucao, "segundos")
