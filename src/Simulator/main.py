'''
Created on 27 avr. 2020

@author: promet
'''

from Ant_Colony.AntCo_Engines import AntCo_Engines
from Ant_Colony.Term_Condition.EnvBased import EnvBased

#Init the ant engine
antCo_Engine = AntCo_Engines("0", "7")

#Start the ant engine
antCo_Engine.ACO_start( EnvBased.termCond() )