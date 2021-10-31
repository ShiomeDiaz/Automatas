from Controller.AutoDos import Automata
import copy

class Control:

    automatas=[]

    def __init__(self, automatas):
        self.automatas = automatas



    # Metodo que devuelve el complemento de un automata
    def complemento(self,nAutomata):

        automataComplemento = copy.deepcopy(self.automatas[nAutomata])
        aceptacion= copy.deepcopy(automataComplemento.estadosAceptacion)

        for estado in automataComplemento.getListaNodoEstado():
            automataComplemento.estadosAceptacion.append(estado.getEstado())

        for i in range(len(aceptacion)):
            reinicio = True
            while reinicio:
                reinicio = False
                for j in range(len(automataComplemento.estadosAceptacion)):
                    if aceptacion[i] == automataComplemento.estadosAceptacion[j]:
                        automataComplemento.estadosAceptacion.pop(j)
                        reinicio = True
                        break
        return automataComplemento

    # Union

    def Union(self):
        listaNodos = []
        estadoInicial = []
        estadoFinal = []
        AutomatA = copy.deepcopy(self.automatas[0])
        AutomatB = copy.deepcopy(self.automatas[1])

        #  alimentamos lista nodos
        for i in AutomatA.getListaNodoEstado():
            for j in AutomatB.getListaNodoEstado():
                listaNodos.append(i.getEstado() + j.getEstado())
        # print(listaNodos, 'estados')


        # alimentar estado inicial

        for i in AutomatA.getEstadoInicial():
            for j in AutomatB.getEstadoInicial():
                estadoInicial.append(i+ j)
        # print(estadoInicial, 'estados iniciales')

        # alimentar estados Aceptacion
        for i in AutomatA.getEstadosAceptacion():
            for j in AutomatB.getEstadosAceptacion():
                estadoFinal.append(i+ j)
        # print(estadoFinal, 'estados aceptacion')


        # alimentamos lista transiciones

        # transicion = []
        # for i in AutomatA.getListaTran():
        #     transicion.append(i.getOrigen())
        # #print(transicion)
        #
        # #print(AutomatA.getAlfabeto())