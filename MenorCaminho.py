import math

#classe que descreve um vértice. O mesmo terá o seu peso, que inicialmente será de 0, e uma lista de vizinhos, que terá
#um conjunto de listas, cada uma com 2 valores: o número do vizinho e a distância para se chegar a este vizinho.
#o peso de um vértice corresponderá à menor distância entre este vértice e o vértice de destino.
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

#Algoritmo usado para ordenar a priority queue, foi utilizado o insertion sort
def Ordenar(Q):
    for i in range(1,len(Q)):
        atual = Q[i]
        anterior = i-1
        while anterior>=0 and atual.getPeso()<Q[anterior].getPeso():
            Q[anterior+1] = Q[anterior]
            anterior=anterior-1
        Q[anterior+1] = atual
#Implementação do algoritmo de Dijkstra, que recebe como parâmetros, o grafo fornecido na entrada, o vertice inicial e o
#vértice final.
def dijkstra(grafo, origem, destino):
    #lista de prioridade para processamento dos vértices, ela conterá todos os
    Q = []
    #o vértice inicial começa com peso 0, denotando que ele é o início do caminho, sendo assim a distância percorrida
    #até o destino igual a 0
    grafo[origem-1].setPeso(0)
    #todos os vértices do grafo são adicionados à lista de prioridade
    for vertice in grafo:
        Q.append(vertice)
    #É feita a ordenação da lista de prioridade, ficando o vértice de menor peso sempre no inicio da lista. Desta forma
    #será sempre verificado o vértice de menor peso e seus vizinhos.
    Ordenar(Q)

    #enquanto a lista de prioridade tiver elementos, o laço será processado
    while Q:
        #vértice verificado
        vertice = Q[0]
        #o vértice verificado será removido da lista,evitando que ele seja verificado novamente
        Q.remove(vertice)
        #para cada vizinho de vertice será verificado se a soma do peso de vertice + a distancia percorrida até o
        #vizinho é menor do que o peso do vizinho, se sim o peso do vizinho será modificado para este somatório.
        #com isso, a tendência é que o processo se propague até o destino. No final deste processo, o peso de destino
        #corresponderá à menor distância entre origem e destino.
        for vizinho in vertice.vizinhos:
            novoPeso = vertice.peso + int(vizinho[1])
            if novoPeso < grafo[int(vizinho[0])-1].peso:
                grafo[int(vizinho[0])-1].peso = novoPeso
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