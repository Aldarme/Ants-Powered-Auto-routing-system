'''
Created on 3 juin 2021

@author: promet
'''

from Utilities.CSVFile import CSVFile


class LexicoRule:
    
    @staticmethod
    def run():
        
        sortedList = []     #list of Optimize Data sorted with LexicoRule
        
        #read csv file to access data
        #fileName = "2021-06-03 14:47:45.430862.csv"
        fileName = "2021-06-03 14:39:21.656270.csv"
        
        dataList = CSVFile.readFile( fileName )
        
        #sort the dataList by maximize transported Volume
        sortedList = sorted( dataList, key=lambda OptimData: OptimData.volume, reverse = True)
        
        print("####################################")
        print("max Volume")
        for elm in sortedList:
            print("ID: {}; Volume: {}".format(elm.antID, elm.volume))
        print("")
            
        #sort the dataList by minimize consumed energy
        sortedList = sorted( dataList, key=lambda OptimData: OptimData.energy, reverse = False)
        
        print("####################################")
        print("min energy")
        for elm in sortedList:
            print("ID: {}; energy: {}".format(elm.antID, elm.energy))
        print("")
        
        #sort the dataList by minimize SOH energy
        sortedList = sorted( dataList, key=lambda OptimData: OptimData.SOH_marker, reverse = False)
        
        print("####################################")
        print("min SOH_marker")
        for elm in sortedList:
            print("ID: {}; SOH: {}".format(elm.antID, elm.SOH_marker))
        print("")
        
        #Print final Lexicographic list
        print("####################################")
        print("final Lexicographic list")
        for elm in sortedList:
            print("Vehicle turn ID: {}, distance:{}, energy:{}, SOH_marker:{}, time:{}, volume:{}".
                                                            format(elm.antID,
                                                                   elm.distance,
                                                                   elm.energy,
                                                                   elm.SOH_marker,
                                                                   elm.time,
                                                                   elm.volume
                                                                   )
            )
            CSVFile.addLine("LexicographicList.csv",
                            elm.antID,     
                            elm.distance,  
                            elm.energy,    
                            elm.SOH_marker,
                            elm.time,      
                            elm.volume
                            )     
        print("")
        
        













###### DEBUG
LexicoRule.run() 