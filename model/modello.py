import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self.aeroporti = DAO.getAllAirports()
        self.grafo = nx.Graph()
        self.idMap = {a.ID: a for a in self.aeroporti}

    def trovaAeroporti(self, minimo):
        return [a for a in self.aeroporti if DAO.getNumCompagnie(a.ID) >= minimo]

    def buildGraph(self, minimo):
        aeroportiTrovati = self.trovaAeroporti(minimo)
        self.grafo.clear()
        self.grafo.add_nodes_from([a.ID for a in aeroportiTrovati])

        for i in range(len(aeroportiTrovati)):
            for j in range(i + 1, len(aeroportiTrovati)):
                a1 = aeroportiTrovati[i]
                a2 = aeroportiTrovati[j]
                arco = DAO.getAllArchi(a1.ID, a2.ID)
                if arco and arco.peso > 0:
                    self.grafo.add_edge(a1.ID, a2.ID, peso=arco.peso)

        return self.grafo

    def trovaPercorso(self, a1, a2):
        if a1 not in self.grafo or a2 not in self.grafo:
            return None
        if not nx.has_path(self.grafo, a1, a2):
            return None
        return nx.shortest_path(self.grafo, source=a1, target=a2)
