class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if not self.raiz:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, atual, valor):
        if valor < atual.valor:
            if atual.esquerda:
                self._inserir(atual.esquerda, valor)
            else:
                atual.esquerda = No(valor)
        else:
            if atual.direita:
                self._inserir(atual.direita, valor)
            else:
                atual.direita = No(valor)

    def em_ordem(self):
        elementos = []
        self._em_ordem(self.raiz, elementos)
        return elementos

    def _em_ordem(self, atual, elementos):
        if atual:
            self._em_ordem(atual.esquerda, elementos)
            elementos.append(atual.valor)
            self._em_ordem(atual.direita, elementos)

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, atual, valor):
        if not atual:
            return None
        if valor < atual.valor:
            atual.esquerda = self._remover(atual.esquerda, valor)
        elif valor > atual.valor:
            atual.direita = self._remover(atual.direita, valor)
        else:
            if not atual.esquerda and not atual.direita:
                return None
            if not atual.esquerda:
                return atual.direita
            if not atual.direita:
                return atual.esquerda
            sucessor = self._minimo(atual.direita)
            atual.valor = sucessor.valor
            atual.direita = self._remover(atual.direita, sucessor.valor)
        return atual

    def _minimo(self, atual):
        while atual.esquerda:
            atual = atual.esquerda
        return atual

arvore = ArvoreBinariaBusca()
valores = [45, 25, 65, 20, 30, 60, 70]
for v in valores:
    arvore.inserir(v)

print("Árvore em ordem crescente:", arvore.em_ordem())
arvore.remover(20)
print("Após remover 20:", arvore.em_ordem())
arvore.remover(25)
print("Após remover 25:", arvore.em_ordem())
arvore.remover(45)
print("Após remover 45:", arvore.em_ordem())
