def busca_binaria(lista, isbn):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == isbn:
            return meio, iteracoes
        elif lista[meio] < isbn:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, iteracoes

livros = list(range(100000, 200000))
len(livros)
isbn_procurado = 160000

indice, iteracoes = busca_binaria(livros, isbn_procurado)
if indice != -1:
    print(f"ISBN encontrado no índice {indice} em {iteracoes} iterações.")
else:
    print(f"ISBN não encontrado após {iteracoes} iterações.")
