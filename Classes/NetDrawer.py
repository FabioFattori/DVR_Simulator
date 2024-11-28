from Classes.Net import Net

class Drawer:
    def __init__(self):
        self.pathToDir = "NetImages"
        pass

    def draw(self,net:Net):
        '''Disegna la rete passata'''
        # use the networkx library to draw the network
        import networkx as nx
        import matplotlib.pyplot as plt
        import datetime
        
        G = nx.Graph()
        
        for node in net.nodes:
            G.add_node(node.name)
            for neighbor, (weight, _) in node.neighbors.items():
                G.add_edge(node.name, neighbor.name, weight=weight)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        # imposta la grandezza dell'immagine
        plt.gcf().set_size_inches(16, 8)
        # ottieni il datetime corrente
        now = datetime.datetime.now()
        # salva il grafico in un file
        fileName = net.name+now.strftime("%Y%m%d%H%M%S")+".png"
        plt.savefig(fileName)
        self.createImageDir()
        self.moveCreatedImageToDir(fileName=fileName)
        plt.show()
    
    def createImageDir(self):
        import os
        if not os.path.exists(self.pathToDir):
            os.makedirs(self.pathToDir)
    
    def moveCreatedImageToDir(self,fileName):
        import os
        import shutil
        shutil.move(fileName, self.pathToDir)
