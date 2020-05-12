'''
Created on 12 mai 2020
@author: promet
'''
from Ant_Colony.CommonKnowledge import CommonKnowledge
from math import ceil


class EnvBasedTerm:
    
    @staticmethod
    def termCond():
        """
        Return the number of iteration of the ant colony according to the complexity of the graph
        """
        nbrNeigbTotal = 0
        vtx_array = []
        
        vtx_array = CommonKnowledge.adjMtxGraph.get_Vertices()
        
        for vtx in vtx_array:
            nbrNeigbTotal += CommonKnowledge.adjMtxGraph.get_nbrOfNeigb(vtx)
        
        return int(ceil(float(nbrNeigbTotal) / float(CommonKnowledge.adjMtxGraph.get_nbrOfVertices())))