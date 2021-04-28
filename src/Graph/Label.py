'''
Created on 28 avr. 2021

@author: promet
'''

class Label:
    
    def __init__( self, nrj_p=0.0, dist_p=0.0, time_p=0.0):
        self.__nrj = nrj_p
        self.__dist = dist_p
        self.__time = time_p
        self.__labelPerf = float("inf")
        self.__prevVtx_Str = "empty"
    
    def setLabel(self, localLabel_p):
        self.__nrj =    localLabel_p.get("nrj")
        self.__dist =   localLabel_p.get("dist")
        self.__time =   localLabel_p.get("time")
        self.__labelPerf = localLabel_p.get("labelPerf")
        
    def get_nrj(self):
        return self.__nrj
    
    def get_dist(self):
        return self.__dist
    
    def get_time(self):
        return self.__time
    
    def get_labelPerf(self):
        return self.__labelPerf
    
    def get_edgList(self):
        return self.__edgList
    
    def get_prevVtx_String(self):
        return self.__prevVtx_Str
    
    def set_labelPerf(self, labelPerf_p):
        self.__labelPerf = labelPerf_p
        
    def set_prevVtx_String(self, str_p):
        self.__prevVtx_Str = str_p
        
    