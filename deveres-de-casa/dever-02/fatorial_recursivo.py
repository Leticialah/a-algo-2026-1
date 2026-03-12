import time


# Função recursiva para calcular o fatorial
def fatorial(n):
    """
    Calcula o fatorial de um número utilizando recursão.

    Parâmetros:
    n (int): número inteiro

    Retorno:
    int: fatorial de n
    """

    # caso base
    if n == 0 or n == 1:
        return 1

    # chamada recursiva
    return n * fatorial(n - 1)


# valores de teste
valores = [10, 100, 500, 1000]

for n in valores:

    inicio = time.time()

    resultado = fatorial(n)

    fim = time.time()

    tempo_execucao = fim - inicio

    print(f"\nValor de n: {n}")
    print(f"Fatorial de {n} calculado.")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
