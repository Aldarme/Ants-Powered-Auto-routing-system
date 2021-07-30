'''
Created on 3 juin 2021

@author: promet
'''

import sys

class OptimData:
    
    def __init__(self, antID_p=0, distance_p=sys.float_info.max, energy_p=sys.float_info.max, SOH_marker_p=sys.float_info.max, time_p=sys.float_info.max, volume_p=sys.float_info.max, turnCnt_p=sys.float_info.max, deliveryPath_p=''):
        '''
        Object to manipulate optimize data of each ant
        '''
        self.antID = antID_p
        self.distance = distance_p
        self.energy = energy_p
        self.SOH_marker = SOH_marker_p
        self.time = time_p
        self.volume = volume_p
        self.turnCnt = turnCnt_p
        self.deliveryPath = deliveryPath_p