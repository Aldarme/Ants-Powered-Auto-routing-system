'''
Created on 25 mai 2020

@author: promet
'''
from Strategies.Delivery import Delivery

class Engine:
    
    @staticmethod
    def fstStrat_run():
        Engine.init_datas()
        Delivery.fstStrat_run()
        
    @staticmethod
    def scdStrat_run():
        Engine.init_datas()
        Delivery.scdStrat_run()
        
    @staticmethod
    def init_datas():
        Delivery.init()


#Engine.fstStrat_run()

Engine.scdStrat_run()