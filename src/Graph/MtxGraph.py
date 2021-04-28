'''
Created on 27 avr. 2020

@author: promet
'''

from Graph.Edge import Edge
from Graph.Numbering import Numbering


class MtxGraph:

    def __init__(self, size_p):
        self.__numbering    = Numbering()
        self.__adjMtx       = [[None for x in range(size_p)] for y in range(size_p)]
    
    def size(self):
        """
        Return the number of elements into arrayVtx
        """
        return len(self.__adjMtx)
    
    def insert_vtx(self, vtx_p):
        """
        Insert a Vertex into the adjacency matrix to assign to it an index
        """
        if self.__numbering.add_element(vtx_p):
            return True
        else:
            return False
    
    def get_vtxIdx(self, vtx_p):
        """
        Return the index of the current vertex, into the adjacency matrix
        """
        return self.__numbering.get_Idx(vtx_p)
    
    def get_vtx(self, vtx_ID_p):
        """
        return vtx thank to the given ID
        """
        return self.__numbering.get_vtxFromID(vtx_ID_p)
    
    def insert_edg_VERTICES(self, vtx_begin_p, vtx_end_p, length_p):
        """
        Insert an edge into the adjacency matrix, thank to its begin & end vertices
        """
        self.insert_vtx(vtx_begin_p)
        self.insert_vtx(vtx_end_p)
        self.__adjMtx[self.get_vtxIdx(vtx_begin_p)][self.get_vtxIdx(vtx_end_p)] = Edge(length_p, vtx_begin_p, vtx_end_p)
        

    def insert_edg_EDGE(self, edg_p):
        """
        Insert the current edge into the adjacency matrix,
        """
        self.insert_vtx(edg_p.get_vtx_begin())
        self.insert_vtx(edg_p.get_vtx_end())
        self.__adjMtx[self.get_vtxIdx(edg_p.get_vtx_begin())][self.get_vtxIdx(edg_p.get_vtx_end())] = edg_p
   
    
    def exist_edg(self, vtx_begin_p, vtx_end_p):
        """
        Test if there is an edge between two vertices
        """
        edg_tmp = self.__adjMtx[self.get_vtxIdx(vtx_begin_p)][self.get_vtxIdx(vtx_end_p)]   
        if edg_tmp != None:
            if edg_tmp.get_vtx_begin() == vtx_begin_p:
                if edg_tmp.get_vtx_end()== vtx_end_p:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def occur_edg(self, edg_p):
        """
        Verify the existence of a given edge
        """
        edg_tmp = self.__adjMtx[self.get_vtxIdx(edg_p.get_vtx_begin())][self.get_vtxIdx(edg_p.get_vtx_end())]   
        if edg_tmp != None:
            if edg_tmp.get_vtx_begin() == edg_p.get_vtx_begin():
                if edg_tmp.get_vtx_end()== edg_p.get_vtx_end():
                    if edg_tmp.get_length() == edg_p.get_length():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def get_edg(self, vtx_begin_p, vtx_end_p):
        """
        Return the edge corresponding to the given vertices, of the edge exist
        """
        if self.exist_edg(vtx_begin_p, vtx_end_p) != False:
            return self.__adjMtx[self.get_vtxIdx(vtx_begin_p)][self.get_vtxIdx(vtx_end_p)]
        else:
            return None
    
    def get_edglength(self, vtx_begin_p, vtx_end_p):
        """
        Return the length of the given Edge
        """
        return self.__adjMtx[self.get_vtxIdx(vtx_begin_p)][self.get_vtxIdx(vtx_end_p)].get_length()
    
    def get_edgNrjCost(self, vtx_begin_p, vtx_end_p):
        """
        Return the Nrj Cost of the given Edge
        """
        return self.__adjMtx[self.get_vtxIdx(vtx_begin_p)][self.get_vtxIdx(vtx_end_p)].get_nrj_cost()
    
    def modify_length(self, edg_p, length_p):
        """
        Modify the length of the given edge
        """
        self.__adjMtx[self.get_vtxIdx(edg_p.get_vtx_begin())][self.get_vtxIdx(edg_p.get_vtx_end())].set_length(length_p)
    
    
    def delete_edg_EDGE(self, edge_p):
        """
        Delete the given edge
        The case of the edge appear as "None"
        """
        self.__adjMtx[self.get_vtxIdx(edge_p.get_vtx_begin())][self.get_vtxIdx(edge_p.get_vtx_end())] = None
        
    def delete_edg_VERTICES(self, vtx_begin_p, vtx_end_p):
        """
        Delete the edge beginning at "vtx_begin_p" & ending at "vtx_end_p".
        The case of the edge appear as "None"
        """
        self.__adjMtx[self.get_vtxIdx(vtx_begin_p)][self.get_vtxIdx(vtx_end_p)] = None
    
    def get_Neighboor_EDG(self, edge_p):
        """
        Return a list of all the neighbors of the beginning Vertex of the given edge
        """
        neighboors = []
        for elmt in self.__adjMtx[self.get_vtxIdx(edge_p.get_vtx_begin())]:
            if elmt != None:
                if self.exist_edg(edge_p.get_vtx_begin(), elmt.get_vtx_end()):
                    neighboors.append(elmt)
                else:
                    print("echec")
        return neighboors
    
    def get_Neighboor_VTX(self, vtx_p):
        """
        Return a list of all the neighbors of the given Vertex
        """
        neighboors = []
        for elmt in self.__adjMtx[self.get_vtxIdx(vtx_p)]:
            if elmt != None:
                if self.exist_edg(vtx_p, elmt.get_vtx_end()):
                    neighboors.append(elmt)
                else:
                    print("echec, no neighboor")
        return neighboors
    
    def get_nbrOfNeigb(self, vtx_p):
        """
        Return the number of neighbors for the given vertex
        """
        nbrOfNeigb = 0
        for elmt in self.__adjMtx[self.get_vtxIdx(vtx_p)]:
            if elmt != None:
                if self.exist_edg(vtx_p, elmt.get_vtx_end()):
                    nbrOfNeigb += 1    
                else:
                    print("echec")
        return nbrOfNeigb 
    
    def contain_vtx(self, ID_p):
        """
        Test the existence of the given vertex in the adjacency matrix
        """
        if Numbering.contain(self, ID_p):
            return Numbering.get_vtxFromID(self, ID_p)
        else:
            print("error: No vertex ID: {} in the adjacency matrix".format(ID_p))  
    
    def get_Vertices(self):
        """
        Return a list of all Vertices in the adjacency  matrix
        """ 
        return self.__numbering.get_vtxArray()
    
    def get_nbrOfVertices(self):
        """
        Return the numbre of vertices in the adjacency  matrix
        """ 
        return len(self.__numbering.get_vtxArray())
    
    def get_adjMtx(self):
        """
        Return the adjacency matrix
        """
        return self.__adjMtx
    
    def display_adjMtx(self, type_p="object"):
        """
        Display the adjacency matrix according to String parameter
            "object": display edges objects
            "ID": display attributs of edges
        """
        if type_p == "object":
            
            for x in range (0, self.size()):
                for y in range(0, self.size()):
                    if(self.__adjMtx[x][y] != None):
                        print("x: {}, y: {}, {}".format(x,y, self.__adjMtx[x][y]))
        
        elif type_p == "ID":
            
            for x in range (0, self.size()):
                for y in range(0, self.size()):
                    if(self.__adjMtx[x][y] != None):
                        print("x: {}, y: {}, Begin: {}, End: {}, length: {}".format(x,y, self.__adjMtx[x][y].get_vtx_begin().get_ID(), self.__adjMtx[x][y].get_vtx_end().get_ID(), self.__adjMtx[x][y].get_length() ))