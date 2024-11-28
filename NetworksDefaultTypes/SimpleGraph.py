import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.Net import Net

"""
Qui creiamo una rete semplice con 10 nodi.
In questa rete ci sono due centri, uno in A e uno in F collegati fra loro.
"""

net = Net("Simple Network")

nodes = ["A","B","C","D","E","F","G","H","I","J"]

for node in nodes:
    net.addNode(node)

# code for a simple graph
# first center in A
net.addConnection("A","B",1)
net.addConnection("A","C",2)
net.addConnection("A","D",3)
net.addConnection("A","E",4)
net.addConnection("A","F",5)
# second center in F
net.addConnection("F","G",1)
net.addConnection("F","H",2)
net.addConnection("F","I",3)
net.addConnection("F","J",4)

net.run_routing_algorithm()

net.printRoutingTables()