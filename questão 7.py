def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

jogadores = [
    {"nome": "Nivaldo", "pontuacao": 90},
    {"nome": "Pedro", "pontuacao": 50},
    {"nome": "Matheus", "pontuacao": 70},
    {"nome": "Alexssandro", "pontuacao": 10},
]

pontuacoes = [jogador["pontuacao"] for jogador in jogadores]

selection_sort(pontuacoes)

print("Pontuações ordenadas:", pontuacoes)
