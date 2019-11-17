def Max(a , b):
    if a>b:
        return a
    else:
        return b

info = input().split(" ")

numeroItens = int(info[0])
capacidade = int(info[1])

tabela = []

for i in range(numeroItens + 1):
    linha = []
    for j in range(capacidade + 1):
        linha.append(0)
    tabela.append(linha[:])

valores = []
pesos = []

for i in range(numeroItens):
    item = input().split(" ")
    valores.append(item[1])
    pesos.append(item[0])

for i in range(1, numeroItens+1):
    for j in range(1, capacidade+1):
        if int(pesos[i-1]) <= j:
            tabela[i][j] = Max(int(tabela[i-1][j]) , int(tabela[i-1][j-int(pesos[i-1])]+ int(valores[i-1])))

print(tabela[numeroItens][capacidade])


