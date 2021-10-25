import pygame
from Model.Transicion import Transicion
from Model.nodoEstado import nodoEstado
from collections import deque
from copy import copy
import json

'''
class Grafo:
    def __init__(self):
        self.listaNodoEstado = []
        self.listaTransicion = []
        self.listaVisitados = []
        self.listaBloqueadas = []

    def getListaNodoEstado(self):
        return self.listaNodoEstado

    def getListaTransicion(self):
        return self.listaTransicion


#ESTE TENGO CONFUCION CON CUAL CAMBIARLO
    def getListaVisitados(self):
        return self.listaVisitados



    def ingresarNodoEstado(self, estado):
        if self.verificarNodoEstado(estado) is None:
            self.listaTransicion.append(nodoEstado(estado))

    def verificarNodoEstado(self,estado):
        for nodoEstado in self.listaNodoEstado:
            if estado == nodoEstado.getEstado():
                return nodoEstado
        return None

    def obtenerOrigen(self, estado):
        for i in range(len(self.listaNodoEstado)):
            if estado == self.listaNodoEstado[i].getEstado():
                #print('obtengo el vertice :', self.listaVertices[i].getDato() )
                return self.listaNodoEstado[i]

    def ingresarTransicion(self, origen, destino, operacion):
        if self.verificarTransicion(origen, destino) == None:
            if self.verificarNodoEstado(origen) != None and self.verificarTransicion(destino) != None:
                self.listaTransicion.append(Transicion(origen, destino, int(operacion)))
                self.verificarNodoEstado(origen).getListaTransicion().append(destino)

    def verificarTransicion(self, origen, destino):
        for Transicion in self.listaTransicion:
            if Transicion.getOrigen() == origen and Transicion.getDestino() == destino:
                return Transicion
        return None

    def profundidad(self, posicion, lista_visitados):

        if self.verificarNodoEstado(posicion):
            if not lista_visitados:
                lista_visitados.append(posicion)
            for Transicion in self.verificarNodoEstado(posicion).getListaTransicion():
                if Transicion not in lista_visitados:
                    lista_visitados.append(Transicion)
                    lista_visitados = self.profundidad(Transicion, lista_visitados)
            print(lista_visitados)
            return lista_visitados
        else:
            return "El nodo estado señalado para iniciar el recorrido no existe"

    def amplitud(self, estado):
        visitadosA = []
        cola = deque()
        nodoEstado = self.obtenerOrigen(estado)
        if nodoEstado != None:
            cola.append(nodoEstado)
            visitadosA.append(estado)
        while cola:
            elemento = cola.popleft()
            for Transicion in elemento.getListaTransicion():#prueba no dirigida
                if Transicion not in visitadosA:
                    nodoEstado = self.obtenerOrigen(Transicion)
                    cola.append(nodoEstado)
                    visitadosA.append(Transicion)
        return visitadosA


    def imprimirNodoEstado(self):
        for nodoEstado in self.listaNodoEstado:
            print(nodoEstado.getEstado())

    def imprimirTransicion(self):
        for Transicion in self.listaTransicion:
            print('Origen: {0} -- Destino: {1} -- Peso: {2}'.format(Transicion.getOrigen(), Transicion.getDestino(),
                                                                    Transicion.getOperacion()))

    def imprimirListaTransicion(self):
        for nodoEstado in self.listaNodoEstado:
            print('Lista de transiciones de ', nodoEstado.getEstado(), ': ', nodoEstado.getListaTransicion())

    def separador(self):
        print()
        print('----------------------------------')
        print()

    def getPozos(self):
        pozos = 0
        self.mostrarTransicion()
        for i in range(len(self.listaNodoEstado)):
           #print(self.listaNodoEstado[i].getEstado(),'pozos despues de la sagrada linea del tiempo ', self.listaNodoEstado[i].getListaTransicion())
           if len(self.listaNodoEstado[i].getListaTransicion()) == 0:
               #print ('estoy dentro con el pozo ', self.listaNodoEstado[i].getListaTransicion())
               pozos += 1
        #print('pozos despues de la sagrada linea del tiempo ',self.listaNodoEstado.getListaTransicion())
        print('Cantidad de pozos', pozos)
        return pozos

    def getFuentes(self):
        nroFuentes = 0
        bandera = False
        for nodoEstado in self.listaNodoEstado:
            for Transicion in self.listaTransicion:
                if Transicion.getDestino() == nodoEstado.getEstado():
                    bandera = True
                if bandera != False:
                    break
            if bandera == False:
                print('El nodoEstado:', nodoEstado.getEstado(), 'es una fuente')
                nroFuentes += 1
        print('La cantidad de fuentes  es: ', nroFuentes)
        return nroFuentes

    def fuerteConexo(self):
        nroPozos = self.getPozos()
        nroFuentes = self.getFuentes()
        if nroPozos > 0 and nroFuentes > 0:
            return True
        return False # malparido retorno casi no lo hacemos
"""
    def ordenamiento(self, copiaAristas):  # Ordeno de menor a mayor
        for i in range(len(copiaAristas)):
            for j in range(len(copiaAristas)):
                if copiaAristas[i].getPeso() < copiaAristas[j].getPeso():
                    temp = copiaAristas[i]
                    copiaAristas[i] = copiaAristas[j]
                    copiaAristas[j] = temp
"""
"""
    def prim(self):
        copiaAristas = copy(self.listaAristas)
        conjunto = []  # se va encargar de guardar los vertices visitados
        aristasPrim = []
        aristasTemp = []
        self.ordenamiento(copiaAristas)
        self.dirigido(copiaAristas)
        menor = copiaAristas[0]
        conjunto.append(menor.getOrigen())
        terminado = False
        while terminado == False:
            for vertice in conjunto:
                self.algoritmoPrim(copiaAristas, conjunto, aristasPrim, aristasTemp, vertice)
            if len(self.listaVertices) == len(conjunto):
                terminado = True
        print(conjunto)
        for arista in aristasPrim:
            print('Origen: {0} - Destino: {1} - Peso: {2}'.format(arista.getOrigen(), arista.getDestino(),
                                                                  arista.getPeso()))
        return aristasPrim
"""
"""
    def algoritmoPrim(self, copiaAristas, conjunto, aristasPrim, aristasTemp, vertice):
        ciclo = False
        self.agregarTemp(copiaAristas, aristasTemp, vertice)
        candidata = self.candidataPrim(aristasTemp, copiaAristas, aristasPrim)
        if candidata != None:
            if candidata.getOrigen() in conjunto and candidata.getDestino() in conjunto:
                ciclo = True
            if ciclo == False:
                aristasPrim.append(candidata)
                if not candidata.getOrigen() in conjunto:
                    conjunto.append(candidata.getOrigen())
                if not candidata.getDestino() in conjunto:
                    conjunto.append(candidata.getDestino())
"""
"""
    def agregarTemp(self, copiaAristas, aristasTemp, vertice):
        for arista in copiaAristas:
            if arista.getOrigen() == vertice or arista.getDestino() == vertice:
                if self.verificarAristaTemp(arista, aristasTemp):
                    aristasTemp.append(arista)
"""
"""
    def verificarAristaTemp(self, arista, aristasTemp):
        for elemento in aristasTemp:
            if elemento.getOrigen() == arista.getOrigen() and elemento.getDestino() == arista.getDestino():
                return False
        return True
"""
"""
    def candidataPrim(self, aristasTemp, copiaAristas, aristasPrim):
        menor = copiaAristas[len(copiaAristas) - 1]
        for i in range(len(aristasTemp)):
            if aristasTemp[i].getPeso() < menor.getPeso():
                if self.verificarPrim(aristasTemp[i], aristasPrim):
                    menor = aristasTemp[i]
        aristasTemp.pop(aristasTemp.index(menor))
        return menor
"""
"""
    def verificarPrim(self, candidata, aristasPrim):
        for arista in aristasPrim:
            if arista.getOrigen() == candidata.getOrigen() and arista.getDestino() == candidata.getDestino():
                return False
            if arista.getDestino() == candidata.getDestino() and arista.getOrigen() == candidata.getOrigen():
                return False
        return True
"""

    def dirigido(self, copiaTransicion):
        for elemento in copiaTransicion:
            for i in range(len(copiaTransicion)):
                if elemento.getOrigen() == copiaTransicion[i].getDestino() and elemento.getDestino() == copiaTransicion[
                    i].getOrigen():
                    copiaTransicion.pop(i)
                    break

"""
    def noDirigido(self, copiaAristas):
        dirigido = False
        for elemento in copiaAristas:
            for i in range(len(copiaAristas)):
                if elemento.getOrigen() == copiaAristas[i].getDestino() and elemento.getDestino() == copiaAristas[
                    i].getOrigen():
                    dirigido = True
            if dirigido == False:
                copiaAristas.append(Arista(elemento.getDestino(), elemento.getOrigen(), elemento.getPeso()))
"""
"""
    def noDirigido2(self):
        copiaAristas = self.listaAristas
        dirigido = False
        for elemento in copiaAristas:
            for i in range(len(copiaAristas)):
                if elemento.getOrigen() == copiaAristas[i].getDestino() and elemento.getDestino() == copiaAristas[
                    i].getOrigen():
                    dirigido = True
            if dirigido == False:
                copiaAristas.append(Arista(elemento.getDestino(), elemento.getOrigen(), elemento.getPeso()))
"""
"""
    def Kruskal(self):
        copiaAristas = copy(self.getListaAristas())  # copia de las aristas
        AristasKruskal = []
        ListaConjuntos = []

        self.ordenamiento(copiaAristas)  # ordeno las aristas
        for menor in copiaAristas:
            self.Operacionesconjuntos(menor, ListaConjuntos, AristasKruskal)
        # esta ordenada de mayor a menor
        print("-----------Kruskal---------------")
        for dato in AristasKruskal:
            print("Origen: {0} destino: {1} peso: {2}".format(dato.getOrigen(), dato.getDestino(), dato.getPeso()))
        return AristasKruskal

    def Operacionesconjuntos(self, menor, ListaConjuntos, AristasKruskal):
        encontrado1 = -1
        encontrado2 = -1

        if not ListaConjuntos:  # si esta vacia
            ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
            AristasKruskal.append(menor)

        else:
            for i in range(len(ListaConjuntos)):
                if (menor.getOrigen() in ListaConjuntos[i]) and (menor.getDestino() in ListaConjuntos[i]):
                    return  ##Camino cicliclo

            for i in range(len(ListaConjuntos)):
                if menor.getOrigen() in ListaConjuntos[i]:
                    encontrado1 = i
                if menor.getDestino() in ListaConjuntos[i]:
                    encontrado2 = i

            if encontrado1 != -1 and encontrado2 != -1:
                if encontrado1 != encontrado2:  # si pertenecen a dos conjuntos diferentes
                    # debo unir los dos conjuntos
                    ListaConjuntos[encontrado1].update(ListaConjuntos[encontrado2])
                    # este update si funciona correctemente
                    ListaConjuntos[encontrado2].clear()  # elimino el conjunto
                    AristasKruskal.append(menor)

            if encontrado1 != -1 and encontrado2 == -1:  # si va unido por un conjunto
                # el update se cambio con por el add ya que al agregar cadenas a Listaconjuntos
                # no se guardaba como "Silvestre" sino que la desglosaba en sus caracteres "S,i,l,v,e,t,r,e" en Listaconjuntos
                ListaConjuntos[encontrado1].add(menor.getOrigen())
                ListaConjuntos[encontrado1].add(menor.getDestino())
                AristasKruskal.append(menor)

            if encontrado1 == -1 and encontrado2 != -1:  # si va unido por un conjunto
                ListaConjuntos[encontrado2].add(menor.getOrigen())
                ListaConjuntos[encontrado2].add(menor.getDestino())
                AristasKruskal.append(menor)

            if encontrado1 == -1 and encontrado2 == -1:  # si no existe en los conjuntos
                ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                AristasKruskal.append(menor)

    def Boruvka(self):
        copiaNodos = copy(self.getListaVertices())  # copia de los nodos
        copiaAristas = copy(self.getListaAristas())  # copia de las aristas
        borukvka = []
        #self.noDirigido(copiaAristas)
        #self.dirigido(copiaAristas)
        AristasBorukvka = []
        ListaConjuntos = []
        bandera = True
        cantidad = 0
        while (cantidad > 1 or bandera):
            for Nodo in copiaNodos:
                self.OperacionesconjuntosB(Nodo, ListaConjuntos, AristasBorukvka, copiaAristas)
            bandera = False
            cantidad = self.Cantidadconjuntos(ListaConjuntos)

        for dato in AristasBorukvka:
            print("Origen: {0} destino: {1} peso: {2}".format(dato.getOrigen(), dato.getDestino(), dato.getPeso()))


        return AristasBorukvka

    def Cantidadconjuntos(self, ListaConjuntos):
        cantidad = 0
        for conjunto in ListaConjuntos:
            if len(conjunto) > 0:
                catidad = cantidad +1
        return cantidad

    def OperacionesconjuntosB(self, Nodo, ListaConjuntos, AristasBorukvka, copiaAristas):
        encontrado1 = -1
        encontrado2 = -1
        menor = self.Buscarmenor(Nodo, copiaAristas)

        if not menor == None:  # si no esta vacio
            if not ListaConjuntos:  # si esta vacia
                ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                AristasBorukvka.append(menor)
            else:
                for i in range(len(ListaConjuntos)):
                    if (menor.getOrigen() in ListaConjuntos[i]) and (menor.getDestino() in ListaConjuntos[i]):
                        return False  ##Camino cicliclo

                for i in range(len(ListaConjuntos)):
                    if menor.getOrigen() in ListaConjuntos[i]:
                        encontrado1 = i
                    if menor.getDestino() in ListaConjuntos[i]:
                        encontrado2 = i

                if encontrado1 != -1 and encontrado2 != -1:
                    if encontrado1 != encontrado2:  # si pertenecen a dos conjuntos diferentes
                        # debo unir los dos conjuntos
                        ListaConjuntos[encontrado1].update(ListaConjuntos[encontrado2])
                        ListaConjuntos[encontrado2].clear()  # elimino el conjunto
                        AristasBorukvka.append(menor)

                if encontrado1 != -1 and encontrado2 == -1:  # si va unido por un conjunto
                    ListaConjuntos[encontrado1].update(menor.getOrigen())
                    ListaConjuntos[encontrado1].update(menor.getDestino())
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 != -1:  # si va unido por un conjunto
                    ListaConjuntos[encontrado2].update(menor.getOrigen())
                    ListaConjuntos[encontrado2].update(menor.getDestino())
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 == -1:  # si no existe en los conjuntos
                    ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                    AristasBorukvka.append(menor)
"""
    def Buscarmenor(self, Nodo, copiaAristas):
        temp = []
        for adyacencia in Nodo.getListaAdyacentes():
            for Arista in copiaAristas:
                # busco las aristas de esa lista de adyacencia
                if Arista.getOrigen() == Nodo.getDato() and Arista.getDestino() == adyacencia:
                    temp.append(Arista)
        if temp:  # si no esta vacia
            # una vez obtenga todas las aristas, saco la menor
            self.ordenamiento(temp)  # ordeno las aristas
            # elimin ese destino porque ya lo voy a visitar
            print("{0}-{1}:{2}".format(temp[0].getOrigen(), temp[0].getDestino(), temp[0].getPeso()))

            Nodo.getListaAdyacentes().remove(temp[0].getDestino())
            return temp[0]  # es la menor

        return None  # es la menor
"""
"""
    def cambiarDireccion(self, origen, destino):
        for arista in self.listaAristas:
            origenCopia = str(arista.getOrigen())
            destinoCopia = str(arista.getDestino())
            if origen == origenCopia and destino == destinoCopia:
                temp = arista.getOrigen()
                arista.setOrigen(arista.getDestino())
                arista.setDestino(temp)
"""
"""
    def bloquearArista(self, origen, destino):
        for arista in self.listaAristas:
            origenCopia = str(arista.getOrigen())
            destinoCopia = str(arista.getDestino())
            if origen == origenCopia and destino == destinoCopia:
                self.listaBloqueadas.append(arista)
                indice = self.listaAristas.index(arista)
                self.listaAristas.pop(indice)

    def desbloquearArista(self, origen, destino):
        for arista in self.listaBloqueadas:
            origenCopia = str(arista.getOrigen())
            destinoCopia = str(arista.getDestino())
            if origen == origenCopia and destino == destinoCopia:
                self.listaAristas.append(arista)
                indice = self.listaBloqueadas.index(arista)
                self.listaBloqueadas.pop(indice)
"""
    def gradoNodoEstado(self, nodoEstado):
        gradoNodo = 0
        nodoEntrada = self.verificarNodoEntrada(nodoEstado)
        copiaTransicion = copy(self.listaTrsansicion)
        self.noDirigido(self.listaTransicion)
        for nodoEstado in self.listaNodoEstado:
            if nodoEstado == nodoEntrada:
                gradoNodo = len(nodoEstado.getListaTransicion())
        self.listaAristas = copiaTransicion
        return gradoNodo

"""
    def caminoMasCorto(self, origen, destino):
        VerticesAux = []
        VerticesD = []
        caminos = self.dijkstra(origen, VerticesAux)
        #print('Caminos: ', caminos)
        cont = 0
        for i in caminos:
            print('Distancia mínima a:'+self.listaVertices[cont].getDato()+' es: '+str(i))
            cont = cont+1
        self.rutas(VerticesD, VerticesAux, destino, origen)
        print('El camino mas corto de:'+origen+'a'+destino+'es:')
        print(VerticesD)
        return VerticesD
"""
    def rutas(self, VerticesD, VerticesAux, destino, origen):
        verticeDestino = self.obtenerOrigen(destino)
        indice = self.listaVertices.index(verticeDestino)
        if VerticesAux[indice] is None:
            print('No hay camino entre', (destino, origen))
            return
        aux = destino
        #print('si entre', aux, destino)

        while aux != origen:
            verticeDestino = self.obtenerOrigen(aux)
            indice = self.listaVertices.index(verticeDestino)
            VerticesD.insert(0, aux)
            aux = VerticesAux[indice]
        VerticesD.insert(0, aux)

    def dijkstra(self, origen, VerticesAux):
        marcados = []  # la lista de los que ya hemos visitado
        caminos = []  # la lista final
        # iniciar los valores en infinito
        for v in self.listaVertices:  # LO QUE HACE EL FOR ES BUSCA EL ORIGEN EN LA LISTA DE VERTICES Y LO GUARDA EN LA  LISTA EN LA POSICION 0
            caminos.append(float("inf"))
            marcados.append(False)
            VerticesAux.append(None)
            if v.getDato() == origen:
                #print('si entre')
                caminos[self.listaVertices.index(v)] = 0
                VerticesAux[self.listaVertices.index(v)] = v.getDato()

        while not self.todosMarcados(marcados):  # mientras no todos los marcados esten en true
            aux = self.menorNoMarcado(caminos, marcados)  # obtuve el vertices menor no marcado A
            if aux is None:
                break
            indice = self.listaVertices.index(aux)  # indice del menor no marcado
            marcados[indice] = True  # marco como visitado
            valorActual = caminos[indice]
            for vAdya in aux.getListaAdyacentes():  # b TENER ENCUENTA
                indiceNuevo = self.listaVertices.index(self.obtenerOrigen(vAdya))
                arista = self.verificarArista2(aux.getDato(), vAdya)  # (vAdya, aux.getDato())
                if caminos[indiceNuevo] > valorActual + arista.getPeso():
                    caminos[indiceNuevo] = valorActual + arista.getPeso()
                    VerticesAux[indiceNuevo] = self.listaVertices[indice].getDato()

        return caminos

    def menorNoMarcado(self, caminos, marcados):
        verticeMenor = None
        caminosAux = sorted(caminos)  # Me ordena de menor a mayor
        copiacaminos = []
        for f in caminos:
            copiacaminos.append(f)

        bandera = True
        contador = 0
        while bandera:
            menor = caminosAux[contador]
            if marcados[copiacaminos.index(menor)] == False:
                verticeMenor = self.listaVertices[copiacaminos.index(menor)]  # aqui obtengo el vertice menor
                bandera = False
            else:
                copiacaminos[copiacaminos.index(menor)] = "x"
                contador = contador + 1

        return verticeMenor
    def todosMarcados(self, marcados):
        for j in marcados:
            if j is False:
                return False
        return True
#esta es la interfaz pero no se como modificarla
    def cargarRedInicial(self, ruta):
        with open(ruta) as contenido:
            redAcme = json.load(contenido)
        for vertice in redAcme["Cuevas"]:
            self.ingresarVertice(vertice)
        for arista in redAcme["Caminos"]:
            self.ingresarArista(arista[0], arista[1], arista[2])
        #self.noDirigido(self.listaAristas)

    def dibujarTabla(self, x, y, ventana, aguaMarina=pygame.Color(173, 216, 230), blanco=pygame.Color(155, 155, 155),
                     negro=pygame.Color(0, 0, 0)):
        contador = 0
        pygame.draw.rect(ventana, aguaMarina, (x - 200, 0, 400, 30))
        pygame.draw.rect(ventana, blanco, (x - 200, 30, 400, y - 30))
        miFuente = pygame.font.Font(None, 23)
        miTexto = miFuente.render('LISTA ARISTAS', 0, blanco)
        ventana.blit(miTexto, (x - 195, 8))

        for arista in self.listaAristas:
            miTexto1 = miFuente.render(
                '{} - {} - {}'.format(arista.getOrigen(), arista.getDestino(), arista.getPeso()), 0, negro)
            ventana.blit(miTexto1, (x - 195, 35 + contador))
            contador += 15
        pygame.draw.rect(ventana, aguaMarina, (x - 200, 0 + contador + 35, 400, 30))
        miTexto = miFuente.render('LISTA BLOQUEADAS', 0, blanco)
        ventana.blit(miTexto, (x - 195, 8 + 35 + contador))
        for bloqueada in self.listaBloqueadas:
            miTexto1 = miFuente.render(
                '{} - {} - {}'.format(bloqueada.getOrigen(), bloqueada.getDestino(), bloqueada.getPeso()), 0, negro)
            ventana.blit(miTexto1, (x - 195, 40 + 35 + contador))
            contador += 15
    #-----------------------------------------------barra azul inferior donde s emuestra el resultado no joderla por favor--------------------
    def dibujarResultado(self, x, y, ventana, texto, blanco=pygame.Color(155, 155, 155), negro=pygame.Color(0, 0, 0)):
        #pygame.draw.rect(ventana, blanco, ((x / 2) / 2, y - 150, 200, y - 50))
        pygame.draw.rect(ventana, blanco,((x / 8) / 10, y - 70,800,50))
        miFuente = pygame.font.Font(None, 30)
        neuvoTexto = str(texto)
        miTexto = miFuente.render(neuvoTexto, 0, negro)
        ventana.blit(miTexto, (((x / 8) / 8) + 25, y - 50))


    def cambiarDireccion(self, origen, destino):
        for arista in self.listaAristas:
            origenCopia = str(arista.getOrigen())
            destinoCopia = str(arista.getDestino())
            if origen == origenCopia and destino == destinoCopia:
                temp = arista.getOrigen()
                arista.setOrigen(arista.getDestino())
                arista.setDestino(temp)
"""
    def bloquearArista(self, origen, destino):
        for arista in self.listaAristas:
            origenCopia = str(arista.getOrigen())
            destinoCopia = str(arista.getDestino())
            if origen == origenCopia and destino == destinoCopia:
                self.listaBloqueadas.append(arista)
                indice = self.listaAristas.index(arista)
                self.listaAristas.pop(indice)

    def desbloquearArista(self, origen, destino):
        for arista in self.listaBloqueadas:
            origenCopia = str(arista.getOrigen())
            destinoCopia = str(arista.getDestino())
            if origen == origenCopia and destino == destinoCopia:
                self.listaAristas.append(arista)
                indice = self.listaBloqueadas.index(arista)
                self.listaBloqueadas.pop(indice)
"""
    def gradoNodoEstado(self, nodoEstado):
        gradoNodoEstado = 0
        nodoEntrada = self.verificarNodoEstado(nodoEstado)
        copiaTransicion = copy(self.listaTransicion)
        self.noDirigido(self.listaTransicion)
        for nodoEstado in self.listaNodoEstado:
            if nodoEstado == nodoEntrada:
                gradoNodoEstado = len(nodoEstado.getListaTransicion())
        self.listaTransicion = copiaTransicion
        return gradoNodoEstado
    def verificarTransicion2(self, Origen, Destino):
        for i in range(len(self.listaAristas)):
            if self.listaAristas[i].getOrigen() == Origen and self.listaAristas[i].getDestino() == Destino:
                return self.listaAristas[i]
        return None

    def mostrarTransicion(self):
        for i in range(len(self.listaAristas)):
            print(self.listaAristas[i].getOrigen(), self.listaAristas[i].getDestino(),
                  self.listaAristas[i].getOperacion())
"""
'''