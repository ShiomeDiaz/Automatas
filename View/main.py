import copy

from Controller.AutoDos import Automata
from Controller.Control import Control
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from NuevaGrafica.pyui import Ui_MainWindow


if __name__ == "__main__":

    automataUno = Automata()
    automataUno.cargarRedInicialUNO("../Data/datos.json")
    automataDos = Automata()
    automataDos.cargarRedInicialDOS("../Data/datos.json")

    #print(automataDos.listaNodoEstado[0].estado)

    listAutomatas = [automataUno, automataDos]
    control = Control(listAutomatas)
    # ---Ojo aqui se llama el Menu
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, automataUno, automataDos)
    MainWindow.show()
    sys.exit(app.exec_())
    # ---

    # estados = ["A", "B", "C"]
    # trans = [["A", "B", 1],["A", "B", 2], ["A", "A", 0],["B", "A", 0], ["B", "B", 1], ["C", "B", 1]]
    # inicial = ["A"]
    # alf = [0, 1,2]
    # aceptacion = ["C"]
    #
    # sumidero= False
    # copiaEstados= copy.deepcopy(estados)
    # copiaTrans= copy.deepcopy(trans)
    #
    #
    # for i in range(len(estados)):
    #     contadorTrans=0
    #     valorTrans=[]
    #     transSumidero=[]
    #     for j in range(len(trans)):
    #         if estados[i]==trans[j][0]:
    #             contadorTrans=contadorTrans+1
    #             valorTrans.append(trans[j][2])
    #
    #     if contadorTrans!= len(alf):
    #         transSumidero= copy.deepcopy(alf)
    #         for l in range(len(alf)):
    #             for m in range(len(valorTrans)):
    #                 if alf[l] == valorTrans[m]:
    #                     transSumidero.pop(0)
    #
    #         if sumidero==True:
    #             for n in range(len(transSumidero)):
    #                 nuevaTrans=[estados[i],"sumidero",transSumidero[n]]
    #                 copiaTrans.append(nuevaTrans)
    #
    #         if sumidero==False:
    #             sumidero=True
    #             copiaEstados.append("sumidero")
    #             for n in range(len(transSumidero)):
    #                 nuevaTrans = [estados[i], "sumidero", transSumidero[n]]
    #                 copiaTrans.append(nuevaTrans)
    #
    #
    #
    # estados= copiaEstados
    # trans= copiaTrans
    # print(estados)
    # print(trans)
    # ["C", "D", 0], ["D", "C", 1], ["D", "D", 0], ["D", "C", 1]