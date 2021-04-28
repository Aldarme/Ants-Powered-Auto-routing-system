'''
Created on 27 avr. 2020

@author: promet
'''
from Graph.Label import Label

class Vertex:
    
    def __init__(self, ID_p = "empty"):
        self.__ID = ID_p
        self.__label = Label()
        
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