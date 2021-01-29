'''
Created on 13 nov. 2020

@author: promet
'''

from Graph.myGraphs.GpTest import GpTest
from Algorithms.VRP.VRP_Engines import VRP_Engines

'''
Create the graph and initialized the common Knowledge
'''
warehouse_vertex = 4

GpTest.create(warehouse_vertex)

'''
Start the ECHVRP algorithm
'''
VRP_Engines.ESCSHVRP()