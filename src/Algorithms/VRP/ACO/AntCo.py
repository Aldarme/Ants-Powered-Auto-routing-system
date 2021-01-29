'''
Created on 4 mai 2020

@author: promet
'''
from Algorithms.VRP.ACO.Ant import Ant, State
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge

class AntCo:
    
    def __init__(self):
        self.antArray = []
        self.create_ants()
        
    
    def create_ants(self):
        """
        Create an list containing all ants of the colony,
        the ant number is equals to the vertices number
        """
        for i in range(0, CommonKnowledge.adjMtxGraph.size()):
            self.antArray.append(Ant(i))
    
    def search(self):
        """
        Execute the research process of all ants, one by one
        """
        for ant in self.antArray:
            ant.run()
        
    def Scoring(self):
        """
        Determine and save the best traveled path (min distance) made by an ant
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
        Update the pheromone strength of all edges in the graph
        Allow each ant to add pheromone on the arcs it has visited
        Put in return state, all ants that have finished its tour
        """
        
        CommonKnowledge.pheromone_lowering()
        
        for ant in self.antArray:
            if ant.antState == State.RETURNING:
                for edg in ant.edg_tabuList:
                    CommonKnowledge.set_pheromones(CommonKnowledge.adjMtxGraph.get_vtxIdx(edg.get_vtx_begin()),
                                                   CommonKnowledge.adjMtxGraph.get_vtxIdx(edg.get_vtx_end()),
                                                   CommonKnowledge.pheromone_update(edg, ant.distTravelled)
                                                   )

    def localSearch(self):
        """
        Apply a local search, after an ant finished a turn
        """
        pass
    
    def antsDisplay(self):
        """
        Display the vertices list of each ant of the colony
        """
        for ant in self.antArray:
            print("ant: {}".format(ant.get_antVertices_toString()))
            