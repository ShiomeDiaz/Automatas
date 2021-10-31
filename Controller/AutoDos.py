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
        #print(origen, destino, operacion,'--> el careverga')
        #print(self.listaNodoEstado)
        #print(self.listaTran, 'Mp')
        for Transicion in self.listaTran:
            #print(Transicion.getOrigen())
            #print(Transicion.getOrigen(), '=',origen, '---', Transicion.getDestino(),'=', destino, Transicion.getOperacion())
            #print(Transicion.getOperacion())
            if Transicion.getOrigen() == origen and Transicion.getDestino() == destino:
                #print('gonorrea')
                return Transicion
        return None
    '''
    def imprimirNodoEstado(self):
        for nodoEstado in self.listaNodoEstado:
            print(nodoEstado.getEstado())

    '''
    '''
    def cargarRedInicial(self, ruta):
        with open(ruta) as contenido:
            redAcme = json.load(contenido)
        for nodos in redAcme["Cuevas"]:
            self.ingresarVertice(vertice)
        for arista in redAcme["Caminos"]:
            self.ingresarArista(arista[0], arista[1], arista[2])
        self.noDirigido(self.listaAristas)
    '''

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

    '''Creacion de metodos para operaciones,
    Para un solo grafo ---> Complemento, reverso y completar automata en caso de que este incompleto
    Para la pareja de grafos -->
    [A, B]U[C, D] ==> [AC, AD, BC, BD]
    '''

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



