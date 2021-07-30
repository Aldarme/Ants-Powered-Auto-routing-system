'''
Created on 3 juin 2021

@author: promet
'''

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from Utilities.CSVFile import CSVFile

class ParetoFront:
    
    @staticmethod
    def threeD(genFileName=""):
        
        #read csv file to access data
        #fileName = "2021-06-03 14:47:45.430862.csv"
        #fileName = "Reduce_2021-06-10 16:35:02.621682.csv"
        
        dataList = CSVFile.readFile( genFileName )
        
        xData = []
        yData = []
        zData = []
        
        for elm in dataList:
            xData.append(elm.energy)
            yData.append(elm.turnCnt)
            zData.append(elm.SOH_marker)
        
        fig = pyplot.figure()
        Axes3D = fig.add_subplot(projection='3d')
        
        Axes3D.set_xlabel('Energy consumed')
        Axes3D.set_ylabel('Turn number')
        Axes3D.set_zlabel('SOH marker')
        
        Axes3D.scatter3D(xData, yData, zData, zdir='z', s=21, c=None, depthshade=True)
        pyplot.show()
        
    @staticmethod
    def twoD(genFileName=""):
        
        #read csv file to access data
        #fileName = "2021-06-03 14:47:45.430862.csv"
        #fileName = "2021-06-03 14:39:21.656270.csv"
        
        dataList = CSVFile.readFile( genFileName )
        
        xData = []
        yData = []
        
        for elm in dataList:
            xData.append(elm.energy)
            yData.append(elm.turnCnt)
        
        pyplot.plot(xData, yData, 'ro')
        #pyplot.axis([0, 5, 0, 1000])
        pyplot.xlabel("energy consumed")
        pyplot.ylabel("number of turn")
        pyplot.show()

#################################

ParetoFront.twoD("2021-07-21 00:18:06.995083.csv")