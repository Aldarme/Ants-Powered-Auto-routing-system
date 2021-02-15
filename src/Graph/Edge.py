'''
Created on 27 avr. 2020

@author: promet
'''

from Graph import Vertex as vtx
#from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge

class Edge:
    
    """
    Init object parameters value
    By default, nrj_cost is init at 0,25 kwh/km, according to data exploitation
    """
    def __init__(self, length_p = 0, vtx_begin_p = vtx, vtx_end_p = vtx, nrj_cost_p = 0.1): #0.25 is for test app. thanks to Romain's data.
        self.__length       = length_p      #distance Unit: Km
        self.__vtx_begin    = vtx_begin_p
        self.__vtx_end      = vtx_end_p        
        self.__nrj_cost     = nrj_cost_p    #Nrj unit: KWH/Km
    
    def set_length(self, length_p):
        """
        Set the length value
        """
        self.__length = length_p
    
    def set_vtx_begin(self, vtx_p):
        """
        Set the beginning vertex object
        """
        self.__vtx_begin = vtx_p
    
    def set_vtx_end(self, vtx_p):
        """
        Set the ending vertex object
        """
        self.__vtx_end = vtx_p
        
    def get_length(self):
        """
        Get the length value
        """
        return self.__length
    
    def get_vtx_begin(self):
        """
        Get the beginning vertex object
        """
        return self.__vtx_begin
    
    def get_vtx_end(self):
        """
        Get the ending vertex object
        """
        return  self.__vtx_end
    
    def get_nrj_cost(self):
        """
        Get the nrj cost of the edge
        """
        return self.__nrj_cost 
    
    def toString(self):
        """
        Convert class properties into a String 
        """
        return "This edge begin at: {}, end at: {}, with a cost of: {}".format(self.__vtx_begin, self.__vtx_end, self.__length)