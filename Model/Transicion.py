class Transicion:
    def __init__(self, origen, destino, operacion):
        self.origen = origen
        self.destino = destino
        self.operacion = operacion

    # get & set
    def getOrigen(self):
        return self.origen

    def setOrigen(self, origen):
        self.origen = origen

    def getDestino(self):
        return self.destino

    def setDestino(self, destino):
        self.destino = destino

    def getOperacion(self):
        return self.operacion

    def setOperacion(self, operacion):
        self.operacion = operacion