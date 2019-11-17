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

    def buscarPosicaoPacienteGravidade(self, paciente, noReferencia):
        i = self.buscar(noReferencia.getDado())
        while (i is not None) and (i.getDado().getGravidade() > paciente.getGravidade()) and (i.getDado().getPlano() == paciente.getPlano()):
            i = i.getProx()
        if (i is not None) and (i.getDado().getGravidade == paciente.getGravidade()):
            i = self.buscarPosicaoPacienteNome()
        return i  # nao achou

    def buscarPosicaoPacienteNome(self, paciente, noReferencia):
        i = self.buscar(noReferencia.getDado())
        while (i is not None) and (i.getDado().getNome() > paciente.getNome()  and (i.getDado().getGravidade() == paciente.getGravidade())):
            if i.getDado().getNome < paciente.getNome():
                return i
            i = i.getProx()
        return i  # nao achou

    def buscarPosicaoPacientePlano(self, paciente):
        i = self._inicio
        while (i is not None) and (i.getDado().getPlano() > paciente.getPlano()):
            i = i.getProx()

        if(i is not None):
            if (i.getDado().getPlano() == paciente.getPlano()):
                i = self.buscarPosicaoPacienteGravidade(paciente, i);

        return i

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

    def inserirNoFim(self, dado):
        novono = No(dado)
        if self.isVazia():
            self._inicio = novono
            self._fim = self._inicio
        else:
            novono.setAnt(self._fim)
            self._fim.setProx(novono)
            self._fim = novono

    def inserirPaciente(self, paciente):
        novoPaciente = No(paciente)
        if(self.isVazia()):
            noReferencia = None
        else:
            noReferencia = self.buscarPosicaoPacientePlano(paciente)
        if ((noReferencia is None) or (self._inicio is self._fim)):
            self.inserirNoFim(paciente)
        elif(noReferencia is self._inicio):
            self.inserirNoInicio(paciente)
        else:
            if(noReferencia.getAnt() is not None):
                noReferencia.getAnt().setProx(novoPaciente)
                novoPaciente.setProx(noReferencia)
                novoPaciente.setAnt(noReferencia.getAnt())
                noReferencia.setAnt(novoPaciente)
            else:
                novoPaciente.setProx(noReferencia)
                novoPaciente.setAnt(noReferencia.getAnt())
                noReferencia.setAnt(novoPaciente)
        if((noReferencia is not None) and (noReferencia.getDado().getPlano() == novoPaciente.getDado().getPlano())):
            if (noReferencia.getDado().getGravidade() == novoPaciente.getDado().getGravidade()):
                if (noReferencia.getDado().getNome() < novoPaciente.getDado().getNome()):
                    novoPaciente.setProx(noReferencia.getProx())
                    noReferencia.setProx(novoPaciente)
                    verificaSeExisteAnterior = noReferencia.getAnt()
                    if(verificaSeExisteAnterior is not None):
                        if(verificaSeExisteAnterior.getAnt() is not None):
                            noReferencia.getAnt().getAnt().setProx(noReferencia)
                    else:
                        self.setInicio(noReferencia)
                    novoPaciente.setAnt(noReferencia)
                    verificaSeExisteProximo = novoPaciente.getProx()
                    if(verificaSeExisteProximo is not None):
                        if (verificaSeExisteProximo.getProx() is not None):
                            novoPaciente.getProx().getProx().setAnt(novoPaciente)
                    else:
                        self.setFim(novoPaciente)


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
            s += str(i.getDado().getNome()) + "|"
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

class Paciente:
    def __init__(self, nome, plano, gravidade):
        self._nome = nome
        self._plano = plano
        self._gravidade = gravidade

    def getNome(self):
        return self._nome

    def getPlano(self):
        return self._plano

    def getGravidade(self):
        return self._gravidade

    def setNome(self, nome):
        self._nome = nome

    def setProx(self, plano):
        self._plano = plano

    def setAnt(self, gravidade):
        self._gravidade = gravidade

numeroPacientes = int(input())
listaPacientes = ListaEncadeada()
for i in range(numeroPacientes):
    paciente = input().split(" ")
    nome = paciente[0]
    gravidade = int(paciente[2])
    plano = 0
    if(paciente[1] == "premium"):
        plano = 6
    elif (paciente[1] == "diamante"):
        plano = 5
    elif (paciente[1] == "ouro"):
        plano = 4
    elif (paciente[1] == "prata"):
        plano = 3
    elif (paciente[1] == "bronze"):
        plano = 2
    elif (paciente[1] == "resto"):
        plano = 1
    novoPaciente = Paciente(nome,plano,gravidade)
    listaPacientes.inserirPaciente(novoPaciente)

p = listaPacientes.getInicio()

while(p is not None):
    print(p.getDado().getNome())
    p = p.getProx()

