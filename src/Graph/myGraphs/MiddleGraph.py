'''
Created on 26 avr. 2021

@author: promet
'''
from Simulator.DEBUG import DEBUG_MODE
from Graph.Edge import Edge
from Graph.Vertex import Vertex
from Utilities.Dijkstra import Dijkstra
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge

class MiddleGraph:
    
    vtxList = []
    edgList = []
    rvEdgList = []
    
    @staticmethod
    def create(deliveryList_p = None, InitID_p=None):
        
        for elm in deliveryList_p:
            MiddleGraph.vtxList.append(elm)
        
        #get vtx corresponding to "
        myVtx = CommonKnowledge.get_adjMtxGraph().get_vtx(InitID_p)
        
        #From deposit, find the shortest path to all other busStop
        Dijkstra.run(CommonKnowledge.adjMtxGraph, myVtx)
        
        #Build vertices path from each delivery point to the deposit
        
        
        #Build middle graph with vertex label data
            
            
        #for i in range(0, len(deliveryList_p)-2):
        #    MiddleGraph.edgList.append(Edge(deliveryList_p[i], deliveryList_p[i+1], MiddleGraph.dict))
        #    MiddleGraph.rvEdgList.append(Edge(deliveryList_p[i+1], deliveryList_p[i], MiddleGraph.dict))




