from Controller.AutoDos import Automata
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from NuevaGrafica.pyui import Ui_MainWindow




if __name__ == "__main__":
    A = Automata()
    A.cargarRedInicial("../Data/datos.json")
    #---
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow, A)
    # MainWindow.show()
    # sys.exit(app.exec_())
    #---
    #A.imprimirNodoEstado()
    #A.separador()
    #A.imprimirTransicion()
    #A.separador()
    #A.imprimirListaTransicion()
    #A.separador()
    #A.getPozos()
    #A.separador()
    #A.getFuentes()
    #A.separador()
    #A.fuerteConexo()
    #A.separador()
    #A.separador()
    #A.Boruvka()
    #A.Kruskal()
    #A.prim()




    #A.caminoMasCorto("Silvestre", "Correcaminos")
    #A.dijkstra("Silvestre", "Piolin")
    #A.profundidad(1, 'Silvestre')
    #la_animacion = animacion(G)
    #la_animacion = animacion(G)
    #la_animacion.ejecutar()


# A.separador()
# print(G.getListaTransicion())
# A.separador()
# A.amplitud(1)
# print(G.amplitud(1))
