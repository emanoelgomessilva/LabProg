linhaColuna = input().split(" ")
navios = []
contapartes = 0
tag = 0
tags = []
mar = []
saida = 0


def lernavio(linha, coluna):
    mar[linha][coluna] = str(tag)
    if coluna + 1 <= int(linhaColuna[1]) - 1 and mar[linha][coluna + 1] == "#":
        lernavio(linha, coluna + 1)
    if coluna - 1 >= 0 and mar[linha][coluna - 1] == "#":
        lernavio(linha, coluna - 1)
    if linha + 1 <= int(linhaColuna[0]) - 1 and mar[linha + 1][coluna] == "#":
        lernavio(linha + 1, coluna)
    if linha - 1 >= 0 and mar[linha - 1][coluna] == "#":
        lernavio(linha - 1, coluna)


for i in range(int(linhaColuna[0])):
    pedaco = input()
    pedaco1 = [pedaco[i:i + 1] for i in range(0, len(pedaco), 1)];
    mar.append(pedaco1)

numerotiros = int(input());

for i in range(int(linhaColuna[0])):
    for j in range(int(linhaColuna[1])):
        if mar[i][j] == "#":
            navios.append(contapartes)
            lernavio(i, j)
            tag += 1

for i in range(int(linhaColuna[0])):
    for j in range(int(linhaColuna[1])):
        for k in range(len(navios)):
            if mar[i][j] == str(k):
                navios[k] += 1

for i in range(numerotiros):
    tiro = input().split(" ")
    elemento = mar[int(tiro[0]) - 1][int(tiro[1]) - 1]
    if elemento != ".":
        navios[int(elemento)] = navios[int(elemento)] - 1

for i in navios:
    if i == 0:
        saida += 1

print(saida)