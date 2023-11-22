from database import *
#classe node
class Node():
    #Inicia o nó
    def __init__(self, parent = None, pos = None,):
        #pai do no
        self.parent = parent
        #qual estacao ele pertence
        self.pos = pos
        #o custo ate chegar nele
        self.g = 0
        #distancia euclidiana ate o destino
        self.h = 0
        #f + g
        self.f = 0
        #cor da linha que ele se encontra
        self.linha = "inicio"

#funcao que administra a troca de linhas de metro
def Swap(azul, amarela,vermelha, verde, filho, pai):
    if pai.pos in vermelha and filho.pos in vermelha:
        return "vermelha"
    elif pai.pos in verde and filho.pos in verde:
        return "verde"
    elif pai.pos in amarela and filho.pos in amarela:
        return "amarela"
    elif pai.pos in azul and filho.pos in azul:
        return "azul"
def Troca_de_linhas(azul, amarela,vermelha, verde, filho, pai):
    #descobre a linha inicial
    if pai.linha == "inicio":
        if pai.pos in vermelha and filho.pos in vermelha:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            pai.linha = filho.linha
            return 0
        elif pai.pos in verde and filho.pos in verde:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            pai.linha = filho.linha
            return 0
        elif pai.pos in amarela and filho.pos in amarela:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            pai.linha = filho.linha
            return 0
        elif pai.pos in azul and filho.pos in azul:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            pai.linha = filho.linha
            return 0
    else:
        #verifica em cada caso se esta na mesma linha ou esta trocando e efetivamente troca a linha
        if pai.linha == "vermelha" and filho.pos not in vermelha:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            return 4
        elif pai.linha == "verde" and filho.pos not in verde:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            return 4
        elif pai.linha == "amarela" and filho.pos not in amarela:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            return 4
        elif pai.linha == "azul" and filho.pos not in azul:
            filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
            return 4
        else:
            return 0
a = 0
while True:
    a = a+1
    print(f"======== RODADA {a} ========")
    eI = int(input("ESTAÇÃO QUE VOCÊ ESTÁ: ")) - 1      # Estação Inicial

    eF = int(input("ESTAÇÃO QUE VOCÊ DESEJA IR: ")) - 1 # Estação Final
    #lista aberta = fronteira
    #lista fechada = caminho
    lista_aberta = []
    lista_fechada = []
    #escolhe a linha inicial
    start_node = Node(None, eI)

    lista_aberta.append(start_node)

    while len(lista_aberta) > 0:
        fronteira = []
        for i in lista_fechada:
            fronteira.append(i.pos)
        print(fronteira)
        
        #checa o no que tem o menor f para usar de current node
        current_node = lista_aberta[0]
        current_index = 0
        for index, no in enumerate(lista_aberta):
            if no.f < current_node.f:
                current_node = no
                current_index = index
        #tira da fronteira e coloca no caminho
        lista_aberta.pop(current_index)
        lista_fechada.append(current_node)

        if current_node.pos == eF:
            #caso chegue no destino, faz o caminho a ser printado
            caminho = []
            g_total = current_node.g
            current = current_node
            while current != None:
                caminho.append(f"E{current.pos + 1}")
                current = current.parent
            break
        
        filhos = []
        for i in range(14):
            #verifica se existe caminho pro filho percorrer
            if distReal[current_node.pos][i] == INF or distReal[current_node.pos][i] == 0:
                continue
            #cria o filho e guarda pai e posicao
            new_node = Node(current_node, i)
            filhos.append(new_node)
        #verifica se o filho faz parte do caminho, ou seja, se esta repetido
        for filho in filhos:
            if filho in lista_fechada:
                continue
            #adiciona os valores importantes para o filho
            #g eh composto do tempo total, ou seja, tempo do pai acumulado, mais o tempo do pai em minutos para chegar no filho mais o tempo de troca de estacao caso seja aplicavel
            filho.g = ((distReal[current_node.pos][filho.pos] / 30) * 60) + filho.parent.g + Troca_de_linhas(linha_azul, linha_amarela,linha_vermelha, linha_verde, filho, filho.parent)
            filho.h = distdireta[filho.pos][eF]
            filho.f = filho.g + filho.h
            #alem de verificar se esta repetido na fronteira, tambem ve se o caminho repetido eh melhor que o anterior
            for percorrido in lista_aberta:
                if filho == percorrido and filho.g > percorrido.g:
                    continue
            #coloca o filho na fronteira
            lista_aberta.append(filho)
    print(f"caminho: {caminho[::-1]}")
    print(f"tempo gasto: {round(g_total, 2)}")
    print("")

