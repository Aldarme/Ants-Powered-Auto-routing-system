'''
Created on 4 mai 2020

@author: promet
'''
from Algorithms.VRP.ACO.Ant import Ant, State
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge
from pathlib import Path
import sys

class AntCo:
    
    def __init__(self, criterionNbr_p):
        self.antArray = []
        self.create_ants(criterionNbr_p)
        
    
    def create_ants(self, antFactor_p):
        """
        Create an list containing all ants of the colony,
        the ant number is equals to the vertices number
        """
        for i in range(0, CommonKnowledge.adjMtxGraph.size()*antFactor_p):
            self.antArray.append(Ant(i))
    
    def search(self):
        """
        Execute the research process of all ants, one by one
        """
        for ant in self.antArray:
            ant.run()
    
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
                                                   CommonKnowledge.pheromone_update(edg, ant.distTravelled, ant.nrj_capacity)
                                                   )

    def ScoringDistance(self):
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
    
    def ScoringMultiObj(self, DEBUG_p):
        """
        Create an objective score based on all edge constrain used by ants
        """
        localIdxPerf = 0        
        ant_idxPerf = {}
        
        #normalize all constrains to fit [0;100]%
        for ant in self.antArray:
            if(ant.antState != State.KILLED):
                ant.normNRJ = ant.nrj_capacity * 100 / CommonKnowledge.AntInitNrjCapacity
                ant.normDst = ant.distTravelled * 100 / 100 #after basedon the max dist travelled on one of the ants
                ant.perfIdx = ant.normNRJ * ant.normDst
                
                #Analysis of NRJ, Dist couple
                if(ant.perfIdx > localIdxPerf):
                    ant_idxPerf.clear()
                    localIdxPerf = ant.perfIdx
                    ant_idxPerf[ant] = localIdxPerf
                    
                if(DEBUG_p == True):
                    print(ant.normDst)
                    print("{} \r\n".format(ant.normNRJ))
        
        if(DEBUG_p == True):
            print("ant idx perf: {}".format(ant_idxPerf))
    
    
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
            
    def antRound_log(self, consoleLog=False, fileLog=False):
        i = 0
        for ant in self.antArray:
            i += 1
            
            if consoleLog == True:
                if(ant.antState != State.KILLED):
                    print("ant {}".format(i))
                    print("ant's round vertices:{},{} {}".format(CommonKnowledge.vtx_init.get_ID() ,ant.visitedVtx_toString(), CommonKnowledge.vtx_init.get_ID()))
                    print("ant's round distance: {}".format(ant.distTravelled))
                    print("ant's round energy  : {}".format(ant.nrj_capacity))
                    print("\r\n")
                
            if fileLog == True:
                
                #build the relative path leading to "roundLog.txt" file
                path = Path(__file__).parent
                path = "{}{}".format(path.parents[2], "/Logs/")
                
                fo = open(path +"roundLog.txt", "a")
                
                if(ant.antState != State.KILLED):
                    fo.write("Ant {}".format(i) + "\r\n")
                    fo.write("ant's round vertices:{},{} {}".format(CommonKnowledge.vtx_init.get_ID() ,ant.visitedVtx_toString(), CommonKnowledge.vtx_init.get_ID()) + "\r\n")
                    fo.write("Ant's round distance: {}".format(ant.distTravelled) + "\r\n")
                    fo.write("Ant's round energy  : {}".format(ant.nrj_capacity) + "\r\n")
                    fo.write("\r\n")
                    
                # Close opened file
                fo.close()
        
                
                