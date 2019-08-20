#Para a resolução do problema, foi utilizada uma pilha de instruções para o robô, se um f é lido, é incluído na pilha,
#se um t é lido, um f é desempilhado. Ao final da execução a distância será o tamanho da pilha
entrada = input()
pilha = []
instrucoes = [entrada[i:i + 1] for i in range(0, len(entrada), 1)]
for i in instrucoes:
    if(i == "F"):
        pilha.append(i)
    elif(i == "T" and (len(pilha) is not 0)):
        pilha.pop()
print(len(pilha))
