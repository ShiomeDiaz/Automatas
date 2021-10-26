class nodoEstado:
    def __init__(self, estado):
        self.estado = estado
        self.listaTransicion = []

    # get & set

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getListaTransicion(self):
        return self.listaTransicion

    def setListaTransicion(self, listaTransicion):
        self.listaTransicion = listaTransicion
