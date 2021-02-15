'''
Created on 4 mai 2020

@author: promet
'''

from Graph.MtxGraph import MtxGraph
from Graph.Vertex import Vertex
import sys


class CommonKnowledge:
    
    vtx_init            = Vertex        #Beginning vertex of all ants (of the AC(O/S) algorithm)
    nbrOfVtx            = 0             #Total number of vertices in the graph
    iterationNbr        = 0             #Current number of iteration for the ant colony algorithm
    #Param. of Ant Colony Algo. 
    evaporation_rate    = 0             #Evaporation coefficient ]0;1] used to update pheromone strength
    optimalPath_length  = 0             #Length of the best path find by an ant
    optimalPath_edg     = []            #Collection of edges making up the best path 
    optimalPath_vtx     = []            #Collection of vertices making up the best path
    adjMtxGraph         = MtxGraph      #Adjacency matrix
    adjPheroMtx         = []            #Adjacency pheromone matrix
    #Param. of SOC & SOH algorithm
    AntInitNrjCapacity  = 1.0
    nrjCapacityMin      = 0.20
    nrjCapacityMax      = 0.80
    
    
    
    
    @staticmethod
    def comnKldg_init(vtx_init_p, evaporationRate_p = 0.2):
        CommonKnowledge.vtx_init = vtx_init_p
        CommonKnowledge.optimalPath_length = sys.maxsize
        CommonKnowledge.evaporation_rate = evaporationRate_p    #by default is 0.8
        
        #Init the adjacency pheromone matrix at the same size that the adjacency matrix, with all elements at "0.0"
        CommonKnowledge.adjPheroMtx = [[0.0 for x in range(CommonKnowledge.adjMtxGraph.size())] for y in range(CommonKnowledge.adjMtxGraph.size())]
        
    @staticmethod
    def set_pheromones(x, y, value):
        """
        Set calculated pheromones at the given position in the adjacency pheromone matrix
        """
        CommonKnowledge.adjPheroMtx[x][y] = value
    
    @staticmethod
    def get_pheromones(x, y):
        """
        Get the pheromones at the given position in the adjacency pheromone matrix
        """
        return CommonKnowledge.adjPheroMtx[x][y]
    
    @staticmethod
    def get_adjPheroMtx():
        """
        Return a copy of the adjacency pheromone matrix
        """
        return CommonKnowledge.adjPheroMtx
    
    @staticmethod
    def get_vtxOptimalPath():
        """
        Fill the optimal path with vertices of given edges
        """
        for edg in CommonKnowledge.optimalPath_edg:
            if edg.get_vtx_begin() not in CommonKnowledge.optimalPath_vtx:
                CommonKnowledge.optimalPath_vtx.append(edg.get_vtx_begin())
            if edg.get_vtx_end() not in CommonKnowledge.optimalPath_vtx:
                CommonKnowledge.optimalPath_vtx.append(edg.get_vtx_end())
    
    @staticmethod
    def pheromone_lowering():
        """
        Lowering the pheromone strength on all arcs by a constant factor
        """
        for i in range (0, len(CommonKnowledge.adjPheroMtx)):
            for j in range(0, len(CommonKnowledge.adjPheroMtx)):
                CommonKnowledge.adjPheroMtx[i][j] = ((1.0-CommonKnowledge.evaporation_rate) * CommonKnowledge.adjPheroMtx[i][j])
    
    @staticmethod
    def pheromone_update(edg_p, totalDist_p, SOC_p):
        """
        Calculate the evaporation rate of pheromones for the given edge, according to the following equation:
        [(1-p) * PheromoneStrength] + turnSize
        """
        pheromeij = CommonKnowledge.adjPheroMtx[CommonKnowledge.adjMtxGraph.get_vtxIdx(edg_p.get_vtx_begin())][CommonKnowledge.adjMtxGraph.get_vtxIdx(edg_p.get_vtx_end())]
        return (pheromeij + ( (totalDist_p) * (1.0 / SOC_p) ) )
    
    @staticmethod
    def interationCnt():
        """
        Increment the iteration number
        """
        CommonKnowledge.iterationNbr += 1
    
    @staticmethod
    def flusher():
        """
        Flush :
            the adjacency matrix
            the adjacency pheromone matrix        
        """
        CommonKnowledge.optimalPath_length = sys.maxsize
        del CommonKnowledge.optimalPath_edg[:]
        del CommonKnowledge.optimalPath_vtx[:]
        del CommonKnowledge.__optimalPath_vtx_tmp[:]
        del CommonKnowledge.adjMtxGraph[:]
    
    @staticmethod
    def optimalPath_VTX_toString():
        """
        Convert all vertices of the optimal path as a string
        """
        tmp = []
        for elmt in CommonKnowledge.optimalPath_vtx:
            tmp.append(elmt.get_ID())
        return "{}".format(tmp)
    
    @staticmethod
    def optimalPath_EDG_toString():
        """
        Convert all edges of the optimal path as a string
        """
        tmp = []
        for elmt in CommonKnowledge.optimalPath_edg:
            tmp.append(elmt.get_vtx_begin().get_ID())
            tmp.append(elmt.get_vtx_end().get_ID())
        return "{}".format(tmp)
    
    @staticmethod
    def display_bestTurn():
        """
        Display the best turn into the console
        """
        print("*"*20)
        print("Best turn is:")
        for vtx in CommonKnowledge.optimalPath_vtx:
            print(vtx.get_ID())
        print("with a length of: {}".format(CommonKnowledge.optimalPath_length));
        print("*"*20);
    
    @staticmethod
    def displayAdjPheroMtx():
        """
        Display the adjacency pheromone matrix in the console
        """
        print("Adjacency phero mtx:")
        for elmt in CommonKnowledge.adjPheroMtx:
            print(elmt)