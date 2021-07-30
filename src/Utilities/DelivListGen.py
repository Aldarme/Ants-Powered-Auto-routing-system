"""
Created on 31 mai 2021

@author: promet
"""
import random
from Utilities.PackgListGen import PackgListGen
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge

class DelivListGen:
    
    #Graph of belfort is composed of 142 vertices
    buStop = []
    
    debugList = ["Madrid", "Foch", "République", "Briand", "Mairie", "Follereau"]
    
    @staticmethod
    def build():
        """
        Generate buStop String list,
        based on vertices list of the Adjacency matrix
        """
        
        for elm in CommonKnowledge.adjMtxGraph.get_Vertices():
            DelivListGen.buStop.append(elm.get_ID())
            
        #for elm in DelivListGen.buStop:
        #    print(elm)
            
        #print(len(DelivListGen.buStop))
    
    @staticmethod
    def run(delivPtsNbr_p = 1, warehouse_string_p=""):
        """
        Select wanted number of delivery point
        """
        #Build BuStop String list
        DelivListGen.build()
        
        #remove the deposit vertex to avoid Dijkstra to search on it and crash
        DelivListGen.buStop.remove(warehouse_string_p)
        
        finalList = []
        
        #get specific number of bus Stop, according to the parameter
        for i in range(0, delivPtsNbr_p):
            tmpString = random.choice(DelivListGen.buStop)
            finalList.append(tmpString)
            DelivListGen.buStop.remove(tmpString)
        
        return finalList
    

      