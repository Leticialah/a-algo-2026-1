from dataclasses import dataclass


@dataclass
class Paciente:
    id: str
    dor: int
    chegada: int


class MaxHeapTriagem:
    def __init__(self):
        self.heap = []
        self.posicao = {}
        self.ordem_chegada = 0

    def _prioridade_maior(self, p1, p2):
        # Maior dor tem prioridade.
        # Em caso de empate, quem chegou antes tem prioridade.
        if p1.dor != p2.dor:
            return p1.dor > p2.dor
        return p1.chegada < p2.chegada

    def _trocar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.posicao[self.heap[i].id] = i
        self.posicao[self.heap[j].id] = j

    def _subir(self, i):
        while i > 0:
            pai = (i - 1) // 2

            if self._prioridade_maior(self.heap[i], self.heap[pai]):
                self._trocar(i, pai)
                i = pai
            else:
                break

    def _descer(self, i):
        n = len(self.heap)

        while True:
            maior = i
            esq = 2 * i + 1
            dir = 2 * i + 2

            if esq < n and self._prioridade_maior(self.heap[esq], self.heap[maior]):
                maior = esq

            if dir < n and self._prioridade_maior(self.heap[dir], self.heap[maior]):
                maior = dir

            if maior != i:
                self._trocar(i, maior)
                i = maior
            else:
                break

    def inserir(self, id_paciente, dor):
        if id_paciente in self.posicao:
            raise ValueError("Paciente já existe na fila.")

        if dor < 1 or dor > 10:
            raise ValueError("A dor deve estar entre 1 e 10.")

        paciente = Paciente(id_paciente, dor, self.ordem_chegada)
        self.ordem_chegada += 1

        self.heap.append(paciente)
        self.posicao[id_paciente] = len(self.heap) - 1
        self._subir(len(self.heap) - 1)

    def extrair_max(self):
        if not self.heap:
            raise IndexError("Fila vazia.")

        mais_urgente = self.heap[0]
        ultimo = self.heap.pop()

        del self.posicao[mais_urgente.id]

        if self.heap:
            self.heap[0] = ultimo
            self.posicao[ultimo.id] = 0
            self._descer(0)

        return mais_urgente

    def atualizar_prioridade(self, id_paciente, nova_dor):
        if id_paciente not in self.posicao:
            raise ValueError("Paciente não encontrado.")

        if nova_dor < 1 or nova_dor > 10:
            raise ValueError("A dor deve estar entre 1 e 10.")

        i = self.posicao[id_paciente]
        dor_antiga = self.heap[i].dor

        self.heap[i].dor = nova_dor

        if nova_dor > dor_antiga:
            self._subir(i)      # Increase Key
        elif nova_dor < dor_antiga:
            self._descer(i)     # Decrease Key

    def vazio(self):
        return len(self.heap) == 0

    def mostrar_heap(self):
        print("\nFila atual:")
        for p in self.heap:
            print(f"Paciente: {p.id} | Dor: {p.dor} | Chegada: {p.chegada}")


# -------------------------------
# Programa principal
# -------------------------------

fila = MaxHeapTriagem()

n = int(input("Digite a quantidade de pacientes: "))

for i in range(n):
    nome = input(f"\nNome/ID do paciente {i + 1}: ")
    dor = int(input("Nível de dor (1 a 10): "))
    fila.inserir(nome, dor)

fila.mostrar_heap()

print("\nDeseja atualizar a prioridade de algum paciente?")
resposta = input("Digite S ou N: ").upper()

if resposta == "S":
    nome = input("Digite o nome/ID do paciente: ")
    nova_dor = int(input("Digite o novo nível de dor (1 a 10): "))
    fila.atualizar_prioridade(nome, nova_dor)

fila.mostrar_heap()

print("\nOrdem de atendimento:")

while not fila.vazio():
    paciente = fila.extrair_max()
    print(f"Atendendo: {paciente.id} | Dor: {paciente.dor}")
