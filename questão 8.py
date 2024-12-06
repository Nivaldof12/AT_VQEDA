usuarios = {
    "nivaldofilho": {"nome": "Nivaldo Filho", "idade": 22, "cidade": "Caruaru"},
    "pedrohenrique": {"nome": "Pedro Henrique", "idade": 22, "cidade": "Caruaru"},
    "pedroviana": {"nome": "Pedro Viana", "idade": 22, "cidade": "Caruaru"},
}

def buscar_perfil(nome_usuario):
    if nome_usuario in usuarios:
        return usuarios[nome_usuario]
    else:
        return "Usuário não encontrado"

nome_usuario = "nivaldofilho"
perfil = buscar_perfil(nome_usuario)
print(f"Perfil de {nome_usuario}: {perfil}")
