'''
Created on 18 mai 2020

@author: promet
'''

from Algorithms.VRP.Term_Condition.EnvBased import EnvBased
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge 
from Algorithms.VRP.ACO.AntCo import AntCo

class VRP_Engines:
    
    @staticmethod
    def ECHVRP():
        """
        SOC & SOH Vehicle Routing Problem
        """
        #define the convenable number of iteration
        for i in range(0, EnvBased.termCond()):
            
            CommonKnowledge.interationCnt()
            print("iteration: {}".format(CommonKnowledge.iterationNbr))
            
            #Instantiate the ant colony
            antCo = AntCo(CommonKnowledge.vtx_init)
            
            #let all ants construct a turn (one by one)
            antCo.search()
            
            #Check all ants to find the best turn according to specified criterion(s)
            antCo.Scoring()
            
            #Set all ants to the initial location
            antCo.getBack()