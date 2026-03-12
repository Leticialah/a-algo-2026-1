# a-algo-2026-1
# Análise de Algoritmos – Deveres de Casa
# Repositório com os deveres da disciplina **Análise de Algoritmos**.
Professor: Pablo Coelho Ferreira

# Dever 01 – Comparação de Algoritmos de Ordenação

## Objetivo
Comparar empiricamente dois algoritmos de ordenação para identificar o ponto em que a diferença de complexidade começa a aparecer na prática.

Os algoritmos comparados foram:

- **Insertion Sort**
- **sorted() do Python (Timsort)**

## Complexidade dos algoritmos

Insertion Sort

Melhor caso: O(n)  
Caso médio: O(n²)  
Pior caso: O(n²)

sorted() (Timsort)

Complexidade média: O(n log n)

# Dever 02 - Fatorial Recursivo

## Objetivo 
Implementar um algoritmo recursivo para calcular o fatorial de um número e analisar sua complexidade assintótica.

## Complexidade dos algoritmos
A função chama a si mesma reduzindo o valor de n em 1 a cada chamada.

Equação de recorrência:

T(n) = T(n-1) + 1

Isso significa que o algoritmo executa aproximadamente n chamadas recursivas.

Portanto a complexidade assintótica é:

O(n)

Ou seja, o tempo de execução cresce linearmente com o tamanho da entrada.
