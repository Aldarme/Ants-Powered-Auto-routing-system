'''
Created on 25 mai 2020

@author: promet
'''
from __builtin__ import staticmethod
from Crypto.Random.random import randint

class Delivery:
    
    cycle = []
    objList = []
    notDelObj = []
    idx = 0
    
    @staticmethod
    def init():
        Delivery.cycle.append(rate(8, 12))
        Delivery.cycle.append(rate(5, 8))
        Delivery.cycle.append(rate(7, 10))
        Delivery.cycle.append(rate(3, 5))
        Delivery.cycle.append(rate(2, 3))
        Delivery.cycle.append(rate(4, 6))
    
    @staticmethod
    def rand():
        return randint(0, 10) #temps d'attente aleatoire entre 0 et 10 minutes
    
    @staticmethod
    def writeFile(fileName_p, myObj):
        
        with open("/media/Stock/Workspaces/Py_WS/Ants Powered Auto-routing system/src/Logs/{}".format(fileName_p), "a+") as file:
            file.write("Colis: {}\n".format(Delivery.idx))
            file.write("distance: {}\n".format(myObj.dist))
            file.write("time: {}\n".format(myObj.time))
            file.write("\n\n")
        
    @staticmethod
    def fstStrat_run():
        
        tmp_time = 0
        tmp_dist = 0
        
        #Pour chaque colis, on stock la distance parcouru et le temps de deplacement
        for elmt in Delivery.cycle:
            tmp_time += elmt.time
            tmp_dist += elmt.dist
            Delivery.objList.append(rate(tmp_dist, tmp_time))
        
        #On stock dans un fichier de log
        for elmt in Delivery.objList:
            Delivery.writeFile("ColisCycle_strat1_Logs.txt", elmt)
            Delivery.idx += 1
            
    
    @staticmethod
    def scdStrat_run():
        
        tmp_time = 0
        tmp_dist = 0
        
        #Pour chaque colis, on stock la distance parcouru et le temps de deplacement
        for i in range(0, len(Delivery.cycle)): 
            tmp_dist += Delivery.cycle[i].dist
            rand = Delivery.rand()
            
            if (i == len(Delivery.cycle)-1 ):
                tmp_time += Delivery.cycle[i].time
                Delivery.objList.append(rate(tmp_dist, tmp_time))
                Delivery.cycle[i].delivered = True
            
            else:
                if rand <= 2:                   #delivre sans temps d'attente
                    tmp_time += Delivery.cycle[i].time
                    Delivery.objList.append(rate(tmp_dist, tmp_time))
                    Delivery.cycle[i].delivered = True
                    
                if rand >= 3 and rand <=7:      #delivre avec temps attente
                    tmp_time += Delivery.cycle[i].time + rand
                    Delivery.objList.append(rate(tmp_dist, tmp_time))
                    Delivery.cycle[i].delivered = True
                    
                if rand >= 8 and rand <= 10:    #non delivre
                    tmp_time += Delivery.cycle[i].time + rand
                    Delivery.objList.append(rate(tmp_dist, tmp_time))
                    Delivery.notDelObj.append(Delivery.cycle[i])
        
        #On stock dans un fichier de log
        for elmt in Delivery.objList:
            Delivery.writeFile("ColisCycle_strat2_Logs.txt", elmt)
            Delivery.idx += 1
            
        Delivery.writeFile("ColisCycle_strat2_Logs.txt", rate(0, 0))
        Delivery.idx = 100    
            
        #On stock dans un fichier de log
        for elmt in Delivery.notDelObj:
            Delivery.writeFile("ColisCycle_strat2_Logs.txt", elmt)
            Delivery.idx += 1





class rate:
    
    def __init__(self, dist_p=0, time_p=0, delivered_p = False ):
        self.dist = dist_p
        self.time = time_p
        self.delivered = delivered_p
        