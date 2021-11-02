import copy
from collections import deque

from Model.Transicion import Transicion
from Model.nodoEstado import nodoEstado
import json

# Trabajamos aqui pilas gonorreas

class Automata:
    def __init__(self):
        self.listaNodoEstado = []
        self.listaTran = []
        self.listaVisitados = []  # necesario?
        self.listaBloqueadas = [] # necesario?
        self.estadoInicial=[]
        self.estadosAceptacion=[]
        self.alfabeto = []

    def getListaNodoEstado(self):
        return self.listaNodoEstado

    def getListaTran(self):
        return self.listaTran
    def setListaTran(self, listaTran):
        self.listaTran = listaTran

    def getEstadoInicial(self):
        return self.estadoInicial

    def getEstadosAceptacion(self):
        return self.estadosAceptacion

    def setEstadoInicial(self, estadoInicial):
        self.estadoInicial.append(estadoInicial)

    def setEstadosAceptacion(self, estadosAceptacion):
        self.estadosAceptacion.append(estadosAceptacion)

    def getAlfabeto(self):
        return self.alfabeto
    def setAlfabeto(self, alfabeto):
        self.alfabeto.append(alfabeto)

    def getListaVisitados(self): # necesario?
        return self.listaVisitados

    def getListaBloqueadas(self): # necesario?
        return self.listaBloqueadas
# Contruccion logica

    def ingresarNodoEstado(self, estado):
        if self.verificarNodoEstado(estado) is None:
            self.listaNodoEstado.append(nodoEstado(estado))

    def verificarNodoEstado(self,estado):
        #print(estado)
        for nodoEstado in self.listaNodoEstado:
            if estado == nodoEstado.getEstado():
                return nodoEstado
        return None

    def completarAutomata(self):
        estados = []
        for i in self.listaNodoEstado:
            estados.append(i.getEstado())
        trans = []
        for i in self.listaTran:
            trans.append([i.getOrigen(), i.getDestino(), i.getOperacion()])
        sumidero = False
        copiaEstados = copy.deepcopy(estados)
        copiaTrans = copy.deepcopy(trans)

        for i in range(len(estados)):
            contadorTrans = 0
            valorTrans = []
            transSumidero = []
            for j in range(len(trans)):
                if estados[i] == trans[j][0]:
                    contadorTrans = contadorTrans + 1
                    valorTrans.append(trans[j][2])

            if contadorTrans != len(self.alfabeto):
                transSumidero = copy.deepcopy(self.alfabeto)
                for l in range(len(self.alfabeto)):
                    for m in range(len(valorTrans)):
                        if self.alfabeto[l] == valorTrans[m]:
                            transSumidero.pop(l)


                if sumidero == True:
                    for n in range(len(transSumidero)):
                        nuevaTrans = [estados[i], "sum", transSumidero[n]]
                        copiaTrans.append(nuevaTrans)

                if sumidero == False:
                    sumidero = True
                    copiaEstados.append("sum")
                    for n in range(len(transSumidero)):
                        nuevaTrans = [estados[i], "sum", transSumidero[n]]
                        copiaTrans.append(nuevaTrans)


        estados = copiaEstados
        trans = copiaTrans

        for o in range(len(estados)):
            if estados[o]=="sum":
                nodo=nodoEstado("sum")
                self.listaNodoEstado.append(nodo)

        self.listaTran=[]
        for p in range(len(trans)):
            o= trans[p][0]
            d= trans[p][1]
            op= trans[p][2]
            transicion= Transicion(o,d,op)
            self.listaTran.append(transicion)

    def obtenerOrigen(self, estado):
        for i in range(len(self.listaNodoEstado)):
            if estado == self.listaNodoEstado[i].getEstado():
                #print('obtengo el vertice :', self.listaVertices[i].getDato() )
                return self.listaNodoEstado[i]

    def ingresarTransicion(self, origen, destino, operacion):
        #print(origen, destino, operacion, '--> IngresarTrans')
        if self.verificarTransicion(origen, destino, operacion) == None:

            if self.verificarNodoEstado(origen) != None and self.verificarNodoEstado(destino) != None: #--> problema

                self.listaTran.append(Transicion(origen, destino, int(operacion)))
                #for i in self.listaTran:
                    #print(i.getOrigen(), i.getDestino(), '--> lista malparida')

                self.verificarNodoEstado(origen).getListaTransicion().append(destino)


    def verificarTransicion(self, origen, destino, operacion):
        for Transicion in self.listaTran:

            if Transicion.getOrigen() == origen and Transicion.getDestino() == destino:

                return Transicion
        return None

    def amplitud(self, estado):
        visitadosA = []
        cola = deque()
        nodoEstado = self.obtenerOrigen(estado)
        if nodoEstado != None:
            cola.append(nodoEstado)
            visitadosA.append(estado)
        while cola:
            elemento = cola.popleft()
            for Transicion in elemento.getListaTransicion():  # prueba no dirigida
                if Transicion not in visitadosA:
                    nodoEstado = self.obtenerOrigen(Transicion)
                    cola.append(nodoEstado)
                    visitadosA.append(Transicion)
        return visitadosA

    def cargarRedInicialUNO(self, ruta): # --> Metodo que se alimenta del json
        with open(ruta) as contenido:
            redAcme = json.load(contenido)

        for nodosuno in redAcme["uno"]["Nodos"]:
            self.ingresarNodoEstado(nodosuno)

        for transuno in redAcme["uno"]["Trans"]:
            #print('-->', transuno[2])
            #print(transuno[0], transuno[1], transuno[2], '--> el for')
            self.ingresarTransicion(transuno[0], transuno[1], transuno[2])


        for nodosuno in redAcme["uno"]["Inicial"]:
            self.setEstadoInicial(nodosuno)
            #print(self.getEstadoInicial(), 'Inicial')

        for nodosuno in redAcme["uno"]["Aceptacion"]:
            self.setEstadosAceptacion(nodosuno)
            #print(self.getEstadoInicial(), 'Final')

        for nodosuno in redAcme["uno"]["Alfabeto"]:
            self.setAlfabeto(nodosuno)

    def cargarRedInicialDOS(self, ruta): # --> Metodo que se alimenta del json
        with open(ruta) as contenido:
            redAcme = json.load(contenido)

        for nodosdos in redAcme["dos"]["Nodos"]:
            self.ingresarNodoEstado(nodosdos)

        for transdos in redAcme["dos"]["Trans"]:
            #print('-->', transuno[2])
            #print(transuno[0], transuno[1], transuno[2], '--> el for')
            self.ingresarTransicion(transdos[0], transdos[1], transdos[2])

        for nodosdos in redAcme["dos"]["Inicial"]:
            self.setEstadoInicial(nodosdos)
            #print(self.getEstadoInicial(), 'Inicial')

        for nodosdos in redAcme["dos"]["Aceptacion"]:
            self.setEstadosAceptacion(nodosdos)

        for nodosdos in redAcme["dos"]["Alfabeto"]:
            self.setAlfabeto(nodosdos)



