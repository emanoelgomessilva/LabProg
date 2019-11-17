dimensoes = input().split(" ")
linha = [0] * int(dimensoes[1])
plantacao = [linha] * int(dimensoes[0])
aux = []
resultados = []
resposta = 0

for i in range(int(dimensoes[0])+1):
    aux1 = []
    for j in range(int(dimensoes[1])+1):
        aux1.append(0)
    aux.append(aux1)

for i in range(int(dimensoes[0])):
    elementos = input().split(" ")
    if(i < len(plantacao)):
        plantacao[i] = elementos

for i in range(1,int(dimensoes[0])+1):
    for j in range(1,int(dimensoes[1])+1):
        if(plantacao[i-1][j-1] != "" and aux[i][j-1] != "" and aux[i-1][j] != "" and aux[i-1][j-1] != ""):
            if ((i - 1 > 0 and j - 1 > 0)):
                aux[i][j] = int(plantacao[i-1][j-1])+(int(aux[i][j-1])+int(aux[i-1][j])-int(aux[i-1][j-1]))

for i in range((int(dimensoes[2])-1)+1,int(dimensoes[0])+1):
    for j in range((int(dimensoes[3])-1)+1,int(dimensoes[1])+1):
        resultado = aux[i][j]-aux[i-int(dimensoes[2])][j]-aux[i][j-int(dimensoes[3])]+aux[i-int(dimensoes[2])][j-int(dimensoes[3])]
        resultados.append(resultado)

for i in resultados:
   if i > resposta:
       resposta = i

print(resposta)