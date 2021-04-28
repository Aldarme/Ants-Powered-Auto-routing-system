'''
Created on 26 avr. 2021

@author: promet
'''
from Graph.Vertex import Vertex
from Simulator.DEBUG import DEBUG_MODE
from copy import deepcopy

class Dijkstra:
    
    @staticmethod
    def run(MtxGraph_p=None, initVtx_p=None):
        
        '''
        Initialization
        '''        
        #get the list of all vertices in the graph
        vtxList = MtxGraph_p.get_Vertices()
        
        #set initVtx label to Zero
        initVtx_p.get_label().set_labelPerf(0.0)
        
        '''
        Processing
        '''
        #search the vtx with min label value
        while len(vtxList) > 0:
            
            #find the vertex with the smallest label value
            vtxWk = Dijkstra.minVtx_find(vtxList)
            
            #add current vertex to his vtx tabu list
            #vtxWk.get_label().set_vtxList(vtxWk)
                  
            print("vtx: {}, labelPerf: {}, nrj: {}, dist: {}, time: {}".format( vtxWk.get_ID(),
                                                                                vtxWk.get_label().get_labelPerf(),
                                                                                vtxWk.get_label().get_nrj(),
                                                                                vtxWk.get_label().get_dist(),
                                                                                vtxWk.get_label().get_time()
                                                                                ))
                
            
            #remove the vtx from "vtxList"
            vtxList.remove(vtxWk)
            
            #get neighbors of the current vertex
            nbList = MtxGraph_p.get_Neighboor_VTX(vtxWk)
            
            #update the label value of each vtx neighbor
            Dijkstra.vtxLabel_update(nbList)
            
            del nbList[:]
        
        
    @staticmethod
    def minVtx_find(vtxList_p):
        """
        find vtx with the smallest label value
        """
        minLabel = float("inf")
        minVtx = Vertex()
        
        for elm in vtxList_p:
            if elm.get_label().get_labelPerf() < minLabel:
                minLabel = elm.get_label().get_labelPerf()
                minVtx = elm
        
        return minVtx
    
    @staticmethod
    def vtxLabel_update(edgList_p=None):
        """
        For each vtx neighbors, update the label value
        """
        for elm in edgList_p:
                
            #display for debug
            #print(elm.toString(False, True))
            
            #calculate vertex label Perf
            localLabel = Dijkstra.labelCalc(elm)
            
            if elm.get_vtx_end().get_label().get_labelPerf() > localLabel.get("labelPerf") :
                elm.get_vtx_end().set_label(localLabel)
                elm.get_vtx_end().get_label().set_prevVtx_String(elm.get_vtx_begin().get_ID())
                #print(elm.get_vtx_end().get_label().get_prevVtx_String())
                    
        
    
    @staticmethod
    def labelCalc(edge_p):
        """
        calculate the label performance value of given edge
        """
        data = {}
        data["nrj"] = edge_p.get_nrj_cost() + edge_p.get_vtx_begin().get_label().get_nrj()
        data["dist"] = edge_p.get_length()  + edge_p.get_vtx_begin().get_label().get_dist()
        data["time"] = edge_p.get_time()    + edge_p.get_vtx_begin().get_label().get_time()
        data["labelPerf"] = (edge_p.get_nrj_cost() * edge_p.get_length() * edge_p.get_time()) + ( edge_p.get_vtx_begin().get_label().get_labelPerf() )
        
        return (data) 
                    
                    
                    
                    
                    
        
        