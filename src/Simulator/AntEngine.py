'''
Created on 6 mai 2020

@author: promet
'''
from Ant_Colony.Ant import Ant
from Graph.Vertex import Vertex
from Graph.Edge import Edge
from Ant_Colony.CommonKnowledge import CommonKnowledge
from Graph.MtxGraph import MtxGraph
from Ant_Colony.AntCo import AntCo


class AntEngine:
    
    
    
    def __init__(self, ID_vtx_begin_p, ID_vtx_toReach_p):
        
        self.vtxList = []
        self.edgList = []
                
        #create vertices
        for i in range(0, 8):
            self.vtxList.append(Vertex(i))
        
        self.edgList.append(Edge(8, self.vtxList[0], self.vtxList[1]))
        self.edgList.append(Edge(4, self.vtxList[0], self.vtxList[2]))
        self.edgList.append(Edge(1, self.vtxList[2], self.vtxList[1]))
        self.edgList.append(Edge(5, self.vtxList[1], self.vtxList[3]))
        self.edgList.append(Edge(2, self.vtxList[2], self.vtxList[4]))
        self.edgList.append(Edge(4, self.vtxList[4], self.vtxList[3]))
        self.edgList.append(Edge(3, self.vtxList[3], self.vtxList[6]))
        self.edgList.append(Edge(9, self.vtxList[7], self.vtxList[3]))
        self.edgList.append(Edge(7, self.vtxList[3], self.vtxList[5]))
        self.edgList.append(Edge(3, self.vtxList[4], self.vtxList[5]))
        self.edgList.append(Edge(1, self.vtxList[6], self.vtxList[7]))
        self.edgList.append(Edge(2, self.vtxList[5], self.vtxList[7]))
        
        #instantiate the adjacency matrix
        CommonKnowledge.adjMtxGraph = MtxGraph(len(self.vtxList))
        
        #insert vertices in the adjacency matrix
        for vtx in self.vtxList:
            CommonKnowledge.adjMtxGraph.insert_vtx(vtx)
        
        #insert edges in the adjacency matrix
        for edg in self.edgList:
            CommonKnowledge.adjMtxGraph.insert_edg_EDGE(edg)
        
        #debug
        #display the adjacency matrix for verification
        for elmt in CommonKnowledge.adjMtxGraph.get_adjMtx():
            print("{}".format(elmt))
        
        #define the beginning point and the point to reach for the ants
        CommonKnowledge.commonKnldg_init(self.vtxList[0], self.vtxList[7])  #CommonKnowledge.adjMtxGraph.contain_vtx(ID_vtx_begin_p) #CommonKnowledge.adjMtxGraph.contain_vtx(ID_vtx_toReach_p)
        
        
    def AE_start(self, itNumb):
        
        for i in range(0, itNumb):
            
            CommonKnowledge.incr_IntNumber()
            print("iteration number: {}".format(CommonKnowledge.iterationNbr))
            
            # Instantiate the Ant COlony
            antCo = AntCo(CommonKnowledge.vtx_begin, CommonKnowledge.vtx_toReach)
            
            # Let all ants construct a lap (one by one)
            antCo.search()
            
            # Check all ants to find the best shortest path
            antCo.Scoring()
            
            # Apply local search
            
            # All ants return to their beginning point
            antCo.getBack()
        
        
    
    
    
    
    
    
    
    
        