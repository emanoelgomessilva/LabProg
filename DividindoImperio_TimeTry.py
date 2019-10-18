import math

#Classe que rerpresenta uma cidade do imperio
class Cidade:
    def __init__(self):
        #Código da cidade
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

#Função utilizada para mapear as cidades que farão parte do novo império dividido, ela recebe como parâmetros, a
#primeira cidade que será percorrida, a estrada que será removida, o mapa com todas as cidades do império atual e uma
# lista que armazenará as cidades que farão parte do novo império
def mapeiaCidades(inicio,estrada, mapa,cidades):
    vizinhos = mapa[inicio].getVizinhos()
    #A partir de inicio, serão percorridos de forma recursiva os seus vizinhos
    for vizinho in vizinhos:
        # Se o vizinho não estiver nas cidades ou ele for igual ao destino da estrada removida
        if ((vizinho not in cidades) or (vizinho == int(estrada[1]))):
            #Se a cidade de inicio for diferente da origem da estrada bloqueada ou a sua cidade vizinha for diferente
            #do destino da estrada removida, significa que há um estrada disponível entre as duas cidades
            if((inicio+1 != int(estrada[0]) or vizinho != int(estrada[1]))):
                #Se o vizinho não estiver no percurso da estrada que foi removida e não estiver registrado nas cidades
                #do novo imperio, ele será inserido novo imperio, caso contrário, se a cidade inicio testada na recursão
                #não estiver nas cidades do novo imperio, ela será inserida na lista das novas cidades
                if vizinho not in cidades:
                    if vizinho != int(estrada[0]) and vizinho != int(estrada[1]):
                        cidades.append(vizinho)
                    elif inicio+1 not in cidades:
                        cidades.append(inicio+1)
                    #Em seguida será feita uma chamada recursiva do procedimento para o vizinho, sendo ele o novo inicio
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

#Será feita a execução do procedimento de mapearCidades para cada possibilidade de estrada removida, a quantidade de
#cidades do primeiro imperio será a quantidade de cidades retornada do procedimento e a quantidade de cidades do segundo
#imperio será igual a diferença entre a quantidade de cidades total do imperio atual e a quantidade de cidades
#resultantes do imperio atual. após isso é calculada a diferença entre a quantidade de cidades dos dois imperios e se
#essa diferença for menor do que a menor diferença encontrada anteriormente ela será a nova menor diferença.
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


