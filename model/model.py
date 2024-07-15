import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nodes = []
        self.edges = []
        self.valoreBest = 0

    def nodi(self):
        return self.grafo.nodes

    def creaGrafo(self):
        self.nodes = DAO.getLocalizzazioni()
        self.edges = DAO.getArchi()

        self.grafo.add_nodes_from(self.nodes)
        for arco in self.edges :
            if arco[0] in self.nodes and arco[1] in self.nodes :
                self.grafo.add_edge(arco[0],arco[1],weight=int(arco[2]))
    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def statistiche(self,localizzazione):
        lista_connesse = self.grafo.edges(localizzazione,data=True)
        return lista_connesse

    def getAdiacenti(self, nodo):
        ris = []
        for vicino in self.grafo.neighbors(nodo):
            ris.append((vicino, self.grafo[nodo][vicino]["weight"]))
        return ris
    def trova_percorso(self,nodo_partenza):
        self.solBest = []
        self.valoreBest = 0
        for vicino in self.grafo.neighbors(nodo_partenza) :
            self.ricorsione([nodo_partenza,vicino])
        return self.solBest,self.valoreBest
    def ricorsione(self,parziale):
        vicini = self.nodiVisitabili(parziale)
        if vicini == [] :
            if self.costaDiPiu(parziale) :
                print("best")
                self.solBest = copy.deepcopy(parziale)
            else :
                for nofo in vicini :
                    last = parziale[-1][1]
                    parziale.append((last,nofo))
                    self.ricorsione(parziale)
                    parziale.pop()

    def nodiVisitabili(self, lista):  # no archi ripetuti
        ris = []
        print(lista)
        ultimoNodo = lista[-1][1]
        for vicino in self.grafo.neighbors(ultimoNodo):
            if (ultimoNodo, vicino) not in lista:
                ris.append(vicino)
        print(ris)
        return ris

    def costaDiPiu(self, parziale):
        valore = 0
        for elemento in parziale :
            valore += self.grafo[elemento[0]][elemento[1]]["weight"]
        if valore > self.valoreBest :
            self.valoreBest = valore
            return True
        return False