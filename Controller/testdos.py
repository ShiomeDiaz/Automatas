
import json

def cargarRedInicial(ruta):
    with open(ruta) as contenido:
        redAcme = json.load(contenido)
    for nodosuno in redAcme["uno"]["Nodos"]:
        print(nodosuno)
    for transuno in redAcme["uno"]["Trans"]:
        print(transuno)
    for nodosdos in redAcme["dos"]["Nodos"]:
        print(nodosdos)
    for transdos in redAcme["dos"]["Trans"]:
        print(transdos[0], transdos[1], transdos[2])
print(cargarRedInicial("C:/Users/Shio/PycharmProjects/Automatas/Data/datos.json"))