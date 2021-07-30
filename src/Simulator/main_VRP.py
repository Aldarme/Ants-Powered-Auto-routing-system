'''
Created on 13 nov. 2020

@author: promet
'''

from Graph.myGraphs.GpTest import GpTest
from Graph.myGraphs.GpBelfort import GpBelfort
from Algorithms.VRP.VRP_Engines import VRP_Engines
from Graph.myGraphs.bdd_Graph.dbExploit import dbExploit
from Graph.myGraphs.MiddleGraph import MiddleGraph
from Utilities.DelivListGen import DelivListGen
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge

'''
Initialize connection to the graph database
'''

dbExploit.init_connection()

'''
Create graph of the public system transport of Belfort 
'''

GpBelfort.create()

'''
Create intermediate graph based on delivery points list
'''

#MiddleGraph.create(DelivListGen.debugList)
MiddleGraph.create(DelivListGen.run(80, CommonKnowledge.warehouse_vertex))


'''
Start the ECHVRP algorithm
'''

VRP_Engines.ESCSHVRP(3)