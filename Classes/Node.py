
from __future__ import annotations

class Node:
    def __init__(self,name):
        """
        Inizializza un nuovo nodo con un nome specificato.
        """
        self.name = name
        self.routingTable = {
            self:(0,name)
        }
        self.neighbors = {}
    
    def addNeighbor(self,neighbor:Node,weight):
        """
        Aggiunge un collegamento tra questo nodo e un vicino con un peso specificato.
        """
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = (weight,self.name)
            self.updateRoutingTable()
    
    def updateRoutingTable(self):
        """
        Aggiorna la tabella di routing di questo nodo con le informazioni dei vicini.
        Operazione singola di Distance Vector Routing.
        """
        updated = False
        for neighbor, cost_to_neighbor in self.neighbors.items():
            # Ottiene la tabella di routing del vicino
            for destination, (neighbor_cost, next_hop) in neighbor.routingTable.items():
                # Costo totale per raggiungere la destinazione passando per il vicino
                new_cost = cost_to_neighbor[0] + neighbor_cost

                # Se la destinazione non è nella tabella o se abbiamo trovato un percorso più breve, aggiorna
                if (destination not in self.routingTable or
                    new_cost < self.routingTable[destination][0]):
                    self.routingTable[destination] = (new_cost, neighbor.name)
                    updated = True
        return updated  # Ritorna True se la tabella è stata aggiornata