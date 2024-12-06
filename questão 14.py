class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, atual, valor):
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = Node(valor)
            else:
                self._inserir(atual.esquerda, valor)
        else:
            if atual.direita is None:
                atual.direita = Node(valor)
            else:
                self._inserir(atual.direita, valor)

    def encontrar_minimo(self):
        if self.raiz is None:
            raise ValueError("A árvore está vazia, não há valor mínimo.")
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def encontrar_maximo(self):
        if self.raiz is None:
            raise ValueError("A árvore está vazia, não há valor máximo.")
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.valor

notas = [85, 70, 95, 60, 75, 90, 100]
arvore = ArvoreBinariaDeBusca()

for nota in notas:
    arvore.inserir(nota)

try:
    minimo = arvore.encontrar_minimo()
    maximo = arvore.encontrar_maximo()
    print(f"Nota mínima: {minimo}")
    print(f"Nota máxima: {maximo}")
except ValueError as e:
    print(e)
