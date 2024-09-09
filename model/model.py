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
               self.grafo.add_edge(collegamento[0],collegamento[1],weight=int(collegamento[2]))
        print(self.grafo.edges)


    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)
