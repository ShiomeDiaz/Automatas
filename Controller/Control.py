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

        for estado in automataComplemento.getListaNodoEstado():
            automataComplemento.estadosAceptacion.append(estado.getEstado())

        for i in range(len(aceptacion)):
            reinicio = True
            while reinicio:
                reinicio = False
                for j in range(len(automataComplemento.estadosAceptacion)):
                    if aceptacion[i] == automataComplemento.estadosAceptacion[j]:
                        automataComplemento.estadosAceptacion.pop(j)
                        reinicio = True
                        break

        print(automataComplemento)
        return automataComplemento

    # return ala union

    def Union(self):
        AutomatA = copy.deepcopy(self.automatas[0])
        AutomatB = copy.deepcopy(self.automatas[1])

        automataUnion = copy.deepcopy(self.automatas[0])