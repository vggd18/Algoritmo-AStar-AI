from database import *

class Cell:
    def __init__(self, parent = None, position = None, linha = None, g = 0):
        self.parent = parent
        self.position = position
        self.g = g #the cost of the cheapest known path from the start to a cell 
        self.h = 0 #the cost of the cheapest known path from the start to a cell 
        self.f = 0 #the sum of g and h
        self.linha = linha
    
    def __eq__(self, other):
        return self.position == other.position

#funcao que administra a troca de linhas de metro
def Swap(azul, amarela,vermelha, verde, filho, pai):
    if pai.position in vermelha and filho.position in vermelha:
        return "vermelha"
    elif pai.position in verde and filho.position in verde:
        return "verde"
    elif pai.position in amarela and filho.position in amarela:
        return "amarela"
    elif pai.position in azul and filho.position in azul:
        return "azul"

def Troca_de_linhas(azul, amarela,vermelha, verde, filho, pai):
    #descobre a linha inicial
    #verifica em cada caso se esta na mesma linha ou esta trocando e efetivamente troca a linha
    if pai.linha == "vermelha" and filho.position not in vermelha:
        filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
        return 4
    elif pai.linha == "verde" and filho.position not in verde:
        filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
        return 4
    elif pai.linha == "amarela" and filho.position not in amarela:
        filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
        return 4
    elif pai.linha == "azul" and filho.position not in azul:
        filho.linha = Swap(azul, amarela,vermelha, verde, filho, pai)
        return 4
    else:
        return 0
        
def sorting(cell):
    return cell.f

def reconstruct_path(final_cell):
    path = []
    current = final_cell
    while current is not None:
        path.append(f"E{current.position+1}|{current.linha}")
        current = current.parent
    return path[::-1]

def pathfinder(start, end, linha):
    start = Cell(None, start, linha)
    end = Cell(None, end)

    open_cells = [start]
    closed_cells = []
    while len(open_cells) > 0:
        open_cells.sort(key=sorting)
        fronteira = []
        for i in open_cells:
            j = i.position
            fronteira.append(f"E{j+1}")
        print(fronteira)
        current_cell = open_cells[0]
        closed_cells.append(current_cell.position)
        open_cells.pop(0)

        if current_cell == end:
            print(f"Caminho:{reconstruct_path(current_cell)}\nTempo gasto: {current_cell.g}")
            break
        
        for i in range(14):
            if distReal[current_cell.position][i] == INF or distReal[current_cell.position][i] == 0:
                continue
            if i in closed_cells:
                continue
            newcell = Cell(current_cell, i, current_cell.linha)
            newcell.g = current_cell.g + (distReal[current_cell.position][i] /30 * 60) + Troca_de_linhas(linha_azul, linha_amarela,linha_vermelha, linha_verde, newcell, newcell.parent)
            newcell.h = distdireta[end.position][i]
            newcell.f = newcell.g + newcell.h
            open_cells.append(newcell)
x = 1
while True:
    print(f"=========  RODADA {x}  =========")
    startStation = int(input("ESTAÇÃO QUE VOCÊ ESTÁ: ")) - 1    # Estação Inicial
    startLine = input("LINHA QUE VOCÊ ESTÁ: ").lower()
    endStation = int(input("ESTAÇÃO QUE VOCÊ DESEJA IR: ")) - 1 # Estação Final
    pathfinder(startStation,endStation, startLine)
    x = x+1