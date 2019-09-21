
def encontrar_menor_caminho(inicio, fim, grafo, caminho, peso, pesos):
    for i in range(int(inicio),len(grafo)):
        if len(grafo[i]) > 0:
            for aresta in grafo[i]:
                if (int(aresta[0]) not in caminho and int(aresta[0]) is not fim):
                    caminho.append(int(aresta[0]))
                    peso = peso + int(aresta[1])
                    encontrar_menor_caminho(aresta[0], fim, grafo, caminho, peso, pesos)
                elif(int(aresta[0]) is fim):
                    peso = peso + int(aresta[1])
                    pesos.append(peso)
        else:
            peso = 0
    return pesos


entrada = input().split(" ")
n = int(entrada[0])
a = int(entrada[1])
b = int(entrada[2])
grafo = {}
caminho = []
peso = 0
pesos = []

for i in range(1,int(n)+1):
    grafo[i] = {}

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
    if(len(grafo.get(int(montaAresta[0]))) == 0):
        grafo[int(montaAresta[0])] = arestas
    else:
        lista = grafo[int(montaAresta[0])]
        lista.append(aresta)
        grafo[int(montaAresta[0])] = lista
    if (len(grafo.get(int(montaAresta[1]))) == 0):
        grafo[int(montaAresta[1])] = arestas1
    else:
        lista1 = grafo[int(montaAresta[1])]
        lista1.append(aresta1)
        grafo[int(montaAresta[1])] = lista1

print(min(encontrar_menor_caminho(a, b, grafo, caminho, peso,pesos)))
