historico_voltar = []
historico_avancar = []

pagina_atual = "Página Inicial"

def navegar_para(nova_pagina):
    global pagina_atual
    historico_voltar.append(pagina_atual)
    pagina_atual = nova_pagina
    historico_avancar.clear()
    print(f"Navegando para: {pagina_atual}")

def voltar():
    global pagina_atual
    if historico_voltar:
        historico_avancar.append(pagina_atual)
        pagina_atual = historico_voltar.pop()
        print(f"Voltando para: {pagina_atual}")
    else:
        print("Não há páginas para voltar.")

def avancar():
    global pagina_atual
    if historico_avancar:
        historico_voltar.append(pagina_atual)
        pagina_atual = historico_avancar.pop()
        print(f"Avançando para: {pagina_atual}")
    else:
        print("Não há páginas para avançar.")

navegar_para("Página 1")
navegar_para("Página 2")
voltar()
voltar()
avancar()
