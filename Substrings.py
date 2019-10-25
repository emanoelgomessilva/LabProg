#Sem nenhum laço
print("Sem nenhum laço:")
def SubstringRecursivo(nome, inicio, range):
    if range <= len(nome):
        print(nome[inicio:range])
    if range+1 <= len(nome):
        SubstringRecursivo(nome, inicio, range+1)
    elif inicio+1 <= len(nome):
        SubstringRecursivo(nome, inicio+1, inicio+1)

SubstringRecursivo("PAULA", 0, 0)

#Com um laço
print("Com um laço:")
def SubstringUmLaco(inicio,nome, range):
    if range <= len(nome):
        print(nome[inicio:range])
    if range+1 <= len(nome):
        SubstringUmLaco(inicio, nome, range+1)

nome = "PAULA"

for i in range(len(nome)):
    SubstringUmLaco(i, nome, i)

#Com dois laços
print("")
print("Com dois laços:")
for i in range(len(nome)+1):
    inicio = i
    for j in range(inicio, len(nome)+1):
        print(nome[inicio:j])