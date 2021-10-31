# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyui.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from View import VentanaAutomata
from Controller.AutoDos import Automata
from Controller.Control import Control

from View.VentanaAutomata import VentanaGrafico, dibujarAutomata


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, automatauno, automatados):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(417, 447)
        MainWindow.setMaximumSize(417, 447)
        #MainWindow.resize(417, 447)
        self.automatauno = automatauno
        self.automatados = automatados
        self.listautomata = [automatauno, automatados]
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("\n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:0.823864 rgba(84, 19, 213, 255), stop:1 rgba(23, 138, 255, 228));\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 30, 391, 121))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap('./icono.png'))
        #self.label.setPixmap(QtGui.QPixmap("C:/Users/Shio/PycharmProjects/Automatas/View/NuevaGrafica/icono.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:1 rgba(62, 62, 62, 255));\n"
"\n"
"border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:1 rgba(62, 62, 62, 255));\n"
"\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:1 rgba(62, 62, 62, 255));\n"
"\n"
"border-radius:20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:1 rgba(62, 62, 62, 255));\n"
"\n"
"border-radius:20px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 280, 75, 23))
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:1 rgba(62, 62, 62, 255));\n"
"\n"
"border-radius:20px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 310, 75, 23))
        self.pushButton_6.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:1, y2:0, stop:1 rgba(62, 62, 62, 255));\n"
"\n"
"border-radius:20px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.onPushButtonCLicked)
        self.pushButton_2.clicked.connect(self.onPushButtonCLicked2)
        self.pushButton_3.clicked.connect(self.onPushButtonCLicked3)
        self.pushButton_4.clicked.connect(self.onPushButtonCLicked4)
        self.pushButton_5.clicked.connect(self.onPushButtonCLicked5)
        self.pushButton_6.clicked.connect(self.onPushButtonCLicked6)
    def onPushButtonCLicked(self):
        self.grafica(self.automatauno)


    def onPushButtonCLicked2(self):
        C = Control(self.listautomata)
        self.grafica(C.complemento(0))


    def onPushButtonCLicked3(self):
        C = Control(self.listautomata)
        self.grafica(C.Union())
    def onPushButtonCLicked4(self):
        self.grafica(self.automatados)



    def onPushButtonCLicked5(self):
        C = Control(self.listautomata)
        self.grafica(C.complemento(1))
    def onPushButtonCLicked6(self):
        print(self.automatados.amplitud('C'))

    def grafica(self, automata):

        auto = automata
        alf = auto.getAlfabeto()
        estados = []
        for i in auto.getListaNodoEstado():
            estados.append(i.getEstado())
        trans = []
        for i in auto.getListaTran():
           trans.append([i.getOrigen(), i.getDestino(), i.getOperacion()])

        inicial = auto.getEstadoInicial()
        aceptacion = auto.getEstadosAceptacion()

        x = dibujarAutomata(alf, estados, inicial, trans, aceptacion)
        v = VentanaGrafico(alf, inicial, aceptacion, estados, trans)
        if x == 2:
            v.iniciarVentana()
        else:
            v.EAlfabeto()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Automata Uno"))
        self.pushButton_2.setText(_translate("MainWindow", "Complemento Uno"))
        self.pushButton_3.setText(_translate("MainWindow", "Reverso  Uno"))
        self.pushButton_4.setText(_translate("MainWindow", "Automata dos"))
        self.pushButton_5.setText(_translate("MainWindow", "Complemento dos"))
        self.pushButton_6.setText(_translate("MainWindow", "Reverso dos"))
