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
    
    def __init__(self, ID_p, vtxBegin_p, vtx_toReach_p):
        self.ID             = ID_p
        self.vtx_begin      = vtxBegin_p        #Vertex where the ant begin in the graph
        self.vtx_toReach    = vtx_toReach_p     #Destination that the ant have to reach in the graph
        self.antState       = State.HANDLE      #Define the state of the ant during the algorithm
        self.vtx_end        = Vertex()          #Next Vertex in the graph the ant have to join
        self.distTravelled  = 0                 #Distance travelled by an ant for a 
        self.vtx_toVisit    = []                #Collection of all remaining vertices of the graph to visit 
        self.vtx_tabuList   = []                #Collection of all visited Vertices, by the ant
        self.vtx_landMark   = []                #Contain the landmark that an ant have to check during a lap
        self.edg_tabuList   = []                #Revoir cette element de dorigo prob, si vraiment utile ? Collection of all visited edges by the ant    
        self.neigb_tabuList = []                #Collection of ant tested neighbors
        
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
        
        #Return the heuristic destination determined by the DorigoProb
        self.vtx_end =  self.dorigo_prob(self.vtx_begin).get_vtx_end()
        
        #Test if the end vertex can be reach
        if self.vtx_end in self.vtx_toVisit:
            self.vtx_tabuList.append(self.vtx_begin)
            self.vtx_toVisit.remove(self.vtx_begin)
            self.distTravelled += CommonKnowledge.adjMtxGraph.get_edglength(self.vtx_begin, self.vtx_end)
            
            #Stop the research if the ant find the Vertex to reach
            if(self.vtx_end.get_ID() == self.vtx_toReach.get_ID() ):
                self.antState = State.RETURNING
                self.vtx_tabuList.append(self.vtx_end)
                self.vtx_toVisit.remove(self.vtx_end)
                self.vtx_begin = self.vtx_end
                #Debug line
                #print("Ant: {}, Path: {}, length: {}".format(self.ID, self.vtx_tabuList, self.distTravelled))
                return False
            
            #Kill the ant if the it is in dead end (No neighbors to visit)
            if len(CommonKnowledge.adjMtxGraph.get_Neighboor_VTX(self.vtx_end)) == 0: #Warning, this case work only for directed graph 
                self.antState   = State.KILLED
                self.vtx_begin  = CommonKnowledge.vtx_begin
                del self.vtx_tabuList[:]        #flush the tabu list
                del self.vtx_toVisit[:]         #flush the to visit list
                self.distTravelled = sys.maxint #flush the total dist. travel
                return False
        
            self.vtx_begin = self.vtx_end   #the ant have to find the next vertex to reach
            self.vtx_end = None             
            return True
        
        else: #The vertex can't be reach, have to find a new one
            
            #Fill the tabu list of tested neighbors
            if len(self.neigb_tabuList) < len(CommonKnowledge.adjMtxGraph.get_Neighboor_VTX(self.vtx_begin)
                and self.vtx_end not in self.neigb_tabuList):
                self.neigb_tabuList.append(self.vtx_end)
                return True
            
            else:
                #The tested neighbors list is full, we kill the ant
                self.antState = State.KILLED
                self.vtx_begin  = CommonKnowledge.vtx_begin
                del self.vtx_tabuList[:]        #flush the tabu list
                del self.vtx_toVisit[:]         #flush the to visit list
                del self.neigb_tabuList[:]      #flush the tested neighbors tabu list
                self.distTravelled = sys.maxint #flush the total dist. travel
                return False             
    
    def dorigo_prob(self, vtx_p):
        """
        Calculate the probability for the next destination 
        """
        neighbors_EDGE  = CommonKnowledge.adjMtxGraph.get_Neighboor_VTX(vtx_p)
        PhLg_tab        = []
        PhLg_Sum        = 0.0
        DorigoProb      = []
        DorigoProb_sum  = 0.0
        bundMark_tab    = []
        rtEdge          = Edge
        
        #Calculate Pheromones/Length ratio define as Tij * (Nij) for all neighbor of the current Vertex
        #with Tij = pheromone trail strength ; Nij = 1/Distance between vtxA, vtxB 
        for elmt in neighbors_EDGE:
            tmp = CommonKnowledge.get_pheromones(CommonKnowledge.adjMtxGraph.get_vtxIdx(elmt.get_vtx_begin()),
                                                 CommonKnowledge.adjMtxGraph.get_vtxIdx(elmt.get_vtx_end())
                                                 )* (1.0 / float(elmt.get_length()))
            PhLg_tab.append(tmp);
            PhLg_Sum += tmp;
        
        #Calculate the Dorigo probability for all neighbor of the current vertex
        for i in range (0, len(neighbors_EDGE)):
            if PhLg_Sum != 0:
                DorigoProb.append(PhLg_tab[i] / PhLg_Sum)
                DorigoProb_sum += PhLg_tab[i] / PhLg_Sum            #according to proba. calc. the sum should == 1
           
        #ToDebug     
        #Generate a random edge according to the Dorigo prob
        if PhLg_Sum == 0:
            rand = random.randint(0, (len(neighbors_EDGE)-1) ) #rand between [0; nbrOfNeighbors 
            rtEdge = neighbors_EDGE[rand]
            self.edg_tabuList.append(rtEdge)
        else:
            rand = random.random() #random number between [0.0; 1.0]
            
            #Generate boundary markers
            for i in range(0, len(DorigoProb)):
                if i == 0:
                    bundMark_tab.append( DorigoProb[i] )
                else:
                    bundMark_tab.append( bundMark_tab[i-1] + DorigoProb[i] )            
            
            #Select an edge according to boundary marker
            for i in range(0, len(neighbors_EDGE)):
                if rand <= bundMark_tab[i]:
                    rtEdge = neighbors_EDGE[i]
                    self.edg_tabuList.append(neighbors_EDGE[i])
                    break
                        
        return rtEdge
    
    def toVisit(self):
        """
        Create lists of vertices to visit for an ant,
        as both the list of all vertices of the graph and the list of landmark points
        """
        self.vtx_toVisit    = CommonKnowledge.adjMtxGraph.get_Vertices()
        self.vtx_landMark   = CommonKnowledge.landmarkList[:] 
    
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
    
"""
def toReach(self):
        
        #Return the heuristic destination determined by the DorigoProb
        self.vtx_end =  self.dorigo_prob(self.vtx_begin).get_vtx_end()
        
        #Test if the end vertex can be reach
        if self.vtx_end in self.vtx_toVisit:
            self.vtx_tabuList.append(self.vtx_begin)    #from the beginning, the starting point is set in the taboo list
            self.vtx_toVisit.remove(self.vtx_begin)
            self.distTravelled += CommonKnowledge.adjMtxGraph.get_edglength(self.vtx_begin, self.vtx_end)
            
            #Kill the ant in the case it arrive in dead end (No neighbors to visit)
            if len(CommonKnowledge.adjMtxGraph.get_Neighboor_VTX(self.vtx_end)) == 0: #Warning, this case work only for directed graph 
                self.antState   = State.KILLED
                self.vtx_begin  = CommonKnowledge.vtx_begin
                del self.vtx_tabuList[:]        #flush the tabu list
                del self.vtx_toVisit[:]         #flush the to visit list
                self.distTravelled = sys.maxint #flush the total dist. travel
                return False
            
            self.vtx_begin = self.vtx_end   #the ant have to find the next vertex to reach
            self.vtx_end = None             
            return True
        
        #Stop the research if the ant find the Vertex to reach
        elif(self.vtx_end.get_ID() == self.vtx_toReach.get_ID() #test if the end point is reach and the landmark list is clear 
              and not self.vtx_landMark):
                self.antState = State.RETURNING
                self.vtx_begin = self.vtx_end
                self.vtx_end = None
                return False
        
        else: #The vertex can't be reach, have to find a new one
            
            #Fill the tabu list of tested neighbors
            if len(self.neigb_tabuList) < len(CommonKnowledge.adjMtxGraph.get_Neighboor_VTX(self.vtx_begin)
                and self.vtx_end not in self.neigb_tabuList):
                self.neigb_tabuList.append(self.vtx_end)
                return True
            
            else:
                #The tested neighbors list is full, we kill the ant
                self.antState = State.KILLED
                self.vtx_begin  = CommonKnowledge.vtx_begin
                del self.vtx_tabuList[:]        #flush the tabu list
                del self.vtx_toVisit[:]         #flush the to visit list
                del self.neigb_tabuList[:]      #flush the tested neighbors tabu list
                self.distTravelled = sys.maxint #flush the total dist. travel
                return False
"""