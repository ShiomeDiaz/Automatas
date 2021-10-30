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
    # listAutomatas = [automataUno, automataDos]
    # control = Control(listAutomatas)
    # ---Ojo aqui se llama el Menu
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, automataUno, automataDos)
    MainWindow.show()
    sys.exit(app.exec_())
    # ---
