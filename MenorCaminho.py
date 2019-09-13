class Aresta():
    def __init__(self):
        self.cidades = []
        self.peso = 0
        self.marcado = ""

    def getCidades(self):
        return self.cidades

    def setCidades(self, cidades):
        self.cidades = cidades

    def getMarcado(self):
        return self.marcado

    def setMarcado(self, marcado):
        self.marcado = marcado

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

def mapeiaCaminho(origem, destino, arestas, caminho):
    menorArestaOrigem = 1000000
    menorArestaDestino = 1000000
    menorDistanciaOrigem = 1000000
    menorDistanciaDestino = 1000000

    for i in range(len(arestas)):
        soma = i
        if((arestas[i].getCidades().__contains__(origem)) and (arestas[i].getCidades().__contains__(destino))):
            caminho= caminho + arestas[i].getPeso()
            return caminho
        if((arestas[i].getCidades()[0]) == (arestas[i].getCidades()[1])):
            return caminho
        if ((arestas[i].getCidades()[0] == origem) and (arestas[i].getPeso() < menorDistanciaOrigem)):
            menorDistanciaOrigem = arestas[i].getPeso()
            menorArestaOrigem = soma
        if ((arestas[i].getCidades()[0] == destino) and (arestas[i].getPeso() < menorDistanciaDestino)):
            menorDistanciaDestino = arestas[i].getPeso()
            menorArestaDestino = soma
    if(menorArestaOrigem != 1000000):
        arestas[menorArestaOrigem].setMarcado("s")
    if (menorArestaDestino != 1000000):
        arestas[menorArestaDestino].setMarcado("s")
    if(menorDistanciaOrigem == 1000000):
        caminho = caminho + menorDistanciaDestino
    elif (menorDistanciaDestino == 1000000):
        caminho = caminho + menorDistanciaOrigem
    else:
        caminho = caminho + menorDistanciaOrigem + menorDistanciaDestino
    if(menorArestaOrigem != 1000000 and arestas[menorArestaOrigem].getCidades()[0] == origem):
        origem = arestas[menorArestaOrigem].getCidades()[1]
    elif(menorArestaOrigem != 1000000):
        origem = arestas[menorArestaOrigem].getCidades()[0]
    if (menorArestaDestino != 1000000 and arestas[menorArestaDestino].getCidades()[0] == destino):
        destino = arestas[menorArestaDestino].getCidades()[1]
    elif(menorArestaDestino != 1000000):
        destino = arestas[menorArestaDestino].getCidades()[0]

        mapeiaCaminho(origem, destino, arestas, caminho)
    return caminho

entrada = input().split(" ")
n = int(entrada[0])
a = int(entrada[1])
b = int(entrada[2])
arestas = []
caminho = 0
OrigemPercorrida=0
Destinopercorrido = 0

for i in range(int(n)-1):
    montaAresta = input().split(" ")
    aresta = Aresta()
    cidades = []
    cidades.append(int(montaAresta[0]))
    cidades.append(int(montaAresta[1]))
    aresta.setCidades(cidades)
    aresta.setPeso(int(montaAresta[2]))
    arestas.append(aresta)

print(mapeiaCaminho(a, b, arestas, caminho))








