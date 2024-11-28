import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Net import Net
import random

"""
Qui creiamo una rete con 8 nodi tutti connessi tra loro, creando di fatto una rete a maglia completa.
"""

net = Net("Fully Connected Network")

nodes = ["A","B","C","D","E","F","G","H"]

for node in nodes:
    net.addNode(node)

# code for fully connected graph
for node1 in nodes:
    for node2 in nodes:
        if node1 != node2:
            net.addConnection(node1,node2,random.randint(1,10))


net.run_routing_algorithm()

net.printRoutingTables()