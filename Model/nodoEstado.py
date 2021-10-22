class nodoEstado:
    def __init__(self, estado):
        self.estado = estado
        self.listaTransicion = []
        self.estadoAceptacion = bool

    # get & set

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getListaTransicion(self):
        return self.listaTransicion

    def setListaTransicion(self, listaTransicion):
        self.listaTransicion = listaTransicion

    def getEstadoAceptacion(self):
        return self.estadoAceptacion

    def setEstadoAceptacion(self, estadoAceptacion):
        self.estadoAceptacion = estadoAceptacion