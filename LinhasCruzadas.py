N = input()
pregos = input().split(" ")
numeroCruzamentos = 0

for i in range(int(N)):
    for j in range(i, int(N)):
        if(int(pregos[i]) > int(pregos[j])):
            numeroCruzamentos = numeroCruzamentos +1

print(numeroCruzamentos)