import json
def carga():
    file = open("C:/Users/Shio/PycharmProjects/Automatas/Data/datos.json")
    copy = file.read()
    file.close()
    jsonfile = json.loads(copy)
    NodosUno = jsonfile['uno']['Nodos']
    TransUno = jsonfile['uno']['Trans']
    NodosDos = jsonfile['dos']['Nodos']
    TransDos = jsonfile['dos']['Trans']
    return NodosUno, TransUno, NodosDos, TransDos
#print(carga())