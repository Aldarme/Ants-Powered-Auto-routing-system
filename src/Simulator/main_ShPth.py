'''
Created on 27 avr. 2020

@author: promet
'''

from Algorithms.ShPath_ACO.ShPath_Engines import ShPath_Engines
from Algorithms.ShPath_ACO.ACO.CommonKnowledge import CommonKnowledge


CommonKnowledge.commonKnldg_init(vtxBegin_p, vtx_toReach_p)

#Init the ant engine
ShPath_Engines = ShPath_Engines("0", "7")

#Start the ant engine
ShPath_Engines.ShP_start()