# Para a resolução do problema foi utilizada uma heurística de coloração de grafos, onde cada província foi representada
# por um vértice do grafo e as fronteiras entre as províncias por um conjunto de arestas para cada vértice. Na
# heurísticautilizou-se um conjunto de cores que representaram a quantidade máxima de cores que poderiam ser utilizadas
# para colorir  o mapa. Cada província é iniciada com a cor "0" e será mudada à medida que é checada a sua vizinhança.

#Classe que representa cada vértice
class Provincia:
    def __init__(self):
        #Código da província
        self.codigo = 0
        #Cor inicial do vértice
        self.cor = 0
        #Conjunto de arestas que ligam o vértice à seus vizinhos
        self.vizinhos = []

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
# 0 2 4 6
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
        provincia.setCor(0)
        provincia.setCodigo(codigo)
        provincia.setVizinhos(entrada)
        mapa.append(provincia)
        codigo+=1
        novaCor+=1
        cores.append(novaCor)
    except EOFError:
        break;
#Checagem da vizinhança de cada vértice, verifica se determinada cor já foi utilizada por algum vizinho. Se não, a cor
#será atribuída ao vértice, se sim a próxima cor da lista será verificada
for provincia in mapa:
    vizinhanca = provincia.getVizinhos()
    iterador = 0
    while iterador < len(cores):
        ocorrencia = 0
        for vizinho in vizinhanca:
            if mapa[int(vizinho)].getCor() == cores[iterador]:
                ocorrencia+=1
        if ocorrencia == 0:
            provincia.setCor(cores[iterador])
            iterador = len(cores)
        else:
            iterador+=1

#Verifica a cor com maior valor utilizada, como a lista de cores é ordenada, a maior cor utilizada, representa a
# quantidade de cores utilizada.
for provincia in mapa:
    if provincia.getCor() > maiorCor:
        maiorCor = provincia.getCor()

print(maiorCor)