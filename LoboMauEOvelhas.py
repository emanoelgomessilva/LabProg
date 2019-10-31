dimensoes = input().split(" ")
resultadoCampo = [0,0]
linha = [0]* int(dimensoes[1])
campo = [linha] * int(dimensoes[0])
resultado = [0,0]

def mapeamento(i,j):
    if(campo[i][j] == "k"):
        resultadoCampo[0] = resultadoCampo[0]+1
    elif(campo[i][j] == "v"):
        resultadoCampo[1] = resultadoCampo[1]+1
    campo[i][j] = "c"
    if ((j + 1 < int(dimensoes[1]) - 1 and campo[i][j + 1] == ".") or
          (j + 1 <int(dimensoes[1]) - 1 and campo[i][j + 1] == "v") or
          (j + 1 < int(dimensoes[1]) - 1 and campo[i][j + 1] == "k")):
        mapeamento(i, j + 1)
    if((i-1>0 and campo[i-1][j] == ".") or
           (i-1>0 and campo[i-1][j] == "v") or
           (i-1>0 and campo[i-1][j] == "k")):
        mapeamento(i-1,j)
    if ((j - 1 > 0 and campo[i][j - 1] == ".") or
          (j - 1 > 0 and campo[i][j - 1] == "v") or
          (j - 1 > 0 and campo[i][j - 1] == "k")):
        mapeamento(i, j - 1)
    if ((i+1<int(dimensoes[0])-1 and campo[i+1][j]==".") or
          (i+1<int(dimensoes[0])-1 and campo[i+1][j]=="v") or
          (i+1 < int(dimensoes[0])-1 and campo[i+1][j] == "k")):
        mapeamento(i+1,j)

for i in range(int(dimensoes[0])):
    elementos = input()
    elementos = [elementos[i:i+1]for i in range(0,len(elementos),1)]
    campo[i] = elementos
    chances = 0

for i in range(int(dimensoes[0])):
    for j in range(int(dimensoes[1])):
        if(campo[i][j] == "." or campo[i][j] == "v" or campo[i][j] == "k"):
            mapeamento(i,j)
            if(resultadoCampo[1] >= resultadoCampo[0]):
                resultado[1] = resultado[1] + resultadoCampo[1]
            else:
                resultado[0] = resultado[0] + resultadoCampo[0]
        resultadoCampo = [0,0]

print(str(resultado[0])+" "+str(resultado[1]))