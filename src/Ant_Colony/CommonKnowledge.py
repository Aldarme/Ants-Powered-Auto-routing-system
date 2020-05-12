'''
Created on 4 mai 2020

@author: promet
'''

from Graph.MtxGraph import MtxGraph
from Graph.Vertex import Vertex
import sys
from __builtin__ import staticmethod

class CommonKnowledge:
    
    vtx_begin           = Vertex    #Beginning vertex of all ants
    vtx_toReach         = Vertex    #Vertex to reach for all ants
    nbrOfVtx            = 0         #Total number of vertices in the graph
    iterationNbr        = 0         #Current number of iteration for the ant colony algorithm
    evaporation_rate    = 0         #Evaporation coefficient used to update pheromone strength
    optimalPath_length  = 0         #Length of the best path find by an ant
    optimalPath_edg     = []        #Collection of edges making up the best path 
    optimalPath_vtx     = []        #Collection of vertices making up the best path
    adjPheroMtx         = []        #Adjacency pheromone matrix
    adjMtxGraph         = MtxGraph  #Adjacency matrix
    
    @staticmethod
    def commonKnldg_init(vtxBegin_p, vtx_toReach_p):
        CommonKnowledge.vtx_begin = vtxBegin_p
        CommonKnowledge.vtx_toReach = vtx_toReach_p
        CommonKnowledge.optimalPath_length = sys.maxint
        
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
    def dorigo_evaporation(edg_p, iterationLength_p):
        """
        Calculate the evaporation rate of pheromones for the given edge
        """
        phero = CommonKnowledge.adjPheroMtx[CommonKnowledge.adjMtxGraph.get_vtxIdx(edg_p.get_vtx_begin())][CommonKnowledge.adjMtxGraph.get_vtxIdx(edg_p.get_vtx_end())]
        return (((1.0-CommonKnowledge.evaporation_rate) * phero) + (1.0 / iterationLength_p))
    
    @staticmethod
    def incr_IntNumber():
        CommonKnowledge.iterationNbr += 1
    
    @staticmethod
    def flusher():
        """
        Flush :
            the adjacency matrix
            the adjacency pheromone matrix        
        """
        CommonKnowledge.optimalPath_length = sys.maxint
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
    def display_shortestPath():
        """
        Display the shortest path into the console
        """
        print("*"*20)
        print("Shortest path is:")
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