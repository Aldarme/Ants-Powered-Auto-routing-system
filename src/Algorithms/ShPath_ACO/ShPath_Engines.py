'''
Created on 6 mai 2020

@author: promet
'''

from Algorithms.ShPath_ACO.ACO.CommonKnowledge import CommonKnowledge
from Algorithms.ShPath_ACO.ACO.AntCo import AntCo
from Algorithms.ShPath_ACO.Term_Condition.EnvBased import EnvBased


class ShPath_Engines:
    
    @staticmethod
    def ShP_start():
        """
        Ant Colony Optimization application core
        """
        for i in range(0, EnvBased.termCond()):
            
            CommonKnowledge.incr_Interation()
            print("iteration number: {}".format(CommonKnowledge.iterationNbr))
            
            # Instantiate the Ant Colony
            antCo = AntCo(CommonKnowledge.vtx_begin, CommonKnowledge.vtx_toReach)
            
            # Let all ants construct a turn (one by one)
            antCo.search()
            
            # Check all ants to find the best shortest path
            antCo.Scoring()
            
            # Apply local search
            
            # All ants return to their beginning point
            antCo.getBack()
    
    
    
    
    
    
    
    
        