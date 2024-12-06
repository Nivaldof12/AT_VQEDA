import os

def listar_arquivos(diretorio):
    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        
        if os.path.isfile(caminho_completo):
            print(caminho_completo)
        elif os.path.isdir(caminho_completo):
            listar_arquivos(caminho_completo)

listar_arquivos(r'C:\Users\jurem\Desktop\AT V')
