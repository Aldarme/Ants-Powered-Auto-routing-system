'''
Created on 18 mai 2020

@author: promet
'''

from Algorithms.VRP.Term_Condition.EnvBased import EnvBased
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge 
from Algorithms.VRP.ACO.AntCo import AntCo
from Simulator.DEBUG import DEBUG_MODE

class VRP_Engines:
    
    @staticmethod
    #ESCSHVRP: Electric State of Charge, State of Health Vehicle Routing Problem 
    def ESCSHVRP(nbrOfCriterion_p = 1):
        """
        SOC & SOH Vehicle Routing Problem
        """
        #determine the appropriate number of iterations
        for i in range(0, EnvBased.termCond() * nbrOfCriterion_p):
            
            CommonKnowledge.interationCnt()
            if DEBUG_MODE:
                print("iteration: {}".format(CommonKnowledge.iterationNbr))
            
            #Instantiate the ant colony
            antCo = AntCo(nbrOfCriterion_p)
            
            #let all ants construct a turn (one by one)
            antCo.search()
            
            #log in console and file generated path of each ant (consolog, filog)
            antCo.antRound_log(True, False)
            
            #Set all ants to the initial location
            antCo.getBack()
            
            #Check all ants to find the most appropriate energy/distance couple
            antCo.ScoringMultiObj(True)
            
            