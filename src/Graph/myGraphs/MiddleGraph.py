'''
Created on 26 avr. 2021

@author: promet
'''
from Simulator.DEBUG import DEBUG_MODE
from Graph.Edge import Edge
from Graph.Vertex import Vertex
from Utilities.Dijkstra import Dijkstra
from Utilities.PackgListGen import PackgListGen
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge
from locale import currency
from Graph.MtxGraph import MtxGraph

class MiddleGraph:
    
    vtxList = []
    edgList = []
    
    @staticmethod
    def create(deliveryList_string_p = None):
        
        #create vertices list
        for elm in deliveryList_string_p:
            
            #get the wanted vertex
            tmpVtx = CommonKnowledge.get_adjMtxGraph().get_vtx(elm)
            
            #set package list into it
            tmpVtx.set_packageList(PackgListGen.run())
            
            #add the vertex in the MiddleGraph vertices list
            MiddleGraph.vtxList.append(tmpVtx)
        
        #get vtx corresponding to "warehouse_vtx", which is the deposit point, in commonknowledge
        myVtx = CommonKnowledge.get_adjMtxGraph().get_vtx(CommonKnowledge.warehouse_vertex)
        
        #add the deposit vertex to 'vtxList'
        MiddleGraph.vtxList.append(myVtx)
        
        for item in MiddleGraph.vtxList:
            
            #reset the label of each vertices of Belfort graph
            for vtxElm in CommonKnowledge.get_adjMtxGraph().get_Vertices():
                vtxElm.labelFlusher()
            
            #from the current vertex, find the shortest path to all other
            Dijkstra.run(CommonKnowledge.adjMtxGraph, item)
            
            #create tmp list of linked points to create part of MiddleGraph
            tmpList = MiddleGraph.vtxList.copy()
            tmpList.remove(item)
            
            for tmpVtx in tmpList:
                '''
                build path from "tmpVtx" to starting point of current Dijkstra run: 'elm'
                stock the path as list of vertices: 'vtxPath'
                '''
                currentVtx = tmpVtx
                prvVtx = "empty"
                vtxPath = []    #list of vtx constituting the path
                while prvVtx != item.get_ID():
                    prvVtx = currentVtx.get_label().get_prevVtx_String()
                    vtxPath.append(prvVtx)
                    currentVtx = CommonKnowledge.get_adjMtxGraph().get_vtx(prvVtx)
                    
                dict = {}
                dict["NRJ_Wh"]      = tmpVtx.get_label().get_nrj()
                dict["Distance_km"] = tmpVtx.get_label().get_dist()
                dict["time_min"]    = tmpVtx.get_label().get_time()
                                  
                #create and stock current edge of MiddleGraph
                MiddleGraph.edgList.append(Edge(MiddleGraph.getVtx(item), MiddleGraph.getVtx(tmpVtx), dict, vtxPath.copy()))
            
            #for edg in MiddleGraph.edgList:
            #    print("nrjcost: {}".format(edg.get_nrj_cost()))
            #    print("dist: {}".format(edg.get_length()))
            #    print("time: {}".format(edg.get_time()))
            #    print("vtx: {}".format(edg.get_path_asString()))
            #    print("##############################")
            
        #instantiate adjacency matrix of MiddleGraph
        CommonKnowledge.adjMtxMidGraph = MtxGraph(len(MiddleGraph.vtxList))
        
        #insert verticesList in adjacency matrix of MiddleGraph
        for unitVtx in MiddleGraph.vtxList:
            CommonKnowledge.adjMtxMidGraph.insert_vtx(unitVtx)
        
        #insert edgList in adjacency matrix of MiddleGraph
        for unitEdg in MiddleGraph.edgList:
            CommonKnowledge.adjMtxMidGraph.insert_edg_EDGE(unitEdg)
        
        #init adapted commonKnowledge
        CommonKnowledge.comnKldg_init()
    
    
    @staticmethod
    def create_old(deliveryList_string_p = None, InitID_p=None):
        
        #create vertices list
        for elm in deliveryList_string_p:
            
            #get the wanted vertex
            tmpVtx = CommonKnowledge.get_adjMtxGraph().get_vtx(elm)
            
            #set package list into it
            tmpVtx.set_packageList(PackgListGen.run())
            
            #add the vertex in the MiddleGraph vertices list
            MiddleGraph.vtxList.append(tmpVtx)
        
        #get vtx corresponding to "InitID_p", which is the deposit point
        myVtx = CommonKnowledge.get_adjMtxGraph().get_vtx(InitID_p)
        
        #add the deposit vertex to 'vtxList'
        MiddleGraph.vtxList.append(myVtx)
        
        for item in MiddleGraph.vtxList:
            
            #reset the label of each vertices of Belfort graph
            for vtxElm in CommonKnowledge.get_adjMtxGraph().get_Vertices():
                vtxElm.labelFlusher()
            
            #from the current vertex, find the shortest path to all other
            Dijkstra.run(CommonKnowledge.adjMtxGraph, item)
            
            #create tmp list of linked points to create part of MiddleGraph
            tmpList = MiddleGraph.vtxList.copy()
            tmpList.remove(item)
            
            for tmpVtx in tmpList:
                '''
                build path from "tmpVtx" to starting point of current Dijkstra run: 'elm'
                stock the path as list of vertices: 'vtxPath'
                '''
                currentVtx = tmpVtx
                prvVtx = "empty"
                vtxPath = []    #list of vtx constituting the path
                while prvVtx != item.get_ID():
                    prvVtx = currentVtx.get_label().get_prevVtx_String()
                    vtxPath.append(prvVtx)
                    currentVtx = CommonKnowledge.get_adjMtxGraph().get_vtx(prvVtx)
                    
                dict = {}
                dict["NRJ_Wh"]      = tmpVtx.get_label().get_nrj()
                dict["Distance_km"] = tmpVtx.get_label().get_dist()
                dict["time_min"]    = tmpVtx.get_label().get_time()
                                  
                #create and stock current edge of MiddleGraph
                MiddleGraph.edgList.append(Edge(MiddleGraph.getVtx(item), MiddleGraph.getVtx(tmpVtx), dict, vtxPath.copy()))
            
            #for edg in MiddleGraph.edgList:
            #    print("nrjcost: {}".format(edg.get_nrj_cost()))
            #    print("dist: {}".format(edg.get_length()))
            #    print("time: {}".format(edg.get_time()))
            #    print("vtx: {}".format(edg.get_path_asString()))
            #    print("##############################")
            
        #instantiate adjacency matrix of MiddleGraph
        CommonKnowledge.adjMtxMidGraph = MtxGraph(len(MiddleGraph.vtxList))
        
        #insert verticesList in adjacency matrix of MiddleGraph
        for unitVtx in MiddleGraph.vtxList:
            CommonKnowledge.adjMtxMidGraph.insert_vtx(unitVtx)
        
        #insert edgList in adjacency matrix of MiddleGraph
        for unitEdg in MiddleGraph.edgList:
            CommonKnowledge.adjMtxMidGraph.insert_edg_EDGE(unitEdg)
        
        #init adapted commonKnowledge
        CommonKnowledge.comnKldg_init(MiddleGraph.getVtx(myVtx))
        
        
    @staticmethod
    def getVtx(vtx_p):
        for vtx in MiddleGraph.vtxList:
            if vtx.get_ID() == vtx_p.get_ID():
                return vtx
        assert False, "element: **{}**,do not exist in the list".format(vtx_p)
        
        
        