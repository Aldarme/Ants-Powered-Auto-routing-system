'''
Created on 4 mai 2020

@author: promet
'''
from Algorithms.VRP.ACO.Ant import Ant, State
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge
from pathlib import Path
from Simulator.DEBUG import DEBUG_MODE
from _operator import itemgetter
from Utilities.CSVFile import CSVFile
import datetime
from Utilities.OptimData import OptimData


class AntCo:
    
    def __init__(self, criterionNbr_p):
        self.antArray = []
        self.create_ants(criterionNbr_p)
        
    
    def create_ants(self, antFactor_p):
        """
        Create an list containing all ants of the colony,
        the ant number is equals to the vertices number multiply by the number of criterion to optimize
        """
        for i in range(0, CommonKnowledge.adjMtxMidGraph.size()*antFactor_p):
            self.antArray.append(Ant(i))
    
    def search(self):
        """
        Execute the research process of all ants, one by one
        """
        for ant in self.antArray:
            if DEBUG_MODE:
                print("ant ID:{}".format(ant.ID))
            
            #run ant research
            ant.run()
            
    def SOHmarkers_calc(self):
        '''
        Calculate State of Health (SOH) marker of each turn
        '''
        totalEnergy = 0.0
        checkSum = 0.0
        
        for ant in self.antArray:
            totalEnergy += (CommonKnowledge.initSOE - ant.SOE)
            
        for ant in self.antArray:
            ant.SOHmarker = (CommonKnowledge.initSOE - ant.SOE) * 100 / totalEnergy
            checkSum += ant.SOHmarker
    
    def getBack(self):
        """
        Update the pheromone strength of all edges in the graph based on objective function
        An ant have to be in "Returning" state, to be used to update pheromone strength
        """
        
        #automatic decrease of all pheromones into the graph
        CommonKnowledge.pheromone_lowering()
        
        #calculate pheromone update of each available ant
        for ant in self.antArray:
            if ant.antState == State.RETURNING:
                for edg in ant.edg_tabuList:
                    #find vertices thank to ID
                    inVtx = CommonKnowledge.adjMtxMidGraph.get_vtx(edg.get_vtx_begin().get_ID())
                    outVtx = CommonKnowledge.adjMtxMidGraph.get_vtx(edg.get_vtx_end().get_ID())
                    
                    #update pheromone
                    CommonKnowledge.set_pheromones(CommonKnowledge.adjMtxMidGraph.get_vtxIdx(inVtx),
                                                   CommonKnowledge.adjMtxMidGraph.get_vtxIdx(outVtx),
                                                   CommonKnowledge.pheroUpdt_objFct_VRP_SOE(edg, (CommonKnowledge.initSOE - ant.SOE), ant.distTravelled, ant.timeTravalled, ant.remainVolume)
                                                   )
    
    def turnCounter(self):
        '''
        Determine the number of turn my by each ant
        '''
        for ant in self.antArray:
            for vtx in ant.vtx_tabuList:
                if vtx.get_ID() == ant.get_warehouse_vtx().get_ID():
                    ant.turnCnt += 1
            #we count the number of return to the deposit to have the number of turn,
            #but there is one deposit at the beginning and at the end to delete
            ant.turnCnt = ant.turnCnt - 1
            
        #for ant in self.antArray:
        #    print(ant.turnCnt)

    def ScoringDistance(self):
        """
        Determine and save the best traveled path (min distance) made by an ant
        """
        for ant in self.antArray:
            if ant.distTravelled < CommonKnowledge.optimalPath_length:
                CommonKnowledge.optimalPath_length = ant.distTravelled  #store the length of the best path
                CommonKnowledge.optimalPath_edg = ant.edg_tabuList      #store the edge making up the best path
        
        CommonKnowledge.get_vtxOptimalPath()
        
        print("Optimal path: {}".format(CommonKnowledge.optimalPath_VTX_toString()))
        print("Optimal length: {}".format(CommonKnowledge.optimalPath_length))
    
    def ScoringMultiObj(self, consoleLog=False, fileLog=False):
        """
        Create a data set containing all ant turn sort by performance index
        Log the data set on consol and on file 
        """
        
        dataSet = []    #dataSet of all sorted solution provided
        
        #normalize all constrains to fit [0;100]% TODO
        for ant in self.antArray:
            if(ant.antState != State.KILLED):
                ant.normNRJ     = ant.SOE * 100 / CommonKnowledge.initSOE
                ant.normDst     = ant.distTravelled * 100 / 100 #after based on the max dist travelled on one of the ants
                ant.normTime    = ant.timeTravalled * 100 / 100 #after based on the max dist travelled on one of the ants
                ant.perfIdx     = ant.normNRJ * ant.normDst * ant.normTime
                
                #log current data path
                tmpDict = {}
                tmpDict["IdxPerf"]  = ant.perfIdx        
                tmpDict["NRJ_Wh"]   = ant.SOE   
                tmpDict["Distance_km"]  = ant.distTravelled
                tmpDict["Time_min"]     = ant.timeTravalled
                tmpDict["Path"]     = ant.get_tabuList_asString()
                
                #feed the dataSet
                dataSet.append(tmpDict)
                
        #sort the dataSet by "IdxPerf"
        dataSet = sorted(dataSet, key=itemgetter("IdxPerf"))
        
        #print and log data set
        self.dataSet_log(consoleLog, fileLog, dataSet)
        

    
    def localSearch(self):
        """
        Apply a local search, after an ant finished a turn
        """
        pass
    
    def antsDisplay(self):
        """
        Display the vertices list of each ant of the colony
        """
        for ant in self.antArray:
            print("ant: {}".format(ant.get_antVertices_toString()))
            
    def antRound_log(self, consoleLog=False, fileLog=False, iterationNbr_p=0):
        
        print('iteration: {}'.format(iterationNbr_p+1))
        i = 0
        for ant in self.antArray:
            i += 1
            
            if consoleLog == True:
                if(ant.antState != State.KILLED):
                    print("ant {}".format(i))
                    print("ant's round vertices:{}".format(ant.visitedVtx_toString()))
                    print("ant's round distance: {}".format(ant.distTravelled))
                    print("ant's round energy  : {}".format(CommonKnowledge.initSOE - ant.SOE))
                    print("ant's round SOH marker : {}".format(ant.SOHmarker))
                    print("ant's round time: {}".format(ant.timeTravalled))
                    print("ant's remaining volume: {}".format(ant.remainVolume))
                    print("\r\n")
                
            if fileLog == True:
                
                #build the relative path leading to "roundLog.txt" file
                path = Path(__file__).parent
                path = "{}{}".format(path.parents[2], "/Logs/")
                
                fo = open(path +"roundLog.txt", "a")
                
                fo.write("Algorithm iteration: {}".format(iterationNbr_p+1) + "\r\n")
                
                if(ant.antState != State.KILLED):
                    fo.write("ant {}".format(i) + "\r\n")
                    fo.write("ant's round vertices:{},{} {}".format(CommonKnowledge.vtx_init.get_ID() ,ant.visitedVtx_toString(), CommonKnowledge.vtx_init.get_ID()) + "\r\n")
                    fo.write("ant's round distance: {}".format(ant.distTravelled) + "\r\n")
                    fo.write("ant's round energy  : {}".format(CommonKnowledge.initSOE - ant.SOE) + "\r\n")
                    fo.write("ant's round SOH marker : {}".format(ant.SOHmarker) + "\r\n")
                    fo.write("ant's round time    : {}".format(ant.timeTravalled) + "\r\n" )
                    fo.write("ant's remaining Volume  : {}".format(ant.remainVolume) + "\r\n" )
                    fo.write("\r\n")
                    
                # Close opened file
                fo.close()
                
    def dataSet_log(self, consoleLog=False, fileLog=False, dataSet_p=None):
        """
        Log the data set on console and on file
        """
        if consoleLog == True:
            
            print("All ant delivery path: \r\n")
            
            for elm in dataSet_p:
                print("#####################################")
                print("Perf. indx: {}".format(elm["IdxPerf"]))
                print("Energy consumed: {}".format(elm["NRJ_Wh"]))
                print("SOH marker: {}".format(elm["TODO"]))
                print("Distance travelled: {}".format(elm["Distance_km"]))
                print("Time travalled: {}".format(elm["Time_min"]))
                print("delivery Path: {}".format(elm["Path"]))
                print("#####################################")
                print("\r\n")
                
            print("#####################################")
            print("The best path is: \r\n")
            print("Perf. indx: {}".format(dataSet_p[0]["IdxPerf"]))
            print("Energy consumed: {}".format(dataSet_p[0]["NRJ_Wh"]))
            print("SOH marker: {}".format(elm["TODO"]))
            print("Distance travelled: {}".format(dataSet_p[0]["Distance_km"]))
            print("Time travalled: {}".format(dataSet_p[0]["Time_min"]))
            print("delivery Path: {}".format(dataSet_p[0]["Path"]))
            print("#####################################")
            print("\r\n")
            
        if fileLog == True:
            
            #build the relative path leading to "roundLog.txt" file
            path = Path(__file__).parent
            path = "{}{}".format(path.parents[2], "/Logs/")
            
            fo = open(path +"dataSet.txt", "a")
            
            fo.write("All ant delivery path:" + "\r\n")
            
            for elm in dataSet_p:
                fo.write("#####################################"            + "\r\n")
                fo.write("Perf. indx: {}".format(elm["IdxPerf"])            + "\r\n")
                fo.write("Energy consumed: {}".format(elm["NRJ_Wh"])        + "\r\n")
                fo.write("SOH marker: {}".format(elm["TODO"])               + "\r\n")
                fo.write("Distance travelled: {}".format(elm["Distance_km"])+ "\r\n")
                fo.write("Time travalled: {}".format(elm["Time_min"])       + "\r\n")
                fo.write("delivery Path: {}".format(elm["Path"])            + "\r\n")
                fo.write("#####################################"            + "\r\n")
                fo.write("\r\n"                                             + "\r\n")
                
            fo.write("#####################################"                + "\r\n")
            fo.write("The best path is:"                                    + "\r\n")
            fo.write("Perf. indx: {}".format(dataSet_p[0]["IdxPerf"])       + "\r\n")
            fo.write("Energy consumed: {}".format(dataSet_p[0]["NRJ_Wh"])   + "\r\n")
            fo.write("SOH marker: {}".format(elm["TODO"])                   + "\r\n")
            fo.write("Distance travelled: {}".format(dataSet_p[0]["Distance_km"]) + "\r\n")
            fo.write("Time travalled: {}".format(dataSet_p[0]["Time_min"])  + "\r\n")
            fo.write("delivery Path: {}".format(dataSet_p[0]["Path"])       + "\r\n")
            fo.write("#####################################"                + "\r\n")
            fo.write("\r\n"                                                 + "\r\n")

            # Close opened file
            fo.close()
        
    def csv_log(self, active_p = True):
        '''
        Log all solutions, generated by the ant colony
        '''
        
        if active_p == True:
        
            #get current date and hour for file name
            date = datetime.datetime.now()
            
            for ant in self.antArray:
                if(ant.antState != State.KILLED):
                    CSVFile.addLine((str(date)+".csv"),
                                    str(ant.ID),
                                    str(ant.distTravelled),
                                    str(CommonKnowledge.initSOE - ant.SOE),
                                    str(ant.SOHmarker),
                                    str(ant.timeTravalled),
                                    str(ant.remainVolume),
                                    str(ant.turnCnt),
                                    ant.visitedVtx_toString()
                                    )
            return (str(date)+".csv")
                
    
    
    
    
    
    
        