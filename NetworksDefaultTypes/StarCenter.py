import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.Net import Net

net = Net("Star Center Network")

nodes = ["A","B","C","D","E","F","G","H","I","J"]

for node in nodes:
    net.addNode(node)

# code for a Star Center graph
# first center in A
net.addConnection("A","B",1)
net.addConnection("A","C",2)
net.addConnection("A","D",3)
net.addConnection("A","E",4)
net.addConnection("A","F",5)
net.addConnection("A","G",6)
net.addConnection("A","H",7)
net.addConnection("A","I",8)
net.addConnection("A","J",9)

net.run_routing_algorithm()

net.printRoutingTables()