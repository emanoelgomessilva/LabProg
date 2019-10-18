n = input()
#Lista que guarda os retangulos
retangulos = input().split(" ")
#Lista que guarda os retangulos com menor altura
vales = []
#Variável que guarda a maior quantidade de cortes possível
maiorDivisao = -1

#Se o primeiro retângulo da sequência for menor do que o seu sucessor, ele é um vale
if(int(retangulos[0])<int(retangulos[1])):
    vales.append(int(retangulos[0]))

#Se o ultimo retângulo da sequência for menor do que o seu antecessor, ele é um vale
if(int(retangulos[int(n)-1])<int(retangulos[int(n)-2])):
    vales.append(int(retangulos[int(n)-1]))

#Para cada retangulo da sequencia, se o seu antecessor e sucessor forem maiores que ele, ele será um vale
for i in range(len(retangulos)-1):
    if(i-1 >= 0 and i+1<= len(retangulos)-1):
        if(int(retangulos[i-1])>int(retangulos[i]) and int(retangulos[i+1])>int(retangulos[i])):
            vales.append(int(retangulos[i]))
#
for vale in vales:
    #Inicialmente haverá um pedaço.
    divisao = 1
    #É assumido que se o primeiro retangulo da sequencia for maior que o vale testado, já será acrescentado,
    #um novo pedaço à divisão.
    if (int(retangulos[0])>vale):
        divisao+=1
    #Os retângulos são percorridos. Se um retangulo for menor ou igual ao vale percorrido, será contabilizado
    #um novo pedaço à divisão
    for i in range(len(retangulos)-1):
        if(int(retangulos[i])<=vale and int(retangulos[i-1])>vale):
            divisao+=1
    #Se a divisão resultante for maior ao valor corrente de maiorDivisão, ela será a maior divisão
    if(divisao>maiorDivisao):
        maiorDivisao = divisao

print(maiorDivisao)