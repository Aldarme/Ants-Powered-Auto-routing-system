'''
Created on 3 juin 2021

@author: promet
'''

import csv
from Utilities.OptimData import OptimData


class CSVFile:
    
    @staticmethod
    def addLine(fileName_p, antID_p, distance_p, energy_p, SOH_marker_p, time_p, volume_p):
        '''
        add line in csv file, compose of above parameters
        all parameters are string
        '''
        root = "/media/Stock/Workspaces/Py_WS/Ants Powered Auto-routing system/src/Logs/"
        
        fileName = str(fileName_p)
        
        with open(root+fileName, "a", newline="" ) as csvFile:
        
            file = csv.writer(csvFile)
            
            file.writerow( [ antID_p, distance_p, energy_p, SOH_marker_p, time_p, volume_p ] )
            
    @staticmethod
    def readFile(fileName_p):
        '''
        read csv log file
        return a list of ant containing optimization data
        '''
        
        dataList = []
        
        root = "/media/Stock/Workspaces/Py_WS/Ants Powered Auto-routing system/src/Logs/"
        fileName = fileName_p
        
        toRead = open( root+fileName, "r")
        
        file = csv.reader(toRead)
        
        for row in file:
            dataList.append(OptimData(int(row[0]),
                                     float(row[1]),
                                     float(row[2]),
                                     float(row[3]),
                                     float(row[4]),
                                     float(row[5])
                                     )
            )
        
        #for elm in dataList:
        #    print(elm.antID)
        #    print(elm.distance)
        #    print(elm.energy)
        #    print(elm.SOH_marker)
        #    print(elm.time)
        #    print(elm.volume)
    
    
        return dataList
    
    
    
    
    
    
    
    