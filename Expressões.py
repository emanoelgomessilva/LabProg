class No:
    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None
        self.__ant = None

    def getDado(self):
        return self.__dado

    def getProx(self):
        return self.__prox

    def getAnt(self):
        return self.__ant

    def setDado(self, dado):
        self.__dado = dado

    def setProx(self, prox):
        self.__prox = prox

    def setAnt(self, ant):
        self.__ant = ant


class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._fim = None

    def getInicio(self):
        return self._inicio

    def getFim(self):
        return self._fim

    def setInicio(self, inicio):
        self._inicio = inicio

    def setFim(self, fim):
        self._fim = fim

    def buscar(self, dado):
        i = self._inicio
        while i is not None:
            if i.getDado() == dado:
                return i
            i = i.getProx()
        return i #nao achou

    def isVazia(self):
        return self._inicio is None

    def inserirNoInicio(self, dado):
        novono = No(dado)
        if self.isVazia():
            self._inicio = novono
            self._fim = self._inicio
        else:
            novono.setProx(self._inicio)
            self._inicio.setAnt(novono)
            self._inicio = novono

    def removerDado(self, dado):
        noRemovido = self.buscar(dado) # ponteiro para o resultado da busca
        # o elemento foi encontrado
        if noRemovido is not None:
            prox = noRemovido.getProx()
            ant = noRemovido.getAnt()
            # a lista tinha um elemento
            if self._inicio is self._fim:
                self._inicio = self._fim = None
            # o elemento é o início da lista
            elif noRemovido is self._inicio:
                prox.setAnt(None)
                self._inicio = prox
            # o elemento é o fim da lista
            elif noRemovido is self._fim:
                ant.setProx(None)
                self._fim = ant
            # o elemento está no meio da lista
            else:
                ant.setProx(prox)
                prox.setAnt(ant)
        return noRemovido

    def removerDoInicio(self):
        if not self.isVazia():
            if self._inicio is not self._fim:
                self._inicio.getProx().setAnt(None)
                self._inicio = self._inicio.getProx()
            else:
                self._inicio = self._fim = None

    def removerDoFim(self):
        i = self._fim
        if not self.isVazia():
            if self._inicio is not self._fim:
                self._fim.getAnt().setProx(None)
                self._fim = self._fim.getAnt()
            else:
                self._inicio = self._fim = None
        return i

    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += str(i.getDado()) + "|"
            i = i.getProx()
        if s is "":
            s = "Lista vazia coitada"
        return s


class Fila(ListaEncadeada):
    '''
    Estou apenas renomeando os métodos
    de ListaEncadeada para que o usuário da Fila
    apenas tenha que inserir e remover sem se preocupar
    com a ponta que está sendo alterada
    A palavra chave super é um referência para a
    super classe, neste caso, ListaEncadeada
    '''

    def inserir(self, dado):
        super().inserirNoInicio(dado)

    def remover(self):
        return super().removerDoFim()

    '''
    Vamos especializar a impressão de fila
    e deixá-la mais legível do que a de lista
    '''
    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += str(i.getDado())
            i = i.getProx()
            if i is not None:
                s += "->"
        if s is "":
            return "É bom ficar sem Fila"
        return "último a chegar-> "+s+"->primeiro a chegar"



instancias = int(input())

for i in range(instancias):
    instancia = input()
    semPar = 0
    pilhaCaracteresAbertura = ListaEncadeada()
    for i in range(len(instancia)):
        if((instancia[i] is "[") or (instancia[i] is "{") or (instancia[i] is "(")):
            pilhaCaracteresAbertura.inserirNoInicio(instancia[i])
        elif((instancia[i] is "]") or (instancia[i] is ")") or (instancia[i] is "}")):
            if(pilhaCaracteresAbertura.isVazia()):
                semPar+=1
                break;
            elif(((instancia[i] is "]") and (pilhaCaracteresAbertura.getInicio().getDado() is "["))):
                pilhaCaracteresAbertura.removerDoInicio()
            elif(((instancia[i] is "]") and (pilhaCaracteresAbertura.getInicio().getDado() is not "["))):
                semPar += 1
            if (((instancia[i] is "}") and (pilhaCaracteresAbertura.getInicio().getDado() is "{"))):
                pilhaCaracteresAbertura.removerDoInicio()
            elif (((instancia[i] is "}") and (pilhaCaracteresAbertura.getInicio().getDado() is not "{"))):
                semPar += 1
            if (((instancia[i] is ")") and (pilhaCaracteresAbertura.getInicio().getDado() is "("))):
                pilhaCaracteresAbertura.removerDoInicio()
            elif (((instancia[i] is ")") and (pilhaCaracteresAbertura.getInicio().getDado()) is not "(")):
                semPar += 1
    if(pilhaCaracteresAbertura.isVazia() and semPar is 0):
        print("S")
    else:
        print("N")