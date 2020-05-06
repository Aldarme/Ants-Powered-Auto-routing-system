'''
Created on 4 mai 2020

@author: promet
'''

from Graph.Vertex import Vertex
from Ant_Colony.CommonKnowledge import CommonKnowledge
from Graph.Edge import Edge
import random
import sys

class Ant:
    
    ID = 0
    distTravelled = 0
    vtx_begin     = Vertex()  #Vertex where the ant begin in the graph
    vtx_end       = Vertex()  #Next Vertex in the graph the ant have to join
    vtx_toReach   = Vertex()  #Destination that the ant have to reach in the graph
    antState      = None
    Stg_tabuList  = []        #Collection of all visited Vertices as ID, by the ant
    edg_tabuList  = []        #Collection of all visited edges by the ant
    Stg_toVisit   = []        #Collection of all remaining vertices as ID, of the graph to visit 
    neigb_tabuList = []       #Collection of ant tested neighbors
    
    
    def __init__(self, ID_p = -1, vtxBegin_p, vtx_toReach_p):
        self.antState     = State.HANDLE
        self.ID           = ID_p
        self.vtx_begin    = vtxBegin_p
        self.vtx_toReach  = vtx_toReach_p
        self.toVisit()
    
    def run(self):
        """
        Start the research process for an ant
        """
        self.antState =State.SEARCHING_PATH
        while(self.toReach()):
            pass
        
    def toReach(self):
        """
        Define how an ant build a path between start & toReach vertex
        """
        tmp_vtxBegin = self.vtx_begin
        
        #Return the heuristic destination determined by the DorigoProb
        self.vtx_end =  self.dorigo_prob(self.vtx_begin).get_vtx_end()
        
        #Test if the end vertex can be reach
        if self.vtx_end.get_ID() in self.Stg_toVisit:
            self.Stg_tabuList.append(self.vtx_begin.get_ID())
            self.Stg_toVisit.remove(self.Stg_tabuList[-1])
            self.distTravelled += CommonKnowledge.adjMtxGraph.get_edglength(self.vtx_begin, self.vtx_end)
            
            #Stop the research if the ant find the Vertex to reach
            if(self.vtx_end.get_ID() == self.vtx_toReach.get_ID() ):
                self.antState = State.RETURNING                     #put the ant in returning state
                self.Stg_tabuList.append(self.vtx_end.get_ID())
                self.Stg_toVisit.remove(self.Stg_tabuList[-1])
                self.vtx_begin = self.vtx_end
                #Debug line
                #print("Ant: {}, Path: {}, length: {}".format(self.ID, self.Stg_tabuList, self.distTravelled))
                return False
            
            #Kill the ant if the it is in dead end (No neighbors to visit)
            if len(CommonKnowledge.adjMtxGraph.getNeighboor_VTX(self.vtx_end)) == 0:
                self.antState   = State.KILLED
                self.vtx_begin  = tmp_vtxBegin   #think about it
                del self.Stg_tabuList[:]
                del self.Stg_toVisit[:]
                self.distTravelled = sys.maxint
                return False
        
            self.vtx_begin = self.vtx_end
            self.vtx_end = None
            return True
        
        else:
            #test if the number of tested neighbor is inf. to the number of neighbors & was not previously tested
            if len(self.neigb_tabuList) < len(CommonKnowledge.adjMtxGraph.getNeighboor_VTX(self.vtx_begin)
                and self.vtx_end not in self.neigb_tabuList):
                self.neigb_tabuList.append(self.vtx_end)
                return True
            
            else:
                #Kill the current ant, it already tested all neighbors
                self.antState = State.KILLED
                return False                
            
    
    def dorigo_prob(self, vtx_p):
        """
        Calculate the probability for the next destination 
        """
        neighbors   = CommonKnowledge.adjMtxGraph.getNeighboor_VTX(vtx_p)
        dico_neigbProb = {}
        PhLg_tab    = []
        DorigoProb  = []
        neighborSum = 0.0;
        rtEdge      = Edge
        
        #Calculate PhLg ratio for all neighbor of the current Vertex
        for elmt in neighbors:
            tmp = CommonKnowledge.get_pheromones(CommonKnowledge.adjMtxGraph.get_vtxIdx(elmt.get_vtx_begin()),
                                                 CommonKnowledge.adjMtxGraph.get_vtxIdx(elmt.get_vtx_end())
                                                 )/ (1.0 / float(elmt.get_length()))
        PhLg_tab.add(tmp);
        neighborSum += tmp;
        
        #Calculate the Dorigo probability for all neighbor of the current vertex
        for i in range (0, len(neighbors)):
            if neighborSum == 0:
                DorigoProb.append(0.0)
            else:
                dico_neigbProb[PhLg_tab[i] / neighborSum] = neighbors[i]
                DorigoProb.append(PhLg_tab[i] / neighborSum)
        
        if neighborSum == 0:
            rand = random.randint(neighborSum, len(neighbors)) # [0;X]
            randEdg = neighbors[rand]
            self.__edg_tabuList.append(neighbors[randEdg])
        else:
            #Sort Dorigo Prob List
            DorigoProb.sort()
            
            #Generate random number
            randNbr = float(random.randint(int(neighborSum), int(round(DorigoProb[len(DorigoProb)-1], 0))) ) / 100.0 # [0;X]
        
            #Use generated random number to define the next Vertex to reach
            for PhLg_ratio in DorigoProb:
                if randNbr <= PhLg_ratio:
                    rtEdge = dico_neigbProb.get(PhLg_ratio)
                    self.__edg_tabuList.append(rtEdge)
                    break
        
        return rtEdge
    
    def toVisit(self):
        """
        Create the vtx_toVisit collection for each ant
        """
        for elmt in CommonKnowledge.adjMtxGraph.get_Vertices():
            self.vtx_toVisit.append(elmt)
    
    def get_antVertices_toString(self):
        """
        Return the parameters vertices of an Ant
        """
        return "Beginning Vertex: {}, To reach Vertex: {}, ending Vertex: {}".format(self.vtx_begin, self.vtx_toReach, self.vtx_end)


class State:
    """
    This enumeration define the current ant state over the course of the ant colony algorithm 
    """
    HANDLE          = 1
    SEARCHING_PATH  = 2
    RETURNING       = 3
    KILLED          = 4