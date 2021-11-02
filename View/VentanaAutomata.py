# -*- coding: utf-8 -*-

import graphviz as gv

import sys
import pygame
from pygame.locals import *

import networkx as nx



def dibujarAutomata(alfabeto, estados, inicio, trans, final):
    g = gv.Digraph(format='png')
    g.graph_attr['rankdir'] = 'LR'
    g.node('ini', shape="point")
    for e in estados:
        if e in final:
            g.node(e, shape="doublecircle")
        else:
            g.node(e)

        if e in inicio:
            g.edge('ini', e)

    for t in trans:
        if t[2] not in alfabeto:
            return 0
        g.edge(t[0], t[1], label=str(t[2]))

    g.render(view=False)
    return 2


class VentanaGrafico:
    def __init__(self, alf, inicial, aceptacion, estados, trans):
        # self.cursor = Cursor()
        self.G = nx.Graph()
        self.inicial = inicial
        self.aceptacion = aceptacion
        # self.imagen1 = pygame.image.load("boton1.png")
        self.alf = alf
        self.estados = estados
        self.trans = trans
        # self.recorridoBctk = []

    def iniciarVentana(self):
        pygame.init()
        ventana = pygame.display.set_mode((1000, 650))
        pygame.display.set_caption("Automata")
        colorFondo = (250, 250, 250)
        while True:
            ventana.fill(colorFondo)
            for evento in pygame.event.get():

                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # self.cursor.update()
            self.textoInformacion(ventana)
            self.graficarAutomata(ventana)
            pygame.display.update()



    def textoInformacion(self, ventana):

        textoEstInicial = "El estado inicial es: " + str(self.inicial)
        textoEstAceptacion = "El estado de aceptación es: " + str(self.aceptacion)
        miFuente = pygame.font.SysFont("Arial", 20)
        textoEI = miFuente.render(textoEstInicial, 1, (0, 0, 0))
        ventana.blit(textoEI, (20, 510))
        textoEA = miFuente.render(textoEstAceptacion, 1, (0, 0, 0))
        ventana.blit(textoEA, (20, 535))

    def graficarAutomata(self, ventana):

        imagenAutomata = pygame.image.load("Digraph.gv.png")
        posX, posY = 50, 20
        imagenAutomata = pygame.transform.smoothscale(imagenAutomata, (900, 470))
        ventana.blit(imagenAutomata, (posX, posY))

