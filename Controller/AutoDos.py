from collections import deque

from Model.Transicion import Transicion
from Model.nodoEstado import nodoEstado
import json

# Trabajamos aqui pilas gonorreas

class Automata:
    def __init__(self):
        self.listaNodoEstado = []
        self.listaTran= []
        self.listaVisitados = []  # necesario?
        self.listaBloqueadas = [] # necesario?
        self.estadoInicial=[]
        self.estadosAceptacion=[]

    def getListaNodoEstado(self):
        return self.listaNodoEstado

    def getListaTran(self):
        return self.listaTran

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
        print(origen, destino, operacion, '--> IngresarTrans')
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
    def recorrido(self, lista): # ---> metodo de recorrido mediante la quintupla
        lista
    def cargarRedInicial(self, ruta):
        with open(ruta) as contenido:
            redAcme = json.load(contenido)
        for nodosuno in redAcme["uno"]["Nodos"]:
            self.ingresarNodoEstado(nodosuno)
        for transuno in redAcme["uno"]["Trans"]:
            #print('-->', transuno[2])
            #print(transuno[0], transuno[1], transuno[2], '--> el for')
            self.ingresarTransicion(transuno[0], transuno[1], transuno[2])
        #for nodosdos in redAcme["dos"]["Nodos"]:
            #self.ingresarNodoEstado(nodosdos)
        #for transdos in redAcme["dos"]["Trans"]:
            #self.ingresarTransicion(transdos[0], transdos[1], transdos[2])

    # Metodo que devuelve el complemento de un automata
    def complemento(self):
        listaComplemento=[]
        for i in range(len(self.listaNodoEstado)):
            listaComplemento.insert(i,self.listaNodoEstado)

        for estado in self.listaComplemento:

            if estado.estadoAceptacion==False:
                estado.estadoAceptacion=True
            elif estado.estadoAceptacion==True:
                estado.estadoAceptacion = False
        return listaComplemento

