from database import *

class Node():
    #Inicia o nó
    def __init__(self, parent = None, pos = None):
        self.parent = parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0


eI = int(input("ESTAÇÃO QUE VOCÊ ESTÁ: ")) - 1      # Estação Inicial

eF = int(input("ESTAÇÃO QUE VOCÊ DESEJA IR: ")) - 1 # Estação Final

lista_aberta = []
lista_fechada = []

start_node = Node(None, eI)

lista_aberta.append(start_node)

while len(lista_aberta) > 0:
    current_node = lista_aberta[0]
    current_index = 0
    for index, no in enumerate(lista_aberta):
        if no.f < current_node.f:
            current_node = no
            current_index = index
    lista_aberta.pop(current_index)
    lista_fechada.append(current_node)
    
    if current_node.pos == eF:
        caminho = []
        g_total = current_node.g
        current = current_node
        while current != None:
            caminho.append(f"E{current.pos + 1}")
            current = current.parent
        break
    
    filhos = []
    for i in range(14):
        if distReal[current_node.pos][i] == INF or distReal[current_node.pos][i] == 0:
            continue
        new_node = Node(current_node, i)
        filhos.append(new_node)
    for filho in filhos:
        if filho in lista_fechada:
            continue
        
        filho.g = distReal[current_node.pos][filho.pos] + filho.parent.g
        filho.h = distdireta[filho.pos][eF]
        filho.f = filho.g + filho.h
        for percorrido in lista_aberta:
            if filho == percorrido and filho.g > percorrido.g:
                continue
        lista_aberta.append(filho)
print(f"caminho: {caminho[::-1]}")
print(f"tempo gasto: {round(g_total, 2)}")

