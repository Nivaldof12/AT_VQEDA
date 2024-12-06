def verifica_duplicatas(lista):
    elementos_vistos = set()

    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)

    return False

lista = [1, 2, 3, 4, 5, 6, 3]
if verifica_duplicatas(lista):
    print("A lista contém duplicatas.")
else:
    print("A lista não contém duplicatas.")
