import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Classes.Net import Net
import random

"""
Qui creiamo una rete con 6 nodi, simulando il percorso di un pacchetto da un dispositivo di origine a Google.
Questo esempio è utile per capire come funzionano i collegamenti tra i vari nodi di una rete, anche se nella realtà i collegamenti sono molto più complessi e numerosi.
"""

net = Net("Ping From Home to Google")

nodes = ["Dispositivo di origine","Home Router","ISP","BackBone Node","IXP","Google Global Network"]

for node in nodes:
    net.addNode(node)


net.addConnection("Dispositivo di origine","Home Router",1)
net.addConnection("Home Router","ISP",random.randint(1,50))
net.addConnection("ISP","BackBone Node",random.randint(1,75))
net.addConnection("BackBone Node","IXP",random.randint(1,100))
net.addConnection("IXP","Google Global Network",random.randint(1,125))

net.run_routing_algorithm()

net.printRoutingTables()