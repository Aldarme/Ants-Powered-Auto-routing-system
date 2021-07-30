'''
Created on 3 juin 2021

@author: promet
'''

import csv
from Utilities.OptimData import OptimData


class CSVFile:
    
    @staticmethod
    def addLine(fileName_p, antID_p, distance_p, energy_p, SOH_marker_p, time_p, volume_p, turnCnt_p, deliveryPath_p):
        '''
        add line in csv file, compose of above parameters
        all parameters are string
        '''
        root = "/media/Stock/Workspaces/Py_WS/Ants Powered Auto-routing system/src/Logs/"
        
        fileName = str(fileName_p)
        
        with open(root+fileName, "a", newline="" ) as csvFile:
        
            file = csv.writer(csvFile)
            
            file.writerow( [ antID_p, distance_p, energy_p, SOH_marker_p, time_p, volume_p, turnCnt_p, deliveryPath_p ] )
            
    @staticmethod
    def feedColm(fileName_p, data_p):
        '''
        fill column to with data 
        '''
        root = "/media/Stock/Workspaces/Py_WS/Ants Powered Auto-routing system/src/Logs/"
        fileName = str(fileName_p)

        with open(root+fileName+"_SOH", "a", newline="" ) as csvFile:  # output csv file
            outFile = csv.writer(csvFile)
            with open(root+fileName,'r') as csvfile: # input csv file
                reader = csv.reader(csvfile, delimiter=',')
                i = 0
                for row in reader:  
                    row[3] = data_p[i]
                    outFile.writerow(row)
                    i += 1
                    
        
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
        
        #create a list of object containing ant's data
        for row in file:
            dataList.append(OptimData(int(row[0]),
                                     float(row[1]),
                                     float(row[2]),
                                     float(row[3]),
                                     float(row[4]),
                                     float(row[5]),
                                     int(row[6]),
                                     str(row[7])
                                     )
            )
        
        #for elm in dataList:
        #    print(elm.antID)
        #    print(elm.distance)
        #    print(elm.energy)
        #    print(elm.SOH_marker)
        #    print(elm.time)
        #    print(elm.volume)
    
    
        return dataList #return the object list
    
    
    
    
    
    
    
    