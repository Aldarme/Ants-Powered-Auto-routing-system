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
        
        #Instantiate the ant colony
        antCo = AntCo(nbrOfCriterion_p)
        
        #determine the appropriate number of iterations
        for i in range(0, EnvBased.termCond() * nbrOfCriterion_p): 
            
            #reset properties of each ant
            for elm in antCo.antArray:
                elm.resetter()
            
            #let all ants construct a turn (one by one)
            antCo.search()
            
            #calculate SOH maker turn
            antCo.SOHmarkers_calc()
            
            #log in console and/or file generated path of each ant (consolog, filog)
            antCo.antRound_log(True, False, i)
            
            #update pheromone trail and set all ants at the initial deposit location
            antCo.getBack()
            
            #display the adj. pheromone matrix to see update
            
        
        #Check all ants to find the most appropriate energy/distance couple
        print('##################################')
        print('Final result')
        print('##################################')
        
        #log in console and/or file, final path of each ant and the best path (consoleLog, fileLog)
        # TODO antCo.ScoringMultiObj(True, False)
            
            