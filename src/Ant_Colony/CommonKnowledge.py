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
    interationNbr       = 0         #Current number of iteration for the ant colony algorithm
    evaporation_rate    = 0         #Evaporation coefficient used to update pheromone strength
    optimalPath_length  = 0         #Length of the best path find by an ant
    optimalPath_edg     = []        #Collection of edges making up the best path 
    optimalPath_vtx     = []        #Collection of vertices making up the best path
    __optimalPath_vtx_tmp = []      #temporary copy for internal use
    adjPheroMtx         = []        #Adjacency pheromone matrix
    adjMtxGraph         = MtxGraph  #Adjacency matrix
    
    @staticmethod
    def commonKnldg_init(self, vtxBegin_p, vtx_toReach_p):
        self.vtx_begin = vtxBegin_p
        self.vtx_toReach = vtx_toReach_p
        self.optimalPath_length = sys.maxint
        
        #Init the adjacency pheromone matrix at the same size that the adjacency matrix, with all elements at "0.0"
        self.adjPheroMtx = [[0.0 for x in range(self.adjMtxGraph.size())] for y in range(self.adjMtxGraph.size())]
    
    @staticmethod
    def set_pheromones(self, x, y, value):
        """
        Set calculated pheromones at the given position in the adjacency pheromone matrix
        """
        self.adjPheroMtx[x][y] = value
    
    @staticmethod
    def get_pheromones(self, x, y):
        """
        Get the pheromones at the given position in the adjacency pheromone matrix
        """
        return self.adjPheroMtxj[x][y]
    
    @staticmethod
    def get_adjPheroMtx(self):
        """
        Return a copy of the adjacency pheromone matrix
        """
        return self.adjPheroMtx
    
    @staticmethod
    def get_vtxOptimalPath(self):
        """
        Fill the optimal path with vertices of given edges
        """
        for edg in self.optimalPath_edg:
            if edg.get_vtx_begin() not in self.__optimalPath_vtx_tmp:
                self.__optimalPath_vtx_tmp.append(edg.get_vtx_begin)
            if edg.get_vtx_end() not in self.__optimalPath_vtx_tmp:
                self.__optimalPath_vtx_tmp.append(edg.get_vtx_end())
    
    @staticmethod
    def dorigo_evaporation(self, edg_p, iterationLength_p):
        """
        Calculate the evaporation rate of pheromones for the given edge
        """
        phero = self.adjPheroMtx[self.adjMtxGraph.get_vtxIdx(edg_p.get_vtx_begin())][self.adjMtxGraph.get_vtxIdx(edg_p.get_vtx_end())]
        return (((1.0-self.evaporation_rate) * phero) + (1.0 / iterationLength_p))
    

    
    @staticmethod
    def flusher(self):
        """
        Flush :
            the adjacency matrix
            the adjacency pheromone matrix        
        """
        self.optimalPath_length = sys.maxint
        del self.optimalPath_edg[:]
        del self.optimalPath_vtx[:]
        del self.__optimalPath_vtx_tmp[:]
        del self.adjMtxGraph[:]
    
    @staticmethod
    def optimalPath_VTX_toString(self):
        """
        Convert all vertices of the optimal path as a string
        """
        tmp = []
        for vtx in self.optimalPath_vtx:
            tmp.append(vtx.get_ID())
        return "{}".format(tmp)
    
    @staticmethod
    def optimalPath_EDG_toString(self):
        """
        Convert all edges of the optimal path as a string
        """
        tmp = []
        for elmt in self.optimalPath_edg:
            tmp.append(elmt.get_vtx_begin().get_ID())
            tmp.append(elmt.get_vtx_end().get_ID())
        return "{}".format(tmp)
    
    @staticmethod
    def display_shortestPath(self):
        """
        Display the shortest path into the console
        """
        print("*"*20)
        print("Shortest path is:")
        for vtx in self.optimalPath_vtx:
            print(vtx.get_ID())
        print("with a length of: {}".format(self.optimalPath_length));
        print("*"*20);
    
    @staticmethod
    def displayAdjPheroMtx(self):
        """
        Display the adjacency pheromone matrix in the console
        """
        print("Adjacency phero mtx:")
        for elmt in self.adjPheroMtx:
            print(elmt)