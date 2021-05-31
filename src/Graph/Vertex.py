'''
Created on 27 avr. 2020

@author: promet
'''
from Graph.Label import Label
from numpy import empty

class Vertex:
    
    def __init__(self, ID_p = "empty", packageList_p = []):
        self.__ID = ID_p
        self.__label = Label()
        self.__packageList = packageList_p
        
    def get_ID(self):
        """
        Get the ID of the current Vertex
        """
        return  self.__ID
    
    def set_ID(self, ID_p):
        """
        Set the ID of the current Vertex
        """
        self.__ID = ID_p
        
    def get_label(self):
        """
        Get the ID of the current Vertex
        """
        return  self.__label
    
    def set_label(self, localLabel):
        """
        Set the ID of the current Vertex
        """
        self.__label.setLabel(localLabel)
        
    def labelFlusher(self):
        """
        Flush vertex label
        """
        self.__label.flusher()
        
    def set_packageList(self, packgList_p):
        """
        Set the package list with the given list
        """
        self.__packageList = packgList_p.copy()
        
    def get_packageList(self):
        """
        Return package List
        """
        return self.__packageList
        
    def get_packagesTotalVol(self):
        """
        return total volume of packages
        """
        tmpVol = 0.0
        for elm in self.__packageList:
            tmpVol += elm.volume
        
        return tmpVol
    
    def get_packagesTotalWgt(self):
        """
        return total weight of packages
        """
        tmpWei = 0.0
        for elm in self.__packageList:
            tmpWei += elm.weight
        
        return tmpWei
    
