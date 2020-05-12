'''
Created on 27 avr. 2020

@author: promet
'''

from Simulator.AntEngine import AntEngine
from Ant_Colony.Term_Condition.EnvBasedTerm import EnvBasedTerm

antEngine = AntEngine("0", "7")

tmp = EnvBasedTerm.termCond()
antEngine.AE_start(tmp)