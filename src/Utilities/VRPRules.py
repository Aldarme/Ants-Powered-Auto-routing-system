'''
Created on 19 mai 2020

@author: promet
'''
from __builtin__ import staticmethod
from Ant_Colony.CommonKnowledge import CommonKnowledge
from random import random
from Utilities.Score import Score
class VRPRules:
    
    @staticmethod
    def randPropRule(scoresList_p):
        PhLg_tab = []
        PhLg_Sum = 0.0
        idx = 0
        rpr      = []   #Random Proportional rule
        rpr_sum  = 0.0  #Random Proportional rule SUM
        bundMark_tab    = []
        rtSc = Score()
        
        #Calculate Pheromones/Length ratio define as Tij * (Nij) for the specified path
        #with Tij = pheromone trail strength ; Nij = 1/Distance between vtxA, vtxB 
        for elmt in scoresList_p:
            for i in range(0, (len(scoresList_p)-1) ):
                tmp = CommonKnowledge.get_pheromones(
                                                            CommonKnowledge.adjMtxGraph.get_vtxIdx( elmt.opt_vtx_path[i] ),
                                                            CommonKnowledge.adjMtxGraph.get_vtxIdx( elmt.opt_vtx_path[i+1] )
                                                          )
                PhLg_tab[idx]   += tmp
                PhLg_Sum        += tmp
        idx += 1        
        
        #Calculate the Random Proportional Rule (RPR) for ant point to be chose as destination
        for elmt in PhLg_tab:
            if PhLg_Sum != 0:
                rpr.append(PhLg_tab[i] / PhLg_Sum)
                rpr_sum += PhLg_tab[i] / PhLg_Sum
        
        #Generate the random Vertex according to the Random Proportional Rule
        if PhLg_Sum == 0:
            rand = random.randint(0, (len(scoresList_p)-1) )    #rand between [0; nbrOfNeighbors-1]
            rtSc = scoresList_p[rand]                           #return the last element of the list (the landmark tarket)
        
        else:
            rand = random.random() #random number between [0.0; 1.0]
            
            #Generate boundary markers
            for i in range(0, len(rpr)):
                if i == 0:
                    bundMark_tab.append( rpr[i] )
                else:
                    bundMark_tab.append( bundMark_tab[i-1] + rpr[i] )            
            
            #Select an edge according to boundary marker
            for i in range(0, len(scoresList_p)):
                if rand <= bundMark_tab[i]:
                    rtSc = scoresList_p[i]
                    break
                        
        return rtSc
    
    