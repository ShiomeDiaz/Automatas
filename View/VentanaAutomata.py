# -*- coding: utf-8 -*-

import graphviz as gv
from graphviz import Digraph
import os,sys
import pygame
from pygame.locals import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget, QPushButton, QMessageBox
from PyQt5 import uic
import networkx as nx


# Todos los parámetros son listas o tuplas
# donde:
#  * alfabeto:  es el alfabeto aceptado por el
#               autómata.
#  * estados:   es una lista de estados aceptados
#               por el autómata.
#  * inicio:    Son los estados de inicio del fsm.
#  * trans:     Es una tupla de funciones de transición
#               con tres elementos que son: (a,b,c) donde
#               (a,b) son los estados de partida y llegada;
#               mientras que c es la letra que acepta.
#  * final      Son los estados finales del autómata.

def dibujarAutomata(alfabeto, estados, inicio, trans, final, palabra):
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

    for p in palabra:
        if p not in alfabeto:
            return 1

    g.render(view=False)
    return 2


class VentanaGrafico:
    def __init__(self, alf, inicial, aceptacion, estados, trans, palabra):
        self.cursor = Cursor()
        self.G = nx.Graph()
        self.inicial = inicial
        self.aceptacion = aceptacion
        self.palabra = palabra
        self.imagen1 = pygame.image.load("boton1.png")
        self.alf = alf
        self.estados = estados
        self.trans = trans
        self.recorridoBctk = []

    def iniciarVentana(self):
        pygame.init()
        ventana = pygame.display.set_mode((1300, 650))
        pygame.display.set_caption("Automata")
        colorFondo = (250, 250, 250)
        botones = self.botones()
        while True:
            ventana.fill(colorFondo)
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.cursor.colliderect(botones[0].rect):
                        self.recorerPalabra(ventana)

                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

            for b in botones:
                b.update(ventana, self.cursor)
            self.cursor.update()
            self.textoInformacion(ventana)
            self.graficarAutomata(ventana)
            pygame.display.update()

    def recorerPalabra(self, ventana):
        g = gv.Digraph(format='png')
        g.graph_attr['rankdir'] = 'LR'
        g.node('ini', shape="point")

        for e in self.estados:
            if e in self.aceptacion:
                g.node(e, shape="doublecircle")
            else:
                g.node(e)
            if e in self.inicial:
                g.edge('ini', e)
        for t in trans:
            g.edge(t[0], t[1], label=str(t[2]))

        x = self.inicial.copy()
        self.bckt(x, [["0"]])
        posicion = self.recorridoBctk
        if posicion != None and posicion != []:
            for p in posicion:
                self.textoRecorrido(ventana)
                g.node(p, style='filled', color='red')
                g.render(view=False)
                self.graficarAutomata(ventana)
                pygame.display.update()
                pygame.time.wait(1200)
                g.node(p, style="", color="black")
                g.render(view=False)
                self.graficarAutomata(ventana)
                pygame.display.update()
                pygame.time.wait(500)

        else:
            self.PNoAceptada()

        self.recorridoBctk = []

    def bckt(self, candidato, solucion):
        print("prueba 165 " + str(len(candidato)))
        opcion = []
        print("prueba 167 " + str(candidato) + " " + str(solucion))
        if len(candidato) <= (len(self.palabra) + 1):
            y = solucion[len(solucion) - 1]
            print("prueba 170 " + str(len(candidato)))

            if y[len(y) - 1] in self.aceptacion and len(y) == (len(self.palabra) + 1):
                for e in y:
                    self.recorridoBctk.append(e)
                return
            else:
                if solucion[0] == ["0"]:
                    solucion.pop()

                x = candidato.copy()
                solucion.append(x)
                print("prueba 182 " + str(solucion))

                uActual = x[len(x) - 1]
                print("prueba 185 " + str(uActual))
                if len(candidato) <= len(self.palabra):

                    for i, t in enumerate(self.trans):
                        if t[0] == uActual and t[2] == self.palabra[len(candidato) - 1]:
                            opcion.insert(i, t[1])
                        print("prueba 189 " + str(opcion))

                    for o in opcion:
                        x.append(o)
                        print("prueba 193 " + str(x))
                        self.bckt(x, solucion)
                        x.pop()

    def textoRecorrido(self, ventana):

        textoEstInicial = "El recorrido es: " + str(self.recorridoBctk)
        textoPalabra = "La palabra a seguir es: " + str(self.palabra)
        miFuente = pygame.font.SysFont("Arial", 20)
        textoEI = miFuente.render(textoEstInicial, 1, (0, 0, 0))
        ventana.blit(textoEI, (20, 510))
        textoPA = miFuente.render(textoPalabra, 1, (0, 0, 0))
        ventana.blit(textoPA, (20, 564))

    def textoInformacion(self, ventana):

        textoEstInicial = "El estado inicial es: " + str(self.inicial)
        textoEstAceptacion = "El estado de aceptación es: " + str(self.aceptacion)
        textoPalabra = "La palabra a seguir es: " + str(self.palabra)
        miFuente = pygame.font.SysFont("Arial", 20)
        textoEI = miFuente.render(textoEstInicial, 1, (0, 0, 0))
        ventana.blit(textoEI, (20, 510))
        textoEA = miFuente.render(textoEstAceptacion, 1, (0, 0, 0))
        ventana.blit(textoEA, (20, 535))
        textoPA = miFuente.render(textoPalabra, 1, (0, 0, 0))
        ventana.blit(textoPA, (20, 564))

    def graficarAutomata(self, ventana):

        imagenAutomata = pygame.image.load("Digraph.gv.png")
        posX, posY = 50, 20
        imagenAutomata = pygame.transform.smoothscale(imagenAutomata, (900, 470))
        ventana.blit(imagenAutomata, (posX, posY))

    def botones(self):
        botones = []
        y = 20
        boton1 = Boton(self.imagen1, y)
        botones.append(boton1)
        return botones

    def EAlfabeto(self):
        app = QApplication(sys.argv)
        _ventana = VentanaEAlfabeto()
        _ventana.show()
        app.exec_()

    def EPalabra(self):
        app = QApplication(sys.argv)
        _ventana = VentanaEPalabra()
        _ventana.show()
        app.exec_()

    def PNoAceptada(self):
        app = QApplication(sys.argv)
        _ventana = VentanaPNoAceptada()
        _ventana.show()
        app.exec_()


class VentanaEAlfabeto(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("VentanaEAlfabeto.ui", self)
        self.bAceptar.clicked.connect(self.Cancelar)

    def Cancelar(self, QEvent):
        self.close()


class VentanaEPalabra(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("VentanaEPalabra.ui", self)
        self.bAceptar.clicked.connect(self.Cancelar)

    def Cancelar(self, QEvent):
        self.close()


class VentanaPNoAceptada(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("VentanaPNoAceptada.ui", self)
        self.bAceptar.clicked.connect(self.Cancelar)

    def Cancelar(self, QEvent):
        self.close()


class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen, y, x=1000):
        self.y = y
        self.imagenBoton = imagen
        self.rect = self.imagenBoton.get_rect()
        self.rect.left, self.rect.top = (x, y)

    def update(self, ventana, cursor):
        ventana.blit(self.imagenBoton, self.rect)


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()


if __name__ == '__main__':
    estados = ["A", "B", "C", "E", "F"]
    trans = [("A", "B", 1), ("A", "A", 0), ("A", "E", 0), ("E", "D", 1), ("F", "F", 1), ("D", "C", 1), ("B", "A", 0),
             ("E", "C", 0), ("F", "D", 0), ("B", "B", 1)]
    inicial = ["A"]
    alf = [0, 1]
    aceptacion = ("C")
    palabra = [1, 1, 1, 1, 0, 0, 0]

    x = dibujarAutomata(alf, estados, inicial, trans, aceptacion, palabra)
    v = VentanaGrafico(alf, inicial, aceptacion, estados, trans, palabra)
    if x == 2:
        v.iniciarVentana()
    elif x == 1:
        v.EPalabra()
    else:
        v.EAlfabeto()