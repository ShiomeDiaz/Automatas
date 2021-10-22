from Model.nodoEstado import nodoEstado
from Model.Transicion import Transicion
from graphviz import Digraph
import graphviz as gv
import networkx as nx
import os, sys



class Automata:
    def __init__(self):
        self.transicionLista = []
        self.nodoEstadoLista = []

        # get

    def getTranlista(self):
        return self.transicionLista
    def getNodoLista(self):
        return self.nodoEstadoLista



