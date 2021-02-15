'''
Created on 21 mai 2020

@author: promet
'''

from Graph.Vertex import Vertex
from Graph.Edge import Edge
from Graph.MtxGraph import MtxGraph
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge


class GpTest:
    
    vtxList = []
    edgList = []
    
    DEBUG = False
    
    @staticmethod
    def create( warehouse_p ):
        """
        Initialize the graph test
        """
               
        #Create vertices
        for i in range(0, 8):
            GpTest.vtxList.append(Vertex(i))
        
        #True:  Directed Graph
        #False: Undirected Graph
        bool = False
        
        if bool == True:
            
            #Test graph 1
            #Directed graph
            #Composed of a small number of vertices and a low number of edges (average of one edge by couple of vertices)
            GpTest.edgList.append(Edge(8, GpTest.vtxList[0], GpTest.vtxList[1]))
            GpTest.edgList.append(Edge(4, GpTest.vtxList[0], GpTest.vtxList[2]))
            GpTest.edgList.append(Edge(1, GpTest.vtxList[2], GpTest.vtxList[1]))
            GpTest.edgList.append(Edge(5, GpTest.vtxList[1], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(2, GpTest.vtxList[2], GpTest.vtxList[4]))
            GpTest.edgList.append(Edge(4, GpTest.vtxList[4], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(3, GpTest.vtxList[3], GpTest.vtxList[6]))
            GpTest.edgList.append(Edge(9, GpTest.vtxList[7], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(7, GpTest.vtxList[3], GpTest.vtxList[5]))
            GpTest.edgList.append(Edge(3, GpTest.vtxList[4], GpTest.vtxList[5]))
            GpTest.edgList.append(Edge(1, GpTest.vtxList[6], GpTest.vtxList[7]))
            GpTest.edgList.append(Edge(2, GpTest.vtxList[5], GpTest.vtxList[7]))
        
        if bool == False:
            
            #Test graph 2
            #Undirected graph (Not fully undirected)
            #Composed of a small number of vertices and a significant number of edges
            GpTest.edgList.append(Edge(8, GpTest.vtxList[0], GpTest.vtxList[1]))
            GpTest.edgList.append(Edge(4, GpTest.vtxList[0], GpTest.vtxList[2]))
            GpTest.edgList.append(Edge(8, GpTest.vtxList[1], GpTest.vtxList[0]))
            GpTest.edgList.append(Edge(1, GpTest.vtxList[1], GpTest.vtxList[2]))
            GpTest.edgList.append(Edge(5, GpTest.vtxList[1], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(4, GpTest.vtxList[2], GpTest.vtxList[0]))
            GpTest.edgList.append(Edge(1, GpTest.vtxList[2], GpTest.vtxList[1]))
            GpTest.edgList.append(Edge(2, GpTest.vtxList[2], GpTest.vtxList[4]))
            GpTest.edgList.append(Edge(5, GpTest.vtxList[3], GpTest.vtxList[1]))
            GpTest.edgList.append(Edge(4, GpTest.vtxList[3], GpTest.vtxList[4]))
            GpTest.edgList.append(Edge(7, GpTest.vtxList[3], GpTest.vtxList[5]))
            GpTest.edgList.append(Edge(3, GpTest.vtxList[3], GpTest.vtxList[6]))
            GpTest.edgList.append(Edge(9, GpTest.vtxList[3], GpTest.vtxList[7]))
            GpTest.edgList.append(Edge(2, GpTest.vtxList[4], GpTest.vtxList[2]))
            GpTest.edgList.append(Edge(4, GpTest.vtxList[4], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(3, GpTest.vtxList[4], GpTest.vtxList[5]))
            GpTest.edgList.append(Edge(7, GpTest.vtxList[5], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(3, GpTest.vtxList[5], GpTest.vtxList[4]))
            GpTest.edgList.append(Edge(2, GpTest.vtxList[5], GpTest.vtxList[7]))
            GpTest.edgList.append(Edge(3, GpTest.vtxList[6], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(1, GpTest.vtxList[6], GpTest.vtxList[7]))
            GpTest.edgList.append(Edge(9, GpTest.vtxList[7], GpTest.vtxList[3]))
            GpTest.edgList.append(Edge(2, GpTest.vtxList[7], GpTest.vtxList[5]))
            GpTest.edgList.append(Edge(1, GpTest.vtxList[7], GpTest.vtxList[6]))
        
        
        
        #instantiate the adjacency matrix
        CommonKnowledge.adjMtxGraph = MtxGraph(len(GpTest.vtxList))
        
        #insert vertices in the adjacency matrix
        for vtx in GpTest.vtxList:
            CommonKnowledge.adjMtxGraph.insert_vtx(vtx)
        
        #insert edges in the adjacency matrix
        for edg in GpTest.edgList:
            CommonKnowledge.adjMtxGraph.insert_edg_EDGE(edg)
        
        #debug
        #display the adjacency matrix for check
        if(GpTest.DEBUG):
            for elmt in CommonKnowledge.adjMtxGraph.get_adjMtx():
                print("{}".format(elmt))
        
        #Set the initial vertex of each ants
        #&& initialize common Knowledge
        CommonKnowledge.comnKldg_init(GpTest.vtxList[warehouse_p])
        