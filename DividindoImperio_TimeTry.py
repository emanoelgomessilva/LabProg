import math

class Cidade:
    def __init__(self):
        #Código da província
        self.codigo = 0
        #Conjunto de arestas que ligam o vértice à seus vizinhos
        self.vizinhos = []

    def getVizinhos(self):
        return self.vizinhos

    def setVizinhos(self,vizinhos):
        self.vizinhos = vizinhos

    def getCodigo(self):
        return self.codigo

    def setCodigo(self,codigo):
        self.codigo = codigo

def mapeiaCidades(inicio,estrada, mapa,cidades):
    vizinhos = mapa[inicio].getVizinhos()
    for vizinho in vizinhos:
        if ((vizinho not in cidades) or (vizinho == int(estrada[1]))):
            if((inicio+1 != int(estrada[0]) or vizinho != int(estrada[1]))):
                if vizinho not in cidades:
                    if vizinho != int(estrada[0]) and vizinho != int(estrada[1]):
                        cidades.append(vizinho)
                    elif inicio+1 not in cidades:
                        cidades.append(inicio+1)
                    mapeiaCidades(vizinho-1, estrada, mapa, cidades)
            else:
                break;
    return cidades

n = input()
mapa = []
estradas = []
cidades = []
menorDiferenca = math.inf
for i in range(int(n)):
    cidade = Cidade()
    cidade.codigo = i+1
    mapa.append(cidade)

for i in range(int(n)-1):
    entrada = input().split(" ")
    estradas.append(entrada)

for estrada in estradas:
    a = int(estrada[0])
    b = int(estrada[1])
    vizinhancaA = mapa[a-1].getVizinhos()
    vizinhancaA.append(b)
    mapa[a-1].setVizinhos(vizinhancaA)
    vizinhancaB = mapa[b-1].getVizinhos()
    vizinhancaB.append(a)
    mapa[b-1].setVizinhos(vizinhancaB)

for estrada in estradas:
    cidades = []
    imperio1 = mapeiaCidades(0, estrada, mapa, cidades)
    imperio2= len(mapa) - len(imperio1)
    diferenca = len(imperio1) - imperio2
    if(diferenca < 0):
        diferenca = diferenca * (-1)
    if diferenca < menorDiferenca:
        menorDiferenca = diferenca

print(menorDiferenca)


