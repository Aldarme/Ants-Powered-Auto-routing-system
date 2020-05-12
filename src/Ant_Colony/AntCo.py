'''
Created on 4 mai 2020

@author: promet
'''
from Ant_Colony.Ant import Ant, State
from Ant_Colony.CommonKnowledge import CommonKnowledge

class AntCo:
    
    def __init__(self, vtxBegin_p, vtx_toReach_p):
        self.antArray = []
        self.create_ants(vtxBegin_p, vtx_toReach_p)
        
    
    def create_ants(self, vtxBegin_p, vtx_toReach_p):
        """
        Create an list containing all ants of the colony
        """
        for i in range(0, CommonKnowledge.adjMtxGraph.size()):
            self.antArray.append(Ant(i, vtxBegin_p, vtx_toReach_p))
    
    def search(self):
        """
        Execute the research process of all ants, one by one
        """
        for ant in self.antArray:
            ant.run()
        
    def Scoring(self):
        """
        Determine and save the best traveled path made by an ant
        """
        for ant in self.antArray:
            if ant.distTravelled < CommonKnowledge.optimalPath_length:
                CommonKnowledge.optimalPath_length = ant.distTravelled  #store the length of the best path
                CommonKnowledge.optimalPath_edg = ant.edg_tabuList      #store the edge making up the best path
        
        CommonKnowledge.get_vtxOptimalPath()
        
        print("Optimal path: {}".format(CommonKnowledge.optimalPath_VTX_toString()))
        print("Optimal length: {}".format(CommonKnowledge.optimalPath_length))
    
    def getBack(self):
        """
        Allow to all ants that have finished its tour, to get back at the beginning point
        & apply pheromones to their path
        """
        for ant in self.antArray:
            if ant.antState == State.RETURNING:
                for edg in ant.edg_tabuList:
                    CommonKnowledge.set_pheromones(CommonKnowledge.adjMtxGraph.get_vtxIdx(edg.get_vtx_begin()),
                                                   CommonKnowledge.adjMtxGraph.get_vtxIdx(edg.get_vtx_end()),
                                                   CommonKnowledge.dorigo_evaporation(edg, ant.distTravelled)
                                                   )
        
        #apply evaporation rate
    
    def localSearch(self):
        """
        Apply a local search, after an ant finished a lap
        """
        pass
    
    def antsDisplay(self):
        """
        Display each ant of the colony and its list of vertices
        """
        for ant in self.antArray:
            print("ant: {}".format(ant.get_antVertices_toString()))