from Classes.Node import Node
import logging

class Net:
    def __init__(self,name = "Example Network"):
        """
        Inizializza una nuova rete con un nome specificato.
        Il nome è utile per identificare la rete stessa, il predefinito è "Example Network".
        """
        self.nodes = []
        self.name = name
        self.initializeLogFile()
    
    def addNode(self,name:str):
        '''Aggiunge un nodo alla rete'''
        new = Node(name)
        self.nodes.append(new)
        return new
        
    
    def removeNode(self,node:Node):
        '''Rimuove un nodo dalla rete'''
        self.nodes.remove(node)
    
    def addConnection(self,node1:str,node2:str,weight:int):
        '''Aggiunge un collegamento tra due nodi con un peso, il collegamento è bidirezionale'''
        node1 = self.getNode(node1)
        node2 = self.getNode(node2)
        if node1 is None or node2 is None:
            print("Nodo non trovato.")
            return
        node1.addNeighbor(node2,weight)
        node2.addNeighbor(node1,weight)
    
    def getNode(self,name:str):
        '''Restituisce il nodo con il nome specificato se esiste, altrimenti restituisce None'''
        for node in self.nodes:
            if node.name == name:
                return node
        return None
    
    def run_routing_algorithm(self):
        """Esegue l'algoritmo di Distance Vector Routing finché le tabelle di routing non si stabilizzano."""
        updated = True
        while updated:
            updated = False
            for node in self.nodes:
                if node.updateRoutingTable():
                    updated = True
    
    def printRoutingTables(self):
        """Stampa le tabelle di routing per tutti i nodi della rete."""
        from prettytable import PrettyTable, ALL
        
        for node in self.nodes:
            print(f"Tabella di routing per il nodo {node.name}:")
            table = PrettyTable()
            table.field_names = ["Destinazione", "Costo", "Passando da"]
            
            for destination, (cost, next_hop) in node.routingTable.items():
                table.add_row([destination.name, cost, next_hop]) 
            
            # Configurazione dell'allineamento e dei bordi
            table.align = "c"  # allinea tutto al centro
            table.hrules = ALL  # mostra tutte le linee orizzontali
            print(table)
            self.insertToLogFile(f"Tabella di routing per il nodo {node.name}:\n"+table.get_string())
            print()
        
        print("Fine delle tabelle di routing.")
        print()
        print("ora disegno il grafo...")
        from Classes.NetDrawer import Drawer
        drawer = Drawer()
        drawer.draw(self)
    
    def initializeLogFile(self):
        '''Inizializza un file di log per la rete in cui inserire le routing tables'''
        logging.basicConfig(filename='network'+self.name+'.log', level=logging.INFO)
        logging.info("Inizializzazione del file di log completata.")
    
    def insertToLogFile(self,message:str):
        '''Inserisce un messaggio nel file di log'''
        logging.info(message)