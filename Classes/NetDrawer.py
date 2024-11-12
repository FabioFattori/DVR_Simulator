from Classes.Net import Net

class Drawer:
    def __init__(self):
        pass

    def draw(self,net:Net):
        '''Disegna la rete'''
        # use the networkx library to draw the network
        import networkx as nx
        import matplotlib.pyplot as plt
        
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
        plt.gcf().set_size_inches(12, 8)
        # salva il grafico in un file
        plt.savefig(net.name+".png")
        
        plt.show()
        
