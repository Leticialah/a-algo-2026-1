def encontrar_subconjunto(S, T):
    """
    Verifica se existe um subconjunto de S cuja soma seja igual a T.
    Retorna True e o subconjunto encontrado, ou False e lista vazia.
    """

    def backtracking(indice, soma_atual, subconjunto):
        # Se encontrou a soma exata
        if soma_atual == T:
            return True, subconjunto

        # Se chegou ao final da lista
        if indice == len(S):
            return False, []

        # Opção 1: incluir o elemento atual
        existe, resultado = backtracking(
            indice + 1,
            soma_atual + S[indice],
            subconjunto + [S[indice]]
        )

        if existe:
            return True, resultado

        # Opção 2: não incluir o elemento atual
        existe, resultado = backtracking(
            indice + 1,
            soma_atual,
            subconjunto
        )

        if existe:
            return True, resultado

        return False, []

    return backtracking(0, 0, [])


# -------------------------------
# TESTE 1 - TAMANHO PEQUENO
# -------------------------------

S1 = [2, 4, 6, 10]
T1 = 16

existe, subconjunto = encontrar_subconjunto(S1, T1)

print("Teste 1 - Tamanho Pequeno")
print("Conjunto:", S1)
print("Alvo:", T1)
print("Existe subconjunto?", existe)
print("Subconjunto encontrado:", subconjunto)
print("Soma:", sum(subconjunto))
print()


# -------------------------------
# TESTE 2 - TAMANHO MÉDIO
# -------------------------------

S2 = [-5, -2, 1, 3, 7, 12, 15, 21]
T2 = 0

existe, subconjunto = encontrar_subconjunto(S2, T2)

print("Teste 2 - Tamanho Médio")
print("Conjunto:", S2)
print("Alvo:", T2)
print("Existe subconjunto?", existe)
print("Subconjunto encontrado:", subconjunto)
print("Soma:", sum(subconjunto))
print()


# -------------------------------
# TESTE 3 - TAMANHO GRANDE
# -------------------------------

S3 = [
    12345, 87654, 43210, 56789, 11111,
    22222, 33333, 44444, 55555, 66666,
    77777, 88888, 99999, 13579, 24680,
    11223, 33445, 55667, 77889, 99000,
    10101, 20202, 30303, 40404, 50505,
    60606, 70707, 80808, 90909, 10000
]

T3 = 500000

existe, subconjunto = encontrar_subconjunto(S3, T3)

print("Teste 3 - Tamanho Grande")
print("Conjunto:", S3)
print("Alvo:", T3)
print("Existe subconjunto?", existe)
print("Subconjunto encontrado:", subconjunto)
print("Soma:", sum(subconjunto))
print()


# -------------------------------
# ANÁLISE
# -------------------------------

print("Análise:")
print("Classe do problema: NP-Completo")
print("Complexidade de tempo no pior caso: O(2^n)")
print("Complexidade de espaço: O(n)")
print("Motivo: para cada número, o algoritmo testa duas opções: usar ou não usar.")
