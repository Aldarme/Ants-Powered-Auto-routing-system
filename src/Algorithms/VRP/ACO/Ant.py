'''
Created on 4 mai 2020

@author: promet
'''

from Graph.Vertex import Vertex
from Graph.Edge import Edge
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge
from Simulator.DEBUG import DEBUG_MODE
from Utilities.DelivListGen import DelivListGen
from Graph.MtxGraph import MtxGraph
import copy
import random
import sys



class Ant:
    
    def __init__(self, ID_p):
        self.ID             = ID_p
        self.vtx_current    = Vertex()          #Get warehouse vertex in "adjLocalMtxMidGraph" thanks to "CommonKwonledge.warehouse_vertex"
        self.antState       = State.HANDLE      #Define the state of the ant during the algorithm
        self.vtx_Next       = Vertex()          #Next Vertex in the graph the ant have to join
        self.distTravelled  = 0.0               #Distance travelled by an ant
        self.timeTravalled  = 0.0               #Time travelled by an ant
        self.vtx_toVisit    = []                #Collection of reachable vertices in the graph
        self.vtx_tabuList   = []                #Collection of all visited Vertices, by the ant
        self.edg_tabuList   = []                #Revoir cette element de dorigo prob, si vraiment utile ? Collection of all visited edges by the ant    
        self.neigb_tabuList = []                #Collection of ant tested neighbors
        self.SOE            = CommonKnowledge.initSOE       #Energy capacity of the electric vehicle, [20;80]
        self.SOHmarker      = 0.0                           #State of Health marker of the battery
        self.remainVolume   = CommonKnowledge.packgVolume   #Volume (m3) to transport packages
        self.curbWeight     = CommonKnowledge.curbWeight    #Weight (kg) of the vehicle
        self.normNRJ        = 0.0
        self.normDst        = 0.0
        self.normTime       = 0.0
        self.perfIdx        = 0.0
        self.adjLocalMtxMidGraph = MtxGraph     #Local copy of adjacency matrix of Middle Graph
        self.turnCnt        = 0
        #self.toVisit()                          #Create the list of delivery point, an ant have to visit
    
    def run(self):
        """
        Start the research process for an ant
        As long as function return true, continue to build tour
        """
        self.antState =State.SEARCHING_PATH
        while( self.VRP_tour() ):
            pass
        
        if DEBUG_MODE:
            for elm in self.vtx_tabuList:
                print(elm.get_ID())
            print("#####################")
    
    def VRP_tour(self):
        '''
        Define how an ant build a VRP solution
        The ant will build as many turn as necessary to visit each delivery of the list
        '''
        
        #Get the next vertex to visit
        self.vtx_Next = self.dorigo_prob_VRP(self.vtx_current).get_vtx_end()
        
        if self.vtx_Next.get_ID() == self.get_warehouse_vtx().get_ID():
            sys.exit("next is warehouse !!!")
            
        #Process data from the edge
        self.vtx_tabuList.append(self.vtx_current)
        self.vtx_toVisit.remove(self.vtx_current)
        self.SOE            -= self.adjLocalMtxMidGraph.get_edgNrjCost(self.vtx_current, self.vtx_Next)
        self.distTravelled  += self.adjLocalMtxMidGraph.get_edglength(self.vtx_current, self.vtx_Next)
        self.timeTravalled  += self.adjLocalMtxMidGraph.get_edgTime(self.vtx_current, self.vtx_Next)
        self.remainVolume   -= self.vtx_Next.get_packagesTotalVol()
        self.curbWeight     += self.vtx_Next.get_packagesTotalWgt()
        
        #Unable current delivery point to be reach again
        self.adjLocalMtxMidGraph.kickOut_vtx(self.vtx_current)
        
        
        #Kill current ant if package volume is overloaded
        if self.remainVolume < 0:
            print("Current ant kills, due to capacity volume overload")
            self.antState       = State.KILLED
            return False
        
        
        #Kill current ant if its energy capacity get lower than 20%
        if self.SOE < CommonKnowledge.minSOE:
            print("Current ant kills, due to nrj Capacity Min < 20% of battery capacity")
            self.antState       = State.KILLED
            return False
            
        
        #Return to the deposit if remaining package volume is less than 0.3 cube meter
        if self.remainVolume > 0 and self.remainVolume < 0.3:
            self.vtx_Next = self.get_warehouse_vtx()
            
            try:
                self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost_vtxID(self.vtx_current.get_ID(), self.vtx_Next.get_ID())
            except:
                print("current vtx: " + self.vtx_current.get_ID())
                print("next vtx: " + self.vtx_Next.get_ID())
                print("***********************")
                print("toVisit list")
                for elm in self.vtx_toVisit:
                    print(elm.get_ID())
                print("******")
                print("tabuList list")
                for elm in self.vtx_tabuList:
                    print(elm.get_ID())
                    
                sys.exit("Error current or next & edge")
            
            self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost_vtxID(self.vtx_current.get_ID(), self.vtx_Next.get_ID())
            self.distTravelled  += CommonKnowledge.adjMtxMidGraph.get_edglength_vtxID(self.vtx_current.get_ID(), self.vtx_Next.get_ID())
            self.timeTravalled  += CommonKnowledge.adjMtxMidGraph.get_edgTime_vtxID(self.vtx_current.get_ID(), self.vtx_Next.get_ID())
            self.vtx_current = self.get_warehouse_vtx()
            self.vtx_Next = None
            self.Deposit_reconnect()
            self.vtx_toVisit.append(self.get_warehouse_vtx())
            self.remainVolume   = CommonKnowledge.packgVolume
            return True
        
        #Return to the deposit if remaining energy is between 20 and 23%
        '''
        if self.SOE > (self.SOE * 20 / 100) and self.SOE < (self.SOE * 23 / 100):
            self.vtx_Next = self.get_warehouse_vtx()
            self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost_vtxID(self.vtx_current.get_ID(), self.vtx_Next.get_ID())
            self.distTravelled  += CommonKnowledge.adjMtxMidGraph.get_edglength_vtxID(self.vtx_current.get_ID(), self.vtx_Next.get_ID())
            self.timeTravalled  += CommonKnowledge.adjMtxMidGraph.get_edgTime_vtxID(self.vtx_current.get_ID(), self.vtx_Next.get_ID())
            self.vtx_current = self.get_warehouse_vtx()
            self.vtx_Next = None
            self.Deposit_reconnect()
            self.vtx_toVisit.append(self.get_warehouse_vtx())
            #ne pas laisser le véhicule repartir, il doit être recharger, dans notre strategie, il est maintenant inutilisable
            return True
        '''
        
        #There is no more delivery point to visit, return to the deposit and start next ant
        if len(self.vtx_toVisit) == 1:
            self.antState       = State.RETURNING
            self.vtx_tabuList.append(self.vtx_Next)
            self.vtx_toVisit.remove(self.vtx_Next)
            self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost_vtxID(self.vtx_Next.get_ID(), self.get_warehouse_vtx().get_ID())
            self.distTravelled  += CommonKnowledge.adjMtxMidGraph.get_edglength_vtxID(self.vtx_Next.get_ID(), self.get_warehouse_vtx().get_ID())
            self.timeTravalled  += CommonKnowledge.adjMtxMidGraph.get_edgTime_vtxID(self.vtx_Next.get_ID(), self.get_warehouse_vtx().get_ID())
            self.vtx_Next       = None
            self.vtx_current    = self.get_warehouse_vtx()
            self.vtx_tabuList.append(self.vtx_current)
            
            return False
        
        #Current ant have to find the next vertex to reach
        self.vtx_current = self.vtx_Next   
        self.vtx_Next = None
        return True
        
        
    def resetter(self):
        '''
        Reset an ant as it default state
        '''
        self.vtx_current    = Vertex()
        self.antState       = State.HANDLE      #Define the state of the ant during the algorithm
        self.vtx_Next       = Vertex()          #Next Vertex in the graph the ant have to join
        self.distTravelled  = 0.0               #Distance travelled by an ant
        self.timeTravalled  = 0.0               #Time travelled by an ant
        del self.vtx_toVisit[:]                 #flush the to visit list
        del self.vtx_tabuList[:]                #flush the tabu list
        del self.edg_tabuList[:]                #flush the edge tabu List
        del self.neigb_tabuList[:]              #flush the tested neighbors tabu list
        self.SOE            = CommonKnowledge.initSOE       #Energy capacity of the electric vehicle, [20;80]
        self.SOHmarker      = 0.0                           #State of Health marker of the battery
        self.remainVolume    = CommonKnowledge.packgVolume   #Volume (m3) to transport packages
        self.curbWeight     = CommonKnowledge.curbWeight    #Weight (kg) of the vehicle
        self.normNRJ        = 0.0
        self.normDst        = 0.0
        self.normTime       = 0.0
        self.perfIdx        = 0.0
        self.adjLocalMtxMidGraph = MtxGraph     #Local copy of adjacency matrix of Middle Graph
        self.toVisit()                          #Create the list of delivery point, an ant have to visit
        
    def Deposit_reconnect(self):
        """
        When the ant return to the deposit,
        the deposit needs to be reconnect to all remaining delivery point
        """
                
        for elm in self.vtx_toVisit:
            
            #get the edge between [deposit ; elm] in Commonknowledge.adjMtxMidGraph
            vtxIn = CommonKnowledge.adjMtxMidGraph.get_vtx( CommonKnowledge.warehouse_vertex )
            vtxout = CommonKnowledge.adjMtxMidGraph.get_vtx( elm.get_ID() )
            tmpEdg = CommonKnowledge.adjMtxMidGraph.get_edg(vtxIn, vtxout)
            
            dicTmp = dict()
            dicTmp["NRJ_Wh"]        = tmpEdg.get_nrj_cost()
            dicTmp["Distance_km"]   = tmpEdg.get_length()
            dicTmp["time_min"]      = tmpEdg.get_time()
            
            #insert into local copy of adjMtxMidGraph
            self.adjLocalMtxMidGraph.insert_edg_VERTICES(elm, 
                                                         self.adjLocalMtxMidGraph.get_vtx(CommonKnowledge.warehouse_vertex),
                                                         dicTmp
                                                        )
            
            #get the edge between [elm ; deposit] in Commonknowledge.adjMtxMidGraph
            vtxIn = CommonKnowledge.adjMtxMidGraph.get_vtx( elm.get_ID() )
            vtxout = CommonKnowledge.adjMtxMidGraph.get_vtx( CommonKnowledge.warehouse_vertex )
            tmpEdg = CommonKnowledge.adjMtxMidGraph.get_edg(vtxIn, vtxout)
            
            dicTmp = dict()
            dicTmp["NRJ_Wh"]        = tmpEdg.get_nrj_cost()
            dicTmp["Distance_km"]   = tmpEdg.get_length()
            dicTmp["time_min"]      = tmpEdg.get_time()
            
            #insert into local copy of adjMtxMidGraph
            self.adjLocalMtxMidGraph.insert_edg_VERTICES(self.adjLocalMtxMidGraph.get_vtx(CommonKnowledge.warehouse_vertex),
                                                         elm,
                                                         dicTmp
                                                        )

    def toReach_TSP_CUG(self):
        '''
        Define how an ant build TSP solution in a Complete Undirected Graph
        A solution build one turn, allowing to visit all delivery point of the list
        '''
        #when we are sure that the current ant visited all point, allow he to return at the deposit
        if len(self.vtx_tabuList) < len(DelivListGen.debugList): #len(DelivListGen.buStop)
            #Return the heuristic edge destination determined by the DorigoProb
            self.vtx_Next = self.dorigo_prob(self.vtx_current).get_vtx_end()
        else:
            #if all delivery point has been visited, allow the ant to come back to the delivery point
            self.vtx_toVisit.append(CommonKnowledge.vtx_init)
            self.vtx_Next = CommonKnowledge.vtx_init
        
        #Test if the next vertex can be reach
        if self.vtx_Next in self.vtx_toVisit:
            
            self.vtx_tabuList.append(self.vtx_current)
            self.vtx_toVisit.remove(self.vtx_current)
            self.distTravelled  += CommonKnowledge.adjMtxMidGraph.get_edglength(self.vtx_current, self.vtx_Next)
            self.timeTravalled  += CommonKnowledge.adjMtxMidGraph.get_edgTime(self.vtx_current, self.vtx_Next)
            self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost(self.vtx_current, self.vtx_Next)
            
            #Stop the research if the ant come back to the the deposit point
            if(self.vtx_Next.get_ID() == CommonKnowledge.vtx_init.get_ID() ):
                self.antState       = State.RETURNING
                self.vtx_current    = self.vtx_Next
                self.vtx_tabuList.append(self.vtx_current)
                self.vtx_toVisit.remove(self.vtx_current)
                
                #Debug line
                #print("Ant: {}, Path: {}, length: {}".format(self.ID, self.vtx_tabuList, self.distTravelled))
                return False
            
            self.vtx_current = self.vtx_Next   #the ant have to find the next vertex to reach
            self.vtx_Next = None
            del self.neigb_tabuList[:]
              
            return True
            
        else: #The vertex can't be reach, have to test its neighbors to find one reachable
            
            #get neighbors list of the current vertex 
            neigbs = CommonKnowledge.adjMtxMidGraph.get_Neighboor_VTX(self.vtx_current)
            
            while len(neigbs) >= 0:
            
                #chose an elm randomly
                item = random.choice(neigbs)
                
                #test if the neighbor is reachable
                if item.get_vtx_end() in self.vtx_toVisit:
                    
                    self.vtx_tabuList.append(self.vtx_current)
                    self.vtx_toVisit.remove(self.vtx_current)
                    self.distTravelled  += CommonKnowledge.adjMtxMidGraph.get_edglength(self.vtx_current, item.get_vtx_end())
                    self.timeTravalled  += CommonKnowledge.adjMtxMidGraph.get_edgTime(self.vtx_current, item.get_vtx_end())
                    self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost(self.vtx_current, item.get_vtx_end())
                    
                    #Stop the research if the ant come back to the the deposit point
                    if(item.get_vtx_end().get_ID() == CommonKnowledge.vtx_init.get_ID() ):
                        self.antState       = State.RETURNING
                        self.vtx_current    = item.get_vtx_end()
                        self.vtx_tabuList.append(self.vtx_current)
                        self.vtx_toVisit.remove(self.vtx_current)
                        del neigbs[:]
                        
                        #Debug line
                        #print("Ant: {}, Path: {}, length: {}".format(self.ID, self.vtx_tabuList, self.distTravelled))
                        return False
                    
                    self.vtx_current = item.get_vtx_end()   #the ant have to find the next vertex to reach
                    self.vtx_Next = None
                    del self.neigb_tabuList[:]
                    del neigbs[:]
                      
                    return True
                
                neigbs.remove(item)
        
    
    def toReach_TSP_CUG_lowPerf(self):
        '''
        Define how an ant build TSP solution in a Complete Undirected Graph
        '''
        #when we are sure that the current ant visited all point, allow he to return at the deposit
        if len(self.vtx_tabuList) < len(CommonKnowledge.deliveryList):
            #Return the heuristic edge destination determined by the DorigoProb
            self.vtx_Next = self.dorigo_prob(self.vtx_current).get_vtx_end()
        else:
            #if all delivery point has been visited, allow the ant to come back to the delivery point
            self.vtx_toVisit.append(CommonKnowledge.vtx_init)
            self.vtx_Next = CommonKnowledge.vtx_init
        
        #Test if the next vertex can be reach
        if self.vtx_Next in self.vtx_toVisit:
            
            self.vtx_tabuList.append(self.vtx_current)
            self.vtx_toVisit.remove(self.vtx_current)
            self.distTravelled  += CommonKnowledge.adjMtxMidGraph.get_edglength(self.vtx_current, self.vtx_Next)
            self.timeTravalled  += CommonKnowledge.adjMtxMidGraph.get_edgTime(self.vtx_current, self.vtx_Next)
            self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost(self.vtx_current, self.vtx_Next)
            
            #Stop the research if the ant come back to the the deposit point
            if(self.vtx_Next.get_ID() == CommonKnowledge.vtx_init.get_ID() ):
                self.antState       = State.RETURNING
                self.vtx_current    = self.vtx_Next
                self.vtx_tabuList.append(self.vtx_current)
                self.vtx_toVisit.remove(self.vtx_current)
                
                #Debug line
                #print("Ant: {}, Path: {}, length: {}".format(self.ID, self.vtx_tabuList, self.distTravelled))
                return False
            
            self.vtx_current = self.vtx_Next   #the ant have to find the next vertex to reach
            self.vtx_Next = None
            del self.neigb_tabuList[:]
              
            return True
            
        else: #The vertex can't be reach, have to find a new one

            #Fill the tabu list of tested neighbors
            if self.vtx_Next not in self.neigb_tabuList:
                if len(self.neigb_tabuList) < len(CommonKnowledge.adjMtxMidGraph.get_Neighboor_VTX(self.vtx_current)):
                    self.neigb_tabuList.append(self.vtx_Next)
                    return True
            
            else:
                return True
            
    def toReach_NCUD(self):
        """
        Define how an ant build a turn in a Not Complete Undirected Graph
        """
        
        #Return the heuristic edge destination determined by the DorigoProb
        self.vtx_Next = self.dorigo_prob_VRP(self.vtx_current).get_vtx_end()
        
        #Test if the next vertex can be reach
        if self.vtx_Next in self.vtx_toVisit:
            
            #check that the next point to reach is different from the starting one (deposit)
            if self.vtx_Next.get_ID == CommonKnowledge.vtx_init.get_ID():
                self.distTravelled += CommonKnowledge.adjMtxMidGraph.get_edglength(self.vtx_current, self.vtx_Next)
                self.timeTravalled += CommonKnowledge.adjMtxMidGraph.get_edgTime(self.vtx_current, self.vtx_Next)
            
            else:
                #check if ant is at it's starting point
                if self.vtx_current.get_ID() == CommonKnowledge.vtx_init.get_ID():
                    self.distTravelled += CommonKnowledge.adjMtxMidGraph.get_edglength(self.vtx_current, self.vtx_Next)
                    self.timeTravalled += CommonKnowledge.adjMtxMidGraph.get_edgTime(self.vtx_current, self.vtx_Next)
                    
                else:
                    self.vtx_tabuList.append(self.vtx_current)
                    self.vtx_toVisit.remove(self.vtx_current)
                    self.distTravelled  += CommonKnowledge.adjMtxMidGraph.get_edglength(self.vtx_current, self.vtx_Next)
                    self.timeTravalled  += CommonKnowledge.adjMtxMidGraph.get_edgTime(self.vtx_current, self.vtx_Next)
                    self.SOE            -= CommonKnowledge.adjMtxMidGraph.get_edgNrjCost(self.vtx_current, self.vtx_Next)
                    
                    #Kill the current ant if its nrj capacity get lower than 20%
                    if(self.SOE <= CommonKnowledge.minSOE):
                        print("Current ant Kills, due to nrj Capacity Min < 20% of battery capacity")
                        self.antState       = State.KILLED
                        self.vtx_current    = CommonKnowledge.vtx_init
                        del self.vtx_tabuList[:]        #flush the tabu list
                        del self.vtx_toVisit[:]         #flush the to visit list
                        self.distTravelled  = sys.maxsize #flush the total dist. travel
                        return False
                        
            
            #Stop the research if the ant return to the init. vertex
            if(self.vtx_Next.get_ID() == CommonKnowledge.vtx_init.get_ID() ):
                self.antState       = State.RETURNING
                self.vtx_current    = self.vtx_Next
                #Debug line
                #print("Ant: {}, Path: {}, length: {}".format(self.ID, self.vtx_tabuList, self.distTravelled))
                return False
            
            #Kill the ant if it is in dead end (No neighbors to visit)
            #Warning, this case work only for directed graph
            if len(CommonKnowledge.adjMtxMidGraph.get_Neighboor_VTX(self.vtx_Next)) == 0:
                self.antState       = State.KILLED
                self.vtx_current    = CommonKnowledge.vtx_init
                del self.vtx_tabuList[:]        #flush the tabu list
                del self.vtx_toVisit[:]         #flush the to visit list
                self.distTravelled  = sys.maxsize #flush the total dist. travel
                return False
        
            self.vtx_current = self.vtx_Next   #the ant have to find the next vertex to reach
            self.vtx_Next = None             
            return True
        
        else: #The vertex can't be reach, have to find a new one
            
            #Fill the tabu list of tested neighbors
            if ( len(self.neigb_tabuList) < len(CommonKnowledge.adjMtxMidGraph.get_Neighboor_VTX(self.vtx_current))
                and (self.vtx_Next not in self.neigb_tabuList) ):
                self.neigb_tabuList.append(self.vtx_Next)
                return True
            
            else:
                #The tested neighbors list is full, we kill the ant
                self.antState = State.KILLED
                self.vtx_current  = CommonKnowledge.vtx_init
                del self.vtx_tabuList[:]        #flush the tabu list
                del self.vtx_toVisit[:]         #flush the to visit list
                del self.neigb_tabuList[:]      #flush the tested neighbors tabu list
                self.distTravelled = sys.maxsize #flush the total dist. travel
                return False             
    
    def dorigo_prob_VRP(self, vtx_p):
        """
        Calculate the probability for the next destination
        Return an edge
        """
        #neighbors_EDGE  = CommonKnowledge.adjMtxMidGraph.get_Neighboor_VTX(vtx_p) #get vertices neighbors of the given vtx
        neighbors_EDGE = self.adjLocalMtxMidGraph.get_Neighboor_VTX(vtx_p) #get vertices neighbors of the given vtx
        PhLg_tab        = []
        PhLg_Sum        = 0.0
        DorigoProb      = []
        DorigoProb_sum  = 0.0
        bundMark_tab    = []
        rtEdge          = Edge
        
        #Calculate Pheromones/Length ratio define as Tij * (Nij) for all neighbor of the current Vertex
        #with Tij = pheromone trail strength ; Nij = 1/Distance between vtxA, vtxB 
        for elmt in neighbors_EDGE:
            tmp = CommonKnowledge.get_pheromones(self.adjLocalMtxMidGraph.get_vtxIdx(elmt.get_vtx_begin()),
                                                 self.adjLocalMtxMidGraph.get_vtxIdx(elmt.get_vtx_end())
                                                 )* (1.0 / float(elmt.get_length()))
            PhLg_tab.append(tmp);
            PhLg_Sum += tmp;
        
        #Calculate the Dorigo probability for all neighbor of the current vertex
        for i in range (0, len(neighbors_EDGE)):
            if PhLg_Sum != 0:
                DorigoProb.append(PhLg_tab[i] / PhLg_Sum)
                DorigoProb_sum += PhLg_tab[i] / PhLg_Sum            #according to proba. calc. the sum should == 1
  
        #Generate a random edge according to the Dorigo prob
        if PhLg_Sum == 0:
             
            rand = random.randint(0, (len(neighbors_EDGE)-1) ) #rand between [0; nbrOfNeighbors-1]            
            rtEdge = neighbors_EDGE[rand]
            self.edg_tabuList.append(rtEdge)
        else:
            rand = random.random() #random number between [0.0; 1.0]
            
            #Generate boundary markers
            for i in range(0, len(DorigoProb)):
                if i == 0:
                    bundMark_tab.append( DorigoProb[i] )
                else:
                    bundMark_tab.append( bundMark_tab[i-1] + DorigoProb[i] )            
            
            #Select an edge according to boundary marker
            for i in range(0, len(neighbors_EDGE)):
                if rand <= bundMark_tab[i]:
                    rtEdge = neighbors_EDGE[i]
                    self.edg_tabuList.append(neighbors_EDGE[i])
                    break
                        
        return rtEdge
    
    def dorigo_prob(self, vtx_p):
        """
        Calculate the probability for the next destination
        Return an edge
        """
        neighbors_EDGE  = CommonKnowledge.adjMtxMidGraph.get_Neighboor_VTX(vtx_p) #get vertices neighbors of the given vtx
        PhLg_tab        = []
        PhLg_Sum        = 0.0
        DorigoProb      = []
        DorigoProb_sum  = 0.0
        bundMark_tab    = []
        rtEdge          = Edge
        
        #Calculate Pheromones/Length ratio define as Tij * (Nij) for all neighbor of the current Vertex
        #with Tij = pheromone trail strength ; Nij = 1/Distance between vtxA, vtxB 
        for elmt in neighbors_EDGE:
            tmp = CommonKnowledge.get_pheromones(CommonKnowledge.adjMtxMidGraph.get_vtxIdx(elmt.get_vtx_begin()),
                                                 CommonKnowledge.adjMtxMidGraph.get_vtxIdx(elmt.get_vtx_end())
                                                 )* (1.0 / float(elmt.get_length()))
            PhLg_tab.append(tmp);
            PhLg_Sum += tmp;
        
        #Calculate the Dorigo probability for all neighbor of the current vertex
        for i in range (0, len(neighbors_EDGE)):
            if PhLg_Sum != 0:
                DorigoProb.append(PhLg_tab[i] / PhLg_Sum)
                DorigoProb_sum += PhLg_tab[i] / PhLg_Sum            #according to proba. calc. the sum should == 1
  
        #Generate a random edge according to the Dorigo prob
        if PhLg_Sum == 0:
            rand = random.randint(0, (len(neighbors_EDGE)-1) ) #rand between [0; nbrOfNeighbors-1]
            rtEdge = neighbors_EDGE[rand]
            self.edg_tabuList.append(rtEdge)
        else:
            rand = random.random() #random number between [0.0; 1.0]
            
            #Generate boundary markers
            for i in range(0, len(DorigoProb)):
                if i == 0:
                    bundMark_tab.append( DorigoProb[i] )
                else:
                    bundMark_tab.append( bundMark_tab[i-1] + DorigoProb[i] )            
            
            #Select an edge according to boundary marker
            for i in range(0, len(neighbors_EDGE)):
                if rand <= bundMark_tab[i]:
                    rtEdge = neighbors_EDGE[i]
                    self.edg_tabuList.append(neighbors_EDGE[i])
                    break
                        
        return rtEdge
    
    def toVisit(self):
        """
        Create list of vertices to visit based on middle graph.
        Release a local copy of the "adjMtxMidGraph", to allow the ant to work on it
        """
        #local copy adjMtxMidGraph
        self.adjLocalMtxMidGraph = copy.deepcopy(CommonKnowledge.adjMtxMidGraph)
        
        #get warehouse vertex thank to his ID
        self.vtx_current = self.adjLocalMtxMidGraph.get_vtx(CommonKnowledge.warehouse_vertex)
        
        #list of customer based on local copy of adjacency Mtx Middle Graph
        #self.vtx_toVisit = CommonKnowledge.adjMtxMidGraph.get_Vertices()
        self.vtx_toVisit = self.adjLocalMtxMidGraph.get_Vertices()
    
    def visitedVtx_toString(self):
        """
        Return all visited vertices of an Ant
        """
        str=""
        for vtx in self.vtx_tabuList:
            str += "{},".format(vtx.get_ID())
        return str
    
    def get_tabuList_asString(self):
        '''
        Return the tabu list as a list of string
        '''
        tmpList = []
        for elm in self.vtx_tabuList:
            tmpList.append(elm.get_ID())
        return tmpList
    
    def get_warehouse_vtx(self):
        '''
        Return the warehouse vertex according to his ID (string)
        '''
        return self.adjLocalMtxMidGraph.get_vtx(CommonKnowledge.warehouse_vertex)

class State:
    """
    This enumeration define the current ant state over the course of the ant colony algorithm 
    """
    HANDLE          = 1
    SEARCHING_PATH  = 2
    RETURNING       = 3
    KILLED          = 4
