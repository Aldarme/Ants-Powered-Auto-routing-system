'''
Created on 4 mai 2020

@author: promet
'''

from Graph.MtxGraph import MtxGraph
from Graph.Vertex import Vertex
import sys
from numpy import empty

class CommonKnowledge:
    
    vtx_init            = Vertex        #Beginning vertex of all ants (of the AC(O/S) algorithm)
    nbrOfVtx            = 0             #Total number of vertices in the graph
    iterationNbr        = 0             #Current number of iteration for the ant colony algorithm
    #Param. of Ant Colony Algo. 
    evaporation_rate    = 0             #Evaporation coefficient ]0;1] used to update pheromone strength
    optimalPath_length  = 0             #Length of the best path find by an ant
    optimalPath_edg     = []            #Collection of edges making up the best path 
    optimalPath_vtx     = []            #Collection of vertices making up the best path
    adjMtxGraph         = MtxGraph      #Adjacency matrix of Belfort Graph
    adjMtxMidGraph      = MtxGraph      #Adjacency matrix of Middle Graph
    adjPheroMtx         = []            #Adjacency pheromone matrix
    #Param. of electric vehicle
    FEC_lost    = 0.06                      #(FEC) Full Equivalent Cycle - energy lost (%)
    FEC_cnt     = 0                         #(FEC) Full Equivalent Cycle - count number of FEC done by the vehicle
    initSOH     = 100 - (FEC_cnt*FEC_lost)  #(SOH) State of Health of the battery (%) - Tesla model S 90-D 2017
    initSOE     = 82000 * initSOH           #(SOE) State of energy of the battery - Tesla model S 90-D 2017
    minSOE      = initSOE * 20 /100         #minumum allowed % capacity
    maxSOE      = initSOE * 80 /100         #maximum allowed % capacity
    packgVolume = 4.42                      #unit cubic meter
    curbWeight  = 2199                      #unit Kg
    
    #initSOE     = 64000                 #(SOE) State of energy - Kona electri 2019 64 kWh
    #minSOE      = initSOE * 20 /100     #minumum allowed % capacity   
    #maxSOE      = initSOE * 80 /100     #maximum allowed % capacity
    #VolumeCapa  = 3.77                  #unit cubic meter
    
    @staticmethod
    def comnKldg_init(vtx_init_p, evaporationRate_p = 0.2):
        CommonKnowledge.vtx_init = vtx_init_p
        CommonKnowledge.optimalPath_length = sys.maxsize
        CommonKnowledge.evaporation_rate = evaporationRate_p
        
        #Init the adjacency pheromone matrix at the same size that the adjacency matrix, with all elements at "0.0"
        CommonKnowledge.adjPheroMtx = [[0.0 for x in range(CommonKnowledge.adjMtxMidGraph.size())] for y in range(CommonKnowledge.adjMtxMidGraph.size())]
        
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
    def get_adjMtxGraph():
        """
        
        """
        return CommonKnowledge.adjMtxGraph
    
    @staticmethod
    def adjMtxMidGraph():
        """
        
        """
        return CommonKnowledge.adjMtxMidGraph
    
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
    def pheromone_update(edg_p, SOE_p, SOHmarker_p, totalDist_p, totalTime_p, remainingVolume_p):
        """
        Calculate the evaporation rate of pheromones for the given edge, according to the following equation:
        [(1-p) * PheromoneStrength] + turnSize
        """
        print("SOE: {}".format(SOE_p))
        print("SOHmarker: {}".format(SOHmarker_p))
        print("totalDist: {}".format(totalDist_p))
        print("totalTime: {}".format(totalTime_p))
        print("remainingVolume: {}".format(remainingVolume_p))
        
        pheromeij = CommonKnowledge.adjPheroMtx[CommonKnowledge.adjMtxMidGraph.get_vtxIdx(edg_p.get_vtx_begin())][CommonKnowledge.adjMtxMidGraph.get_vtxIdx(edg_p.get_vtx_end())]
        return (pheromeij + ( (1.0 / SOE_p) * (1.0/SOHmarker_p) * (1/remainingVolume_p) * (totalDist_p) * (totalTime_p)  ))
    
    
    @staticmethod
    def pheroUpdt_objFct(edg_p, SOE_p, SOHmarker_p, totalDist_p, totalTime_p, remainingVolume_p):
        """
        Calculate the evaporation rate of pheromones for the given edge, according to objective function,
        using normalize parameters and a linear function
        """
        
        #normalize all marker between [0; 100]
        SOE     = CommonKnowledge.norm(SOE_p, 0, 82000, 0, 100)
        SOH     = CommonKnowledge.norm(SOHmarker_p, 0, 70, 0, 100)
        Dist    = CommonKnowledge.norm(totalDist_p, 0, 130, 0, 100)
        Time    = CommonKnowledge.norm(totalTime_p, 0, 468, 0, 100)
        Vol     = CommonKnowledge.norm(remainingVolume_p, 0, 4.42, 0, 100)
        
        if False:
            print("SOE_p: {}, SOE: {}".format(SOE_p, SOE))
            print("SOHmarker_p: {}, SOHmarker: {}".format(SOHmarker_p, SOH))
            print("totalDist_p: {}, totalDist: {}".format(totalDist_p, Dist))
            print("totalTime_p: {}, totalTime: {}".format(totalTime_p, Time))
            print("remainingVolume_p: {}, remainingVolume: {}".format(remainingVolume_p, Vol))
        
        #linear objective function between [0; 500] to normalize between [0; 1]
        linObjFct = ( (SOE * 0.004) + (SOH * 0.003) + (Dist * 0.001) + (Time * 0.001) + (Vol * 0.001) )
        print(linObjFct)
        
        pheromeij = CommonKnowledge.adjPheroMtx[CommonKnowledge.adjMtxMidGraph.get_vtxIdx(edg_p.get_vtx_begin())][CommonKnowledge.adjMtxMidGraph.get_vtxIdx(edg_p.get_vtx_end())]
        return (pheromeij + ( 1/linObjFct ))
    
    @staticmethod
    def pheromone_normUpd(edg_p, SOE_p, SOHmarker_p, totalDist_p, totalTime_p, remainingVolume_p):
        """
        Calculate the evaporation rate of pheromones for the given edge, according to the following equation:
        [(1-p) * PheromoneStrength] + turnSize
        """
        pheromeij = CommonKnowledge.adjPheroMtx[CommonKnowledge.adjMtxMidGraph.get_vtxIdx(edg_p.get_vtx_begin())][CommonKnowledge.adjMtxMidGraph.get_vtxIdx(edg_p.get_vtx_end())]
        return (pheromeij + ( (1.0 / SOE_p) * (1.0/SOHmarker_p) * (1/remainingVolume_p) * (totalDist_p) * (totalTime_p)  ))
    
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
        del CommonKnowledge.adjMtxMidGraph[:]
    
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
            
    @staticmethod
    def norm(x, in_min, in_max, out_min, out_max):
        """
        Normalize value between new data range
        """
        if x > in_max:
            out_max = 100
            
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    
    
    
    