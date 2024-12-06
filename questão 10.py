from collections import deque

fila_atendimento = deque()

def adicionar_chamado(chamado):
    fila_atendimento.append(chamado)
    print(f"Chamado '{chamado}' adicionado à fila.")

def atender_chamado():
    if fila_atendimento:
        chamado = fila_atendimento.popleft()
        print(f"Chamado '{chamado}' atendido e removido da fila.")
    else:
        print("Nenhum chamado na fila para atender.")

adicionar_chamado("Chamado 1")
adicionar_chamado("Chamado 2")
adicionar_chamado("Chamado 3")

print("\nAtendendo chamados:")
atender_chamado()
atender_chamado()
atender_chamado()
atender_chamado()
