n = input()
retangulos = input().split(" ")
vales = []
maiorDivisao = -1

if(int(retangulos[0])<int(retangulos[1])):
    vales.append(int(retangulos[0]))

if(int(retangulos[int(n)-1])<int(retangulos[int(n)-2])):
    vales.append(int(retangulos[int(n)-1]))

for i in range(len(retangulos)-1):
    if(i-1 >= 0 and i+1<= len(retangulos)-1):
        if(int(retangulos[i-1])>int(retangulos[i]) and int(retangulos[i+1])>int(retangulos[i])):
            vales.append(int(retangulos[i]))

for vale in vales:
    divisao = 1
    if (int(retangulos[0])>vale):
        divisao+=1
    for i in range(len(retangulos)-1):
        if(int(retangulos[i])<=vale and int(retangulos[i-1])>vale):
            divisao+=1
    if(divisao>maiorDivisao):
        maiorDivisao = divisao

print(maiorDivisao)