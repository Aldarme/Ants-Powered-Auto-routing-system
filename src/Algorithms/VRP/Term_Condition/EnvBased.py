'''
Created on 12 mai 2020
@author: promet
'''
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge
from math import ceil


class EnvBased:
    
    @staticmethod
    def termCond():
        """
        Return the number of iteration of the ant colony according to the complexity of the graph
        """
        nbrNeigbTotal = 0
        vtx_array = []
        
        vtx_array = CommonKnowledge.adjMtxMidGraph.get_Vertices()
        
        for vtx in vtx_array:
            nbrNeigbTotal += CommonKnowledge.adjMtxMidGraph.get_nbrOfNeigb(vtx)
        
        return int(ceil(float(nbrNeigbTotal) / float(CommonKnowledge.adjMtxMidGraph.get_nbrOfVertices())))