# Para a resolução do problema foi utilizada uma heurística de coloração de grafos, onde cada província foi representada
# por um vértice do grafo e as fronteiras entre as províncias por um conjunto de arestas para cada vértice. Na
# heurísticautilizou-se um conjunto de cores que representaram a quantidade máxima de cores que poderiam ser utilizadas
# para colorir  o mapa. Cada província é iniciada com a cor "0" e será mudada à medida que é checada a sua vizinhança.
# Foi utilizada nesta modificação a heurística de DSATUR, que consiste na vericação dos vértices de forma ordenada,
# daquele que possui o maior grau para o que possui o menor grau, checando as cores dos vizinhos de cada vétice.

#Classe que representa cada vértice
class Provincia:
    def __init__(self):
        #Código da província
        self.codigo = 0
        #Cor inicial do vértice
        self.cor = 0
        #Conjunto de arestas que ligam o vértice à seus vizinhos
        self.vizinhos = []
        #grau do vértice
        self.grau = 0

    def getCor(self):
        return self.cor

    def setCor(self, cor):
        self.cor = cor

    def getVizinhos(self):
        return self.vizinhos

    def setVizinhos(self,vizinhos):
        self.vizinhos = vizinhos

    def getCodigo(self):
        return self.codigo

    def setCodigo(self,vizinhos):
        self.codigo = codigo

    def getGrau(self):
        return self.grau

    def setGrau(self, grau):
        self.grau = grau

#Lista que comportará todos os vértices do grafo
mapa = []
#Lista com as possibilidades de cores para os vértices(a quantidade de cores será igual à quantidade de vértices)
cores = []

novaCor = 0
codigo = 1
#Variável que retornará quantas cores da lista foram utilizadas
maiorCor = 0

#Exemplo de entrada para 8 vértices, as arestas referenciam as províncias de 0 à 7, assim os vizinhos da província
# 0 são as províncias 1 e 4 por exemplo:

# 1 4
# 0 2 4 5 6
# 1 3 6 7
# 2 7
# 0 1 5 7
# 1 4 6 7
# 1 2 5 7
# 2 3 4 5 6

#Leitura da entrada. Cada linha comporta um conjunto de arestas que serão atribuídas à um novo vértice que será criado
while True:
    try:
        entrada = input().split(" ")
        provincia = Provincia()
        provincia.setCor(1)
        provincia.setCodigo(codigo)
        provincia.setVizinhos(entrada)
        provincia.setGrau(len(provincia.getVizinhos()))
        mapa.append(provincia)
        codigo+=1
        novaCor+=1
        cores.append(novaCor)
    except EOFError:
        break;
#Checagem da vizinhança de cada vértice, verifica se determinada cor já foi utilizada por algum vizinho. Se não, a cor
#será atribuída ao vértice, se sim a próxima cor da lista será verificada

# Ordenação do menor para o maior vértice de acordo com o grau;
for i in range(1, len(mapa)):
    peso = mapa[i].getGrau()
    k = i
    while k>0 and peso < mapa[k-1].getGrau():
        mapa[k] = mapa[k-1]
        k -= 1
    mapa[k] = mapa[i]

# O grafo é percorrido do vértice de maior grau para o vértice de menor grau e checa as cores de seus respectivos
# vizinhos.
for i in range(len(mapa)-1,0,-1):
    vizinhanca = mapa[i].getVizinhos()
    iterador = 0
    while iterador < len(cores):
        ocorrencia = 0
        for vizinho in vizinhanca:
            if mapa[int(vizinho)].getCor() == cores[iterador]:
                ocorrencia+=1
        if ocorrencia == 0:
            mapa[i].setCor(cores[iterador])
            iterador = len(cores)
        else:
            iterador+=1

#Verifica a cor com maior valor utilizada, como a lista de cores é ordenada, a maior cor utilizada, representa a
# quantidade de cores utilizada.
for provincia in mapa:
    if provincia.getCor() > maiorCor:
        maiorCor = provincia.getCor()

print(maiorCor)