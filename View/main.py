from Controller.AutoDos import Automata




if __name__ == "__main__":
    A = Automata()
    A.cargarRedInicial("../Data/datos.json")
    print(A.amplitud('A'), 'Amplitud')
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


    # trans2 = [["A", "B", 1], ["A", "A", 0], ["A", "E", 0], ["E", "D", 1], ["F", "F", 1], ["D", "C", 1], ["B", "A", 0],
    #          ["E", "C", 0], ["F", "D", 0], ["B", "B", 1]]
    #
    # trans=[]
    # # estados.insert(nodo, A.listaNodoEstado[nodo].estado)
    # for tran in range(len(A.listaTran)):
    #     A=A.listaTran[tran].origen
    #     trans.insert(tran,A.listaTran)
    #
    #
    # inicial = ["A"]
    # alf = [0, 1]
    # aceptacion = ["C"]


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
