'''
Created on 13 nov. 2020

@author: promet
'''

from Graph.myGraphs.GpTest import GpTest
from Graph.myGraphs.GpBelfort import GpBelfort
from Algorithms.VRP.VRP_Engines import VRP_Engines
from Graph.myGraphs.bdd_Graph.dbExploit import dbExploit
from Graph.myGraphs.MiddleGraph import MiddleGraph
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge

'''
Initialize connection to the graph database
'''
dbExploit.init_connection()

'''
Create the graph and initialized the common Knowledge
'''
warehouse_vertex = "Gare"

#GpTest.create(warehouse_vertex)
GpBelfort.create()  #GpBelfort.create(warehouse_vertex)

'''
Create intermediate graph based on delivery points list
'''

MiddleGraph.create(CommonKnowledge.deliveryList, warehouse_vertex)

'''
Start the ECHVRP algorithm
'''
VRP_Engines.ESCSHVRP(2)