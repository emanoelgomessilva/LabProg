import math

class Vertice():
    def __init__(self):
        self.vizinhos = []
        self.peso = 0

    def getVizinhos(self):
        return self.vizinhos

    def setVizinhos(self, vizinhos):
        self.vizinhos = vizinhos

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

def Ordenar(Q):
    for i in range(1,len(Q)):
        x = Q[i]
        j = i-1
        while j>=0 and x.getPeso()<Q[j].getPeso():
            Q[j+1] = Q[j]
            j=j-1
        Q[j+1] = x

def dijkstra(grafo, origem, destino):
    Q = []
    grafo[origem-1].setPeso(0)
    for v in grafo:
        Q.append(v)

    Ordenar(Q)

    while Q:
        v = Q[0]
        Q.remove(v)
        for u in v.vizinhos:
            novoPeso = v.peso + int(u[1])
            if novoPeso < grafo[int(u[0])-1].peso:
                grafo[int(u[0])-1].peso = novoPeso
        Ordenar(Q)
    return grafo[destino-1].peso

entrada = input().split(" ")
n = int(entrada[0])
a = int(entrada[1])
b = int(entrada[2])
grafo = []
caminho = []
peso = 0
pesos = []

for i in range(1,int(n)+1):
    vertice = Vertice()
    vertice.setPeso(math.inf)
    grafo.append(vertice)

for i in range(int(n)-1):
    montaAresta = input().split(" ")
    arestas = []
    aresta = []
    aresta1 = []
    aresta.append(montaAresta[1])
    aresta.append(montaAresta[2])
    aresta1.append(montaAresta[0])
    aresta1.append(montaAresta[2])
    arestas = []
    arestas1 = []
    arestas.append(aresta)
    arestas1.append(aresta1)
    lista = grafo[int(montaAresta[0])-1].getVizinhos()
    lista.append(aresta)
    grafo[int(montaAresta[0])-1].setVizinhos(lista)
    lista1 = grafo[int(montaAresta[1])-1].getVizinhos()
    lista1.append(aresta1)
    grafo[int(montaAresta[1])-1].setVizinhos(lista1)

destino = dijkstra(grafo, a, b)

print(destino)