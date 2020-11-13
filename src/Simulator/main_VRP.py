'''
Created on 13 nov. 2020

@author: promet
'''

from Graph.myGraphs.GpTest import GpTest
from Algorithms.VRP.VRP_Engines import VRP_Engines

'''
Create the graph and initialized the common Knowledge
'''
GpTest.create()

'''
Start the ECHVRP algorithm
'''
VRP_Engines.ECHVRP()