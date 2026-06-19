class UnionFind:
    def __init__(self, vertices):
        self.pai = list(range(vertices))
        self.rank = [0] * vertices

    def buscar_raiz(self, x):
        # Path Compression
        if self.pai[x] != x:
            self.pai[x] = self.buscar_raiz(self.pai[x])
        return self.pai[x]

    def unir(self, x, y):
        raiz_x = self.buscar_raiz(x)
        raiz_y = self.buscar_raiz(y)

        if raiz_x == raiz_y:
            return False  # formaria ciclo

        # Union by Rank
        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1

        return True


def kruskal_maximo(vertices, arestas):
    """
    vertices: quantidade de vértices
    arestas: lista de tuplas no formato (origem, destino, peso)
    """

    # Aqui está a principal modificação:
    # ordenar do maior peso para o menor peso
    arestas.sort(key=lambda x: x[2], reverse=True)

    uf = UnionFind(vertices)

    arvore_maxima = []
    custo_total = 0

    for origem, destino, peso in arestas:
        if uf.unir(origem, destino):
            arvore_maxima.append((origem, destino, peso))
            custo_total += peso

        # Para uma árvore geradora com V vértices, precisamos de V - 1 arestas
        if len(arvore_maxima) == vertices - 1:
            break

    return arvore_maxima, custo_total


# Exemplo de uso
vertices = 8

arestas = [
    (0, 1, 4),
    (0, 2, 8),
    (1, 2, 11),
    (1, 3, 8),
    (2, 4, 7),
    (3, 4, 2),
    (3, 5, 6),
    (4, 5, 14),
    (4, 6, 9),
    (5, 6, 10),
    (5, 7, 2),
    (6, 7, 1)
]

resultado, custo = kruskal_maximo(vertices, arestas)

print("Árvore Geradora Máxima:")
for origem, destino, peso in resultado:
    print(f"{origem} -- {destino} | peso = {peso}")

print(f"\nCusto total máximo: {custo}")
