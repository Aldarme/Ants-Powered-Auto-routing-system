'''
Created on 27 avr. 2020

@author: promet
'''

class Numbering:
    
    def __init__(self):
        self.__cnt          = -1
        self.__dicVtxIdx    = {}    #[Vertex, Index] dictionary
        self.__arrayVtx     = []     #List of vertices
    
    def size(self):
        """
        Return the number of elements into arrayVtx
        """
        return len(self.__arrayVtx)
    
    def add_element(self, vtx_p):
        """
        Add an new element to generate a [Vertex, Index] dictionary
        """
        #if not self.__dicVtxIdx.has_key(vtx_p): #haskey was reprequated, need to find new appropriate one
        if not vtx_p in self.__dicVtxIdx:
            self.__cnt += 1
            self.__dicVtxIdx[vtx_p] = self.__cnt
            self.__arrayVtx.append(vtx_p)
            return True
        else:
            return False
    
    def get_Idx(self, vtx_p):
        """
        Return the index of the given Vertex
        """
        return self.__dicVtxIdx[vtx_p]
    
    def get_vtx(self, Key_p):
        """
        Return a vertex according to its index/key
        """
        return self.__dicVtxIdx.get(Key_p)
    
    def get_vtxAt(self, idx_p):
        """
        Return the Vertex at the given index 
        """
        return self.__arrayVtx[idx_p]
    
    def get_vtxArray(self):
        """
        Return the list of vertices
        """
        return self.__arrayVtx[:]
    
    def contain(self,ID_p):
        """
        Test if the given vertex exist in the numbering class
        """
        for vtx in Numbering.__arrayVtx:
            if vtx.get_ID() == ID_p:
                return True
            else:
                return False
    
    def get_vtxFromID(self, ID_p):
        """
        Return a vertex according to the given ID
        """
        for vtx in self.__arrayVtx:
            if vtx.get_ID() == ID_p:
                return vtx