import networkx as nx

from database.DAO import DAO
from database.DB_connect import DBConnect


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.nodi = []
        self.idMap = {}

    def creaGrafo(self,goal_fatti):
        self.nodi = DAO.getNodi(goal_fatti)
        for nodo in self.nodi :
            self.grafo.add_node(nodo)
        collegamenti = DAO.getArchi()
        for collegamento in collegamenti :
            if collegamento[0] in self.nodi and collegamento[1] in self.nodi :
               if int(collegamento[2]) > int(collegamento[3])  :
                   peso = int(collegamento[2])  - int(collegamento[3])
                   if peso != 0:
                        self.grafo.add_edge(collegamento[0],collegamento[1],weight = peso)
               elif  int(collegamento[2]) < int(collegamento[3])  :
                   peso = int(collegamento[3]) - int(collegamento[2])
                   if peso != 0 :
                        self.grafo.add_edge(collegamento[1], collegamento[0],weight=peso)
    def top_player(self):
        lista = []
        diz = {}
        giocatore_migliore = None
        for nodo in self.grafo.nodes :
            peso = 0
            vicini = list(self.grafo.neighbors(nodo))
            for vicino in vicini :
                peso += int(self.grafo[nodo][vicino]["weight"])
            diz[nodo] = peso
        valore_massimo = max(diz.values())
        for giocatore in diz.keys() :
            if diz[giocatore] == valore_massimo :
                giocatore_migliore = giocatore
        for vicini in self.grafo.neighbors(giocatore_migliore):
            differenza = int(self.grafo[giocatore_migliore][vicini]["weight"])
            lista.append((vicini,differenza))
        return giocatore_migliore,lista

    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)
