'''
Created on 27 avr. 2020

@author: promet
'''

from Simulator.AntEngine import AntEngine
from Ant_Colony.Term_Condition.EnvBasedTerm import EnvBasedTerm

#Init the ant engine
antEngine = AntEngine("0", "7")

#Start the ant engine
antEngine.ACO_start(EnvBasedTerm.termCond())