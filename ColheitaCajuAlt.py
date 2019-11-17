areas = input().split(" ")
maiorColheita = 0
plantacao = []
linhaslimite = (int(areas[0]) - int(areas[2]))+1
colunaslimite = (int(areas[1])-int(areas[3]))+1

for i in range(int(areas[0])):
    linha = input().split(" ");
    if linha.__contains__("") == False:
      plantacao.append(linha)

for i in range(linhaslimite):
  for j in range(colunaslimite):
    colheita = 0
    for k in range(int(areas[2])):
      for l in range(int(areas[3])):
          if((i+k < int(areas[0])-1) and (j+l< int(areas[1])-1)):
            colheita = colheita + int(plantacao[i+k][j+l])
    if colheita > maiorColheita:
      maiorColheita = colheita

print(maiorColheita)