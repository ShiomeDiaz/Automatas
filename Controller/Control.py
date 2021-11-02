import json

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
        AutomatC = copy.deepcopy(self.automatas[0])

        #  alimentamos lista nodos
        for i in AutomatA.getListaNodoEstado():
            for j in AutomatB.getListaNodoEstado():
                listaNodos.append(i.getEstado() + j.getEstado())
        print(listaNodos, 'estados')


        # alimentar estado inicial

        for i in AutomatA.getEstadoInicial():
            for j in AutomatB.getEstadoInicial():
                estadoInicial.append(i+ j)
        print(estadoInicial, 'estados iniciales')

        for i in listaNodos:
            for j in AutomatA.getEstadosAceptacion():
                for m in AutomatB.getEstadosAceptacion():
                    if i[0] == j or i[1] == m:
                        estadoFinal.append(i[0]+i[1])
        print(estadoFinal, 'estados aceptacion')

        # alimentar lista alfabeto
        listalfa = []
        for i in AutomatA.getAlfabeto():
            for j in AutomatB.getAlfabeto():
                if i == j:
                    listalfa.append(i)
        print(listalfa)


        # re prueba
        listaSupersaya = []
        listaNodosAux = listaNodos
        for i in listaNodosAux:
            # print('Transicion', ' ', i[0], i[1])
            for j in AutomatA.getListaTran():
                for k in AutomatA.getAlfabeto():
                    if i[0] == j.getOrigen() and j.getOperacion() == k:
                        # me imprime que encontro la transiciond e A
                        #listaSupersaya.append([j.getOrigen(), j.getDestino(), k])
                        for m in AutomatB.getListaTran():
                            for n in AutomatB.getAlfabeto():
                                if i[1] == m.getOrigen() and m.getOperacion() == n and n ==k:
                                    # print(i[0] + i[1], '===>',j.getDestino()+m.getDestino(), k)
                                    listaSupersaya.append([i[0] + i[1],j.getDestino()+m.getDestino(), k])

        print(listaSupersaya)

        archivo = {"uno" :{  "Nodos": listaNodos, "Trans" : listaSupersaya, "Inicial" : estadoInicial, "Aceptacion" : estadoFinal, "Alfabeto" : listalfa }}
        with open('Union.json', 'w') as file:
            json.dump(archivo, file, indent=4)

        automataUno = Automata()
        automataUno.cargarRedInicialUNO("../Data/Union.json")
        return automataUno

    def Disyuncion(self):
        listaNodos = []
        estadoInicial = []
        estadoFinal = []
        AutomatA = copy.deepcopy(self.automatas[0])
        AutomatB = copy.deepcopy(self.automatas[1])
        AutomatC = copy.deepcopy(self.automatas[0])

        #  alimentamos lista nodos
        for i in AutomatA.getListaNodoEstado():
            for j in AutomatB.getListaNodoEstado():
                listaNodos.append(i.getEstado() + j.getEstado())
        print(listaNodos, 'estados')

        # alimentar estado inicial

        for i in AutomatA.getEstadoInicial():
            for j in AutomatB.getEstadoInicial():
                estadoInicial.append(i + j)
        print(estadoInicial, 'estados iniciales')

        # alimentar estados Aceptacion
        for i in AutomatA.getEstadosAceptacion():
            for j in AutomatB.getEstadosAceptacion():
                estadoFinal.append(i + j)
        print(estadoFinal, 'estados aceptacion')
        listalfa = []
        for i in AutomatA.getAlfabeto():
            for j in AutomatB.getAlfabeto():
                if i == j:
                    listalfa.append(i)
        print(listalfa)

        # re prueba
        listaSupersaya = []
        listaNodosAux = listaNodos
        for i in listaNodosAux:
            # print('Transicion', ' ', i[0], i[1])
            for j in AutomatA.getListaTran():
                for k in AutomatA.getAlfabeto():
                    if i[0] == j.getOrigen() and j.getOperacion() == k:
                        # me imprime que encontro la transiciond e A
                        # listaSupersaya.append([j.getOrigen(), j.getDestino(), k])
                        for m in AutomatB.getListaTran():
                            for n in AutomatB.getAlfabeto():
                                if i[1] == m.getOrigen() and m.getOperacion() == n and n == k:
                                    # print(i[0] + i[1], '===>',j.getDestino()+m.getDestino(), k)
                                    listaSupersaya.append([i[0] + i[1], j.getDestino() + m.getDestino(), k])

        print(listaSupersaya)

        archivo = {
            "uno": {"Nodos": listaNodos, "Trans": listaSupersaya, "Inicial": estadoInicial, "Aceptacion": estadoFinal,
                    "Alfabeto": listalfa}}
        with open('Disyuncion.json', 'w') as file:
            json.dump(archivo, file, indent=4)

        automataUno = Automata()
        automataUno.cargarRedInicialUNO("../Data/Disyuncion.json")
        return automataUno


