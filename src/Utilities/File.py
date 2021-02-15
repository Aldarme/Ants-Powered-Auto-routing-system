'''
Created on 12 févr. 2021

@author: promet
'''

class File:
    
    @staticmethod
    def fileWrite(fileName_p, dataStr_p, path_p):
        
        path = path_p
        fo = open(path + fileName_p, "a")
        
        fo.write(dataStr_p + "\r\n")
            
        # Close opened file
        fo.close()