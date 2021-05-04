'''
Created on 27 avr. 2020

@author: promet
'''

#from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge

class Edge:
    
    """
    Init object parameters value
    By default, nrj_cost is init at 0,25 kwh/km, according to data exploitation
    """
    def __init__(self, vtx_begin_p = None, vtx_end_p = None, dataDict_p = None, path_vertices_p = None ):
        #nrj_Wh_p = None, dist_km_p = None, time_min_p = None
        assert vtx_begin_p  != None, "Empty vtx_begin_p, 'TRUBBLE' empty export from vtxList"
        assert vtx_end_p    != None, "Empty vtx_end_p, 'TRUBBLE' empty export from vtxList"
        assert dataDict_p   != None, "Empty dataDict_p, 'TRUBBLE' empty export from database"
        #assert nrj_Wh_p     == None, "Empty nrj_Wh_p, 'TRUBBLE' empty export from database"
        #assert dist_km_p    == None, "Empty dist_km_p, 'TRUBBLE' empty export from database"
        #assert time_min_p   == None, "Empty time_min_p, 'TRUBBLE' empty export from database"
        
        self.__vtx_begin    = vtx_begin_p
        self.__vtx_end      = vtx_end_p        
        self.__nrj_cost     = dataDict_p["NRJ_Wh"]      #Energy unit: kwh/km
        self.__length       = dataDict_p["Distance_km"] #distance unit: km
        self.__time         = dataDict_p["time_min"]    #time unit: minute
        self.path_vertex    = path_vertices_p
    
    def set_length(self, length_p):
        """
        Set the length value
        """
        self.__length = length_p
    
    def set_vtx_begin(self, vtx_p):
        """
        Set the beginning vertex object
        """
        self.__vtx_begin = vtx_p
    
    def set_vtx_end(self, vtx_p):
        """
        Set the ending vertex object
        """
        self.__vtx_end = vtx_p
    
    def get_nrj_cost(self):
        """
        Get the nrj cost of the edge
        """
        return self.__nrj_cost 
        
    def get_length(self):
        """
        Get the length value
        """
        return self.__length
    
    def get_time(self):
        "Get the time value"
        return self.__time
    
    def get_path_asString(self):
        path = []
        for elm in self.path_vertex:
            path.append(elm)
        return path
    
    def get_vtx_begin(self):
        """
        Get the beginning vertex object
        """
        return self.__vtx_begin
    
    def get_vtx_end(self):
        """
        Get the ending vertex object
        """
        return  self.__vtx_end
    
    def toString(self, name_p = True, data_p = False):
        """
        Convert class properties into a String 
        """
        if name_p == True and data_p == False:
            return "This edge begin at: {}, end at: {}".format(self.__vtx_begin.get_ID(), self.__vtx_end.get_ID())
        
        if name_p == False and data_p == True :
            return "This edge begin at: {}, end at: {}, nrj: {}, dist: {}, time: {}".format(self.__vtx_begin.get_ID(), self.__vtx_end.get_ID(), self.__nrj_cost, self.__length, self.__time)
        
        
        