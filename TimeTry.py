
A minha estratégia foi inicialmente mapear as cidades existentes no imperio e as estradas que continham ele. Em seguida
a ideia seria de para cada possibilidade de estrada removida criar duas novas listas que seriam dois pedaços da antiga
lista sem a estrada retirada. Após isso seriaam percorridas estas duas listas e seriam verificadas as estradas contidas
nelas e quais cidades elas ligam. As cidades ligadas seriam adicionadas a uma lista de

def contaCidades(comeco, fim, estradas):
    estradasdividida = estradas[comeco, fim]
    estradascontadas = []
    for i in estradasdividida:
        if((i[0] not in estradascontadas)):
            estradascontadas.append(i[0])



numerocidades = input()
cidades = []
estradas = []

for i in range(1, numerocidades):
    cidades.append(i)

for i in range(1, numerocidades-1):
    estrada = input().split(" ")
    estradas.append(estrada)

