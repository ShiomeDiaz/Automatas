from Controller.AutoDos import Automata
import copy

class Control:

    automatas=[]

    def __init__(self, automatas):
        self.automatas = automatas



    # Metodo que devuelve el complemento de un automata
    def complemento(self,nAutomata):
        automataComplemento = copy.deepcopy(self.automatas[nAutomata])
        aceptacion= copy.deepcopy(automataComplemento.estadosAceptacion)

        for estado in range(len(automataComplemento.listaNodoEstado)):
            automataComplemento.estadosAceptacion.append(automataComplemento.listaNodoEstado.estado)


        for i in range(len(aceptacion)):
            for j in range(len(automataComplemento.listaNodoEstado)):
                if aceptacion[i]==automataComplemento.estadosAceptacion[j]:
                    automataComplemento.estadosAceptacion.pop(i)




        return automataComplemento