from database import *

eI = int(input("ESTAÇÃO QUE VOCÊ ESTÁ: ")) - 1      # Estação Inicial

eF = int(input("ESTAÇÃO QUE VOCÊ DESEJA IR: ")) - 1 # Estação Final

class Node():
    #Inicia o nó
    def __init__(self, parent = None, pos = None):
        self.parent = parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0

    #Verifica se os nós são iguais
    def __eq__(self, other):
        return self.pos == other.pos
