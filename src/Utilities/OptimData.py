'''
Created on 3 juin 2021

@author: promet
'''

class OptimData:
    
    def __init__(self, antID_p, distance_p, energy_p, SOH_marker_p, time_p, volume_p):
        '''
        Object to manipulate optimize data of each ant
        '''
        self.antID = antID_p
        self.distance = distance_p
        self.energy = energy_p
        self.SOH_marker = SOH_marker_p
        self.time = time_p
        self.volume = volume_p