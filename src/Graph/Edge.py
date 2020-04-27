'''
Created on 27 avr. 2020

@author: promet
'''

import Vertex as vtx

class Edge:
    
    __length = 0
    __vtx_begin = vtx
    __vtx_end = vtx
    
    def __init__(self, lgth_p = 0, vtx_beg_p = vtx, vtx_end_p = vtx):
        self.__length = lgth_p
        self.__vtx_begin = vtx_beg_p
        self.__vtx_end = vtx_end_p
    
    def set_length(self, lgth_p):
        """
        Set the length value
        """
        self.__length = lgth_p
    
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
    
    def toString(self):
        """
        Convert class properties into a String 
        """
        return "This edge begin at: {}, end at: {}, with a cost of: {}".format(self.__vtx_begin, self.__vtx_end, self.__length)