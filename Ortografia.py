entrada = input().split(" ")
tamanhoDicionario = int(entrada[0])
quantidadePalavras = int(entrada[1])
dicionario = []
palavras = []
sugestoes = []
similaridade = 0
mudancas = 0

for i in range(tamanhoDicionario):
    palavra = input()
    dicionario.append(palavra)

for i in range(quantidadePalavras):
    palavra = input()
    palavras.append(palavra)

for palavra in palavras:
    for palavraDicionario in dicionario:
        tabelaCompara = []
        for i in range(len(palavra) + 1):
            linha = []
            for j in range(len(palavraDicionario) + 1):
                linha.append(0)
            tabelaCompara.append(linha[:])
        achou = False
        for i in range(1,len(palavra) + 1):
            achou = False
            for j in range(1, len(palavraDicionario) + 1):
                if palavra[i-1] == palavraDicionario[j-1] and achou == False and tabelaCompara[0][j] != "x":
                    tabelaCompara[i][j] = 1
                    tabelaCompara[0][j] = "x"
                    similaridade += 1
                    achou = True
        if len(palavra) < len(palavraDicionario) or len(palavra) == len(palavraDicionario):
            mudancas = len(palavraDicionario) - similaridade
        if len(palavra) > len(palavraDicionario):
            mudancas = len(palavra) - similaridade
        similaridade = 0
        if mudancas <=2:
            sugestoes.append(palavraDicionario)
        mudancas = 0
    print(*sugestoes, sep= " ")
    sugestoes = []

