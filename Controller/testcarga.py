
from Model.Transicion import Transicion
from Model.nodoEstado import nodoEstado
from Data.cargaDatos import *

cargaNodosuno= carga()[0]
cargaTransuno= carga()[1]
cargaNodosdos= carga()[2]
cargaTransdos= carga()[3]
print("--Nodo Uno__")
print(cargaNodosuno)
print(cargaTransuno)
print("--Nodo Dos__")
print(cargaNodosdos)
print(cargaTransdos)

# Metodo de carga que esta en la estructura del grafo se debe modificar para la entrada de dos grafos

'''
    def cargarRedInicial(self, ruta):
        with open(ruta) as contenido:
            redAcme = json.load(contenido)
        for vertice in redAcme["Cuevas"]:
            self.ingresarVertice(vertice)
        for arista in redAcme["Caminos"]:
            self.ingresarArista(arista[0], arista[1], arista[2])
        self.noDirigido(self.listaAristas)
'''