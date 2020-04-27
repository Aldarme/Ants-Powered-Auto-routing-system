'''
Created on 27 avr. 2020

@author: promet
'''

class Vertex:
    
    __ID = ""
    
    def __init__(self, ID_p = "empty"):
        self.__ID = ID_p
    
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