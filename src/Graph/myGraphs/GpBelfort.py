'''
Created on 21 mai 2020

@author: promet
'''

from Graph.Vertex import Vertex
from Graph.Edge import Edge
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge
from Graph.MtxGraph import MtxGraph
from Graph.myGraphs.bdd_Graph.dbExploit import dbExploit, DBDEBUG
from Simulator.DEBUG import DEBUG_MODE


class GpBelfort:
    
    vtxList = []
    edgList = []
    
    @staticmethod
    def create():  #def create( warehouse_p ):
        '''
        Initialize the public transportation system graph of Belfort  
        
        Create vertices, based on city bus-station
        '''
        #FirstLine - Résidences -> Bruxelles
        GpBelfort.vtxList.append(Vertex("La Douce"))
        GpBelfort.vtxList.append(Vertex("Signoret"))
        GpBelfort.vtxList.append(Vertex("Schuman"))
        GpBelfort.vtxList.append(Vertex("Bruxelles"))
        #FirstLine - Jaurès Hôpital -> Valdoie
        GpBelfort.vtxList.append(Vertex("Jaurès Hôpital"))
        GpBelfort.vtxList.append(Vertex("Strasbourg"))
        GpBelfort.vtxList.append(Vertex("Colmar"))
        GpBelfort.vtxList.append(Vertex("Roseraie"))
        GpBelfort.vtxList.append(Vertex("Marché Vosges"))
        GpBelfort.vtxList.append(Vertex("Salbert"))
        GpBelfort.vtxList.append(Vertex("Rubans"))
        
        
        #SecondLine - Bavilliers -> Bavilliers
        GpBelfort.vtxList.append(Vertex("La Dame"))
        GpBelfort.vtxList.append(Vertex("La Belle"))        
        #SecondLine - Argiésans -> Bavilliers
        '''
        GpBelfort.vtxList.append(Vertex("Acacias"))
        GpBelfort.vtxList.append(Vertex("Argiésans Centre"))
        GpBelfort.vtxList.append(Vertex("Zi de Bavilliers"))
        GpBelfort.vtxList.append(Vertex("Rte d'Urcerey"))
        GpBelfort.vtxList.append(Vertex("Route de Buc"))
        '''
        #SecondLine - Bavilliers -> Bonneff
        GpBelfort.vtxList.append(Vertex("Bavilliers"))
        GpBelfort.vtxList.append(Vertex("Pont Canal"))
        GpBelfort.vtxList.append(Vertex("Mozart"))
        GpBelfort.vtxList.append(Vertex("Bonneff"))
        #SecondLine - Mieg -> Cravanche
        GpBelfort.vtxList.append(Vertex("Mieg"))
        GpBelfort.vtxList.append(Vertex("Saget"))
        GpBelfort.vtxList.append(Vertex("Ste Thérèse"))
        GpBelfort.vtxList.append(Vertex("Grand' Combe"))
        GpBelfort.vtxList.append(Vertex("Laurent Thierry"))
        GpBelfort.vtxList.append(Vertex("Alstom Étang"))
        GpBelfort.vtxList.append(Vertex("Techn' Hom Cravanche"))
        #SecondLine - Les Perches -> Justice
        GpBelfort.vtxList.append(Vertex("Les Perches"))
        GpBelfort.vtxList.append(Vertex("Altkirch"))
        GpBelfort.vtxList.append(Vertex("Sellier"))
        GpBelfort.vtxList.append(Vertex("Parant"))
        GpBelfort.vtxList.append(Vertex("Cimetière Militaire"))
        GpBelfort.vtxList.append(Vertex("Laurencie"))
        GpBelfort.vtxList.append(Vertex("CFA"))
        GpBelfort.vtxList.append(Vertex("Bichat"))
        GpBelfort.vtxList.append(Vertex("Hauts de Belfort"))
        GpBelfort.vtxList.append(Vertex("Camus"))
        
        
        #ThirdLine - Gare TGV -> OEufs Frais
        GpBelfort.vtxList.append(Vertex("1er RA"))
        GpBelfort.vtxList.append(Vertex("Gare TGV"))
        GpBelfort.vtxList.append(Vertex("Rte de Meroux"))
        GpBelfort.vtxList.append(Vertex("Moval"))
        GpBelfort.vtxList.append(Vertex("Hôpital NFC"))
        GpBelfort.vtxList.append(Vertex("Sévenans UTBM"))
        #ThirdLine - Châtenois -> OEufs Frais
        GpBelfort.vtxList.append(Vertex("Géhant"))
        GpBelfort.vtxList.append(Vertex("Châtenois"))
        GpBelfort.vtxList.append(Vertex("Complexe Sportif"))
        GpBelfort.vtxList.append(Vertex("Châtenois Forges"))
        GpBelfort.vtxList.append(Vertex("Rte de Vourvenans"))
        GpBelfort.vtxList.append(Vertex("Trévenans"))
        GpBelfort.vtxList.append(Vertex("Bascule"))
        GpBelfort.vtxList.append(Vertex("Conforama"))
        GpBelfort.vtxList.append(Vertex("Rte de Bermont"))
        #ThirdLine - OEufs Frais -> Varonne
        GpBelfort.vtxList.append(Vertex("OEufs Frais"))
        GpBelfort.vtxList.append(Vertex("Port de Botans"))
        GpBelfort.vtxList.append(Vertex("Andelnans Prés"))
        GpBelfort.vtxList.append(Vertex("Grottes"))
        GpBelfort.vtxList.append(Vertex("Éluard"))
        GpBelfort.vtxList.append(Vertex("Jacquot"))
        GpBelfort.vtxList.append(Vertex("Bosmont"))
        GpBelfort.vtxList.append(Vertex("Varonne"))
        #ThirdLine - Techn' Hom 1 UTBM -> Valdoie
        GpBelfort.vtxList.append(Vertex("Techn' Hom 1 UTBM"))
        GpBelfort.vtxList.append(Vertex("IUT"))
        GpBelfort.vtxList.append(Vertex("Techn' Hom 2"))
        GpBelfort.vtxList.append(Vertex("Techn' Hom 3"))
        GpBelfort.vtxList.append(Vertex("Benoit Frachon"))
        GpBelfort.vtxList.append(Vertex("Méchelle"))
        
        
        #FourthLine - Froideval -> Molière
        '''
        GpBelfort.vtxList.append(Vertex("Berger"))
        GpBelfort.vtxList.append(Vertex("L'assise"))
        GpBelfort.vtxList.append(Vertex("St Antonin"))
        '''
        GpBelfort.vtxList.append(Vertex("Pierre Engel"))
        GpBelfort.vtxList.append(Vertex("Marcel Braun"))
        GpBelfort.vtxList.append(Vertex("Chênois"))
        GpBelfort.vtxList.append(Vertex("Poincaré"))
        GpBelfort.vtxList.append(Vertex("Renan"))
        GpBelfort.vtxList.append(Vertex("Molière"))
        #FourthLine - Hôpital -> Offemont
        GpBelfort.vtxList.append(Vertex("Hôpital"))
        GpBelfort.vtxList.append(Vertex("Mulhouse"))
        GpBelfort.vtxList.append(Vertex("Bohn"))
        GpBelfort.vtxList.append(Vertex("Madagascar"))
        GpBelfort.vtxList.append(Vertex("Ferrette"))
        GpBelfort.vtxList.append(Vertex("Parmentier"))
        GpBelfort.vtxList.append(Vertex("Courbet"))
        GpBelfort.vtxList.append(Vertex("Centre Commercial"))
        GpBelfort.vtxList.append(Vertex("Romaine"))
        GpBelfort.vtxList.append(Vertex("Ballon"))
        GpBelfort.vtxList.append(Vertex("Moulin"))
        GpBelfort.vtxList.append(Vertex("Champs Cerisiers"))
        
        
        #FifthLine - Essert -> Guidon
        GpBelfort.vtxList.append(Vertex("Bois Joli"))
        GpBelfort.vtxList.append(Vertex("Carrières"))
        GpBelfort.vtxList.append(Vertex("Gardey"))
        #FifthLine - Marseille -> Giromagny par Petitmagny
        GpBelfort.vtxList.append(Vertex("Marseille"))
        GpBelfort.vtxList.append(Vertex("Les Forges"))
        GpBelfort.vtxList.append(Vertex("Champ de Mars"))
        GpBelfort.vtxList.append(Vertex("Martinet"))
        GpBelfort.vtxList.append(Vertex("Marchegay"))
        GpBelfort.vtxList.append(Vertex("Pont Blanc"))
        GpBelfort.vtxList.append(Vertex("Paquis"))
        GpBelfort.vtxList.append(Vertex("Savoureuse"))
        GpBelfort.vtxList.append(Vertex("Turenne"))
        GpBelfort.vtxList.append(Vertex("Nallet"))
        GpBelfort.vtxList.append(Vertex("Beurrerie"))
        GpBelfort.vtxList.append(Vertex("Prés d'Aumont"))
        GpBelfort.vtxList.append(Vertex("Mermoz"))
        GpBelfort.vtxList.append(Vertex("Aubépines"))
        GpBelfort.vtxList.append(Vertex("Rosemontoise"))
        GpBelfort.vtxList.append(Vertex("Route de Sermamagny"))
        GpBelfort.vtxList.append(Vertex("Eloie"))
        GpBelfort.vtxList.append(Vertex("Verdoyeux"))
        GpBelfort.vtxList.append(Vertex("Chaume"))
        
        
        #EighthLine - Cravanche -> Essert
        GpBelfort.vtxList.append(Vertex("Schweitzer"))
        GpBelfort.vtxList.append(Vertex("Cravanche Centre"))
        GpBelfort.vtxList.append(Vertex("Cravanchoise"))
        GpBelfort.vtxList.append(Vertex("Haut des Près"))
        GpBelfort.vtxList.append(Vertex("La Forêt"))
        GpBelfort.vtxList.append(Vertex("Bas du Village"))
        GpBelfort.vtxList.append(Vertex("Frezard"))
        GpBelfort.vtxList.append(Vertex("Pins"))
        GpBelfort.vtxList.append(Vertex("Terrasses"))
        
        
        #NinthLine - Miotte -> République
        '''
        GpBelfort.vtxList.append(Vertex("Clinique"))
        GpBelfort.vtxList.append(Vertex("Haute Miotte"))
        GpBelfort.vtxList.append(Vertex("Deshaie"))
        GpBelfort.vtxList.append(Vertex("Picard"))
        GpBelfort.vtxList.append(Vertex("As de Trèfle"))
        '''
        
        
        #Common Bus stop station (North to South)
        GpBelfort.vtxList.append(Vertex("Mairie"))
        GpBelfort.vtxList.append(Vertex("Blumberg"))
        GpBelfort.vtxList.append(Vertex("1re Armée"))
        GpBelfort.vtxList.append(Vertex("Paul Bert"))
        GpBelfort.vtxList.append(Vertex("Briand"))
        #GpBelfort.vtxList.append(Vertex("Miotte"))
        #GpBelfort.vtxList.append(Vertex("Atria"))
        GpBelfort.vtxList.append(Vertex("Clemenceau"))
        GpBelfort.vtxList.append(Vertex("Rabin"))
        GpBelfort.vtxList.append(Vertex("République"))
        GpBelfort.vtxList.append(Vertex("Foch"))
        GpBelfort.vtxList.append(Vertex("Schwob"))
        GpBelfort.vtxList.append(Vertex("Denfert Rochereau"))
        GpBelfort.vtxList.append(Vertex("Strotz"))
        GpBelfort.vtxList.append(Vertex("4 As"))
        GpBelfort.vtxList.append(Vertex("Hatry"))
        GpBelfort.vtxList.append(Vertex("Dubail"))
        GpBelfort.vtxList.append(Vertex("Follereau"))
        GpBelfort.vtxList.append(Vertex("Guidon"))
        GpBelfort.vtxList.append(Vertex("Madrid"))
        GpBelfort.vtxList.append(Vertex("Blum"))
        GpBelfort.vtxList.append(Vertex("Fg de Lyon"))
        GpBelfort.vtxList.append(Vertex("Gare"))
        GpBelfort.vtxList.append(Vertex("Sernam"))
        GpBelfort.vtxList.append(Vertex("Colbert"))
        GpBelfort.vtxList.append(Vertex("Multiplexe"))
        GpBelfort.vtxList.append(Vertex("Le Nôtre"))
        GpBelfort.vtxList.append(Vertex("La Poste"))
        GpBelfort.vtxList.append(Vertex("Essert"))
        GpBelfort.vtxList.append(Vertex("De Gaulle"))
        GpBelfort.vtxList.append(Vertex("Chemin de la ferme"))
        GpBelfort.vtxList.append(Vertex("Ballinamuck"))
        
        
        
        '''
        Create edges, composed of two vertices
        Belfort is an undirected graph
        '''
        #FirstLine - RedLine
            #RESIDENCES -> Madrid
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Douce")  , GpBelfort.getVtx("Signoret")  ,dbExploit.section_getData("La Douce", "Signoret")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Signoret")  , GpBelfort.getVtx("Schuman")   ,dbExploit.section_getData("Signoret", "Schuman")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schuman")   , GpBelfort.getVtx("Bruxelles") ,dbExploit.section_getData("Schuman", "Bruxelles")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bruxelles") , GpBelfort.getVtx("Madrid")    ,dbExploit.section_getData("Bruxelles", "Madrid")))
            #Madrid -> RESIDENCES
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid")    , GpBelfort.getVtx("Bruxelles") ,dbExploit.section_getData("Madrid", "Bruxelles")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bruxelles") , GpBelfort.getVtx("Schuman")   ,dbExploit.section_getData("Bruxelles", "Schuman")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schuman")   , GpBelfort.getVtx("Signoret")  ,dbExploit.section_getData("Schuman", "Signoret")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Signoret")  , GpBelfort.getVtx("La Douce")  ,dbExploit.section_getData("Signoret", "La Douce")))
            #Clemenceau -> VALDOIE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("Jaurès Hôpital"),dbExploit.section_getData("Clemenceau", "Jaurès Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jaurès Hôpital"), GpBelfort.getVtx("Strasbourg"),dbExploit.section_getData("Jaurès Hôpital", "Strasbourg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strasbourg"), GpBelfort.getVtx("Colmar")        ,dbExploit.section_getData("Strasbourg", "Colmar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colmar"), GpBelfort.getVtx("Roseraie")          ,dbExploit.section_getData("Colmar", "Roseraie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Roseraie"), GpBelfort.getVtx("Marché Vosges")   ,dbExploit.section_getData("Roseraie", "Marché Vosges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marché Vosges"), GpBelfort.getVtx("1re Armée")  ,dbExploit.section_getData("Marché Vosges", "1re Armée")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1re Armée"), GpBelfort.getVtx("Salbert")        ,dbExploit.section_getData("1re Armée", "Salbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Salbert"), GpBelfort.getVtx("Rubans")           ,dbExploit.section_getData("Salbert", "Rubans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rubans"), GpBelfort.getVtx("Blumberg")          ,dbExploit.section_getData("Rubans", "Blumberg")))
            #VALDOIE -> Clemenceau
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mairie"), GpBelfort.getVtx("Rubans")            ,dbExploit.section_getData("Mairie", "Rubans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rubans"), GpBelfort.getVtx("Salbert")           ,dbExploit.section_getData("Rubans", "Salbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Salbert"), GpBelfort.getVtx("1re Armée")        ,dbExploit.section_getData("Salbert", "1re Armée")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1re Armée"), GpBelfort.getVtx("Marché Vosges")  ,dbExploit.section_getData("1re Armée", "Marché Vosges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marché Vosges"), GpBelfort.getVtx("Roseraie")   ,dbExploit.section_getData("Marché Vosges", "Roseraie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Roseraie"), GpBelfort.getVtx("Colmar")          ,dbExploit.section_getData("Roseraie", "Colmar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colmar"), GpBelfort.getVtx("Strasbourg")        ,dbExploit.section_getData("Colmar", "Strasbourg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strasbourg"), GpBelfort.getVtx("Jaurès Hôpital"),dbExploit.section_getData("Strasbourg", "Jaurès Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jaurès Hôpital"), GpBelfort.getVtx("Clemenceau"),dbExploit.section_getData("Jaurès Hôpital", "Clemenceau")))
        
        
        
        #SecondLine - OrangeLine
            #JUSTICE ->  Multiplexe
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hauts de Belfort"), GpBelfort.getVtx("Camus")   ,dbExploit.section_getData("Hauts de Belfort", "Camus")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Camus"), GpBelfort.getVtx("CFA")                ,dbExploit.section_getData("Camus", "CFA")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("CFA"), GpBelfort.getVtx("Laurencie")            ,dbExploit.section_getData("CFA", "Laurencie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurencie"), GpBelfort.getVtx("Cimetière Militaire"),dbExploit.section_getData("Laurencie", "Cimetière Militaire")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cimetière Militaire"), GpBelfort.getVtx("Parant"),dbExploit.section_getData("Cimetière Militaire", "Parant")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parant"), GpBelfort.getVtx("Sellier")           ,dbExploit.section_getData("Parant", "Sellier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sellier"), GpBelfort.getVtx("Altkirch")         ,dbExploit.section_getData("Sellier", "Altkirch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Altkirch"), GpBelfort.getVtx("Les Perches")     ,dbExploit.section_getData("Altkirch", "Les Perches")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Perches"), GpBelfort.getVtx("Multiplexe")   ,dbExploit.section_getData("Les Perches", "Multiplexe")))
            #Multiplexe -> JUSTICE  
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Multiplexe"), GpBelfort.getVtx("Les Perches")   ,dbExploit.section_getData("Multiplexe", "Les Perches")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Perches"), GpBelfort.getVtx("Altkirch")     ,dbExploit.section_getData("Les Perches", "Altkirch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Altkirch"), GpBelfort.getVtx("Sellier")         ,dbExploit.section_getData("Altkirch", "Sellier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sellier"), GpBelfort.getVtx("Parant")           ,dbExploit.section_getData("Sellier", "Parant")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parant"), GpBelfort.getVtx("Cimetière Militaire"),dbExploit.section_getData("Parant", "Cimetière Militaire")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cimetière Militaire"), GpBelfort.getVtx("Laurencie"),dbExploit.section_getData("Cimetière Militaire", "Laurencie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurencie"), GpBelfort.getVtx("CFA")            ,dbExploit.section_getData("Laurencie", "CFA")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("CFA"), GpBelfort.getVtx("Bichat")               ,dbExploit.section_getData("CFA", "Bichat")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bichat"), GpBelfort.getVtx("Hauts de Belfort")  ,dbExploit.section_getData("Bichat", "Hauts de Belfort")))
            #BAVILLIERS -> Bavilliers
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Dame"), GpBelfort.getVtx("La Belle")         ,dbExploit.section_getData("La Dame", "La Belle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Belle"), GpBelfort.getVtx("Bavilliers")      ,dbExploit.section_getData("La Belle", "Bavilliers")))
            #Bavilliers -> BAVILLIERS
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bavilliers"), GpBelfort.getVtx("La Belle")      ,dbExploit.section_getData("Bavilliers", "La Belle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Belle"), GpBelfort.getVtx("La Dame")         ,dbExploit.section_getData("La Belle", "La Dame")))
            #ARGIESANS -> Bavilliers
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Acacias"), GpBelfort.getVtx("Argiésans Centre")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Argiésans Centre"), GpBelfort.getVtx("Zi de Bavilliers")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Zi de Bavilliers"), GpBelfort.getVtx("Rte d'Urcerey")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte d'Urcerey"), GpBelfort.getVtx("Route de Buc")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Route de Buc"), GpBelfort.getVtx("Bavilliers")))
        '''
            #Bavilliers -> ARGIESANS
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bavilliers"), GpBelfort.getVtx("Route de Buc")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Route de Buc"), GpBelfort.getVtx("Rte d'Urcerey")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte d'Urcerey"), GpBelfort.getVtx("Zi de Bavilliers")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Zi de Bavilliers"), GpBelfort.getVtx("Argiésans Centre")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Argiésans Centre"), GpBelfort.getVtx("Acacias")))
        '''
            #Bavilliers -> Le Nôtre
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bavilliers"), GpBelfort.getVtx("Pont Canal"),dbExploit.section_getData("Bavilliers", "Pont Canal")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Canal"), GpBelfort.getVtx("Mozart")    ,dbExploit.section_getData("Pont Canal", "Mozart")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mozart"), GpBelfort.getVtx("Bonneff")       ,dbExploit.section_getData("Mozart", "Bonneff")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bonneff"), GpBelfort.getVtx("Le Nôtre")     ,dbExploit.section_getData("Bonneff", "Le Nôtre")))
            #Le Nôtre -> Bavilliers 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Le Nôtre"), GpBelfort.getVtx("Bonneff")     ,dbExploit.section_getData("Le Nôtre", "Bonneff")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bonneff"), GpBelfort.getVtx("Mozart")       ,dbExploit.section_getData("Bonneff", "Mozart")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mozart"), GpBelfort.getVtx("Pont Canal")    ,dbExploit.section_getData("Mozart", "Pont Canal")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Canal"), GpBelfort.getVtx("Bavilliers"),dbExploit.section_getData("Pont Canal", "Bavilliers")))
            #Rabin -> CRAVANCHE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Mieg")           ,dbExploit.section_getData("Rabin", "Mieg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mieg"), GpBelfort.getVtx("Saget")           ,dbExploit.section_getData("Mieg", "Saget")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Saget"), GpBelfort.getVtx("Ste Thérèse")    ,dbExploit.section_getData("Saget", "Ste Thérèse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ste Thérèse"), GpBelfort.getVtx("Grand' Combe")         ,dbExploit.section_getData("Ste Thérèse", "Grand' Combe")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grand' Combe"), GpBelfort.getVtx("Laurent Thierry")     ,dbExploit.section_getData("Grand' Combe", "Laurent Thierry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurent Thierry"), GpBelfort.getVtx("Alstom Étang")     ,dbExploit.section_getData("Laurent Thierry", "Alstom Étang")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Alstom Étang"), GpBelfort.getVtx("Techn' Hom Cravanche"),dbExploit.section_getData("Alstom Étang", "Techn' Hom Cravanche")))
            #CRAVANCHE -> Rabin 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom Cravanche"), GpBelfort.getVtx("Alstom Étang"),dbExploit.section_getData("Techn' Hom Cravanche", "Alstom Étang")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Alstom Étang"), GpBelfort.getVtx("Laurent Thierry")     ,dbExploit.section_getData("Alstom Étang", "Laurent Thierry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurent Thierry"), GpBelfort.getVtx("Grand' Combe")     ,dbExploit.section_getData("Laurent Thierry", "Grand' Combe")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grand' Combe"), GpBelfort.getVtx("Ste Thérèse")         ,dbExploit.section_getData("Grand' Combe", "Ste Thérèse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ste Thérèse"), GpBelfort.getVtx("Saget")                ,dbExploit.section_getData("Ste Thérèse", "Saget")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Saget"), GpBelfort.getVtx("Mieg")                       ,dbExploit.section_getData("Saget", "Mieg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mieg"), GpBelfort.getVtx("Rabin")                       ,dbExploit.section_getData("Mieg", "Rabin")))
        
        
        
        #ThirdLine - BlueLine
            #VALDOIE -> Follereau
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mairie"), GpBelfort.getVtx("Méchelle")              ,dbExploit.section_getData("Mairie", "Méchelle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Méchelle"), GpBelfort.getVtx("Benoit Frachon")      ,dbExploit.section_getData("Méchelle", "Benoit Frachon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Benoit Frachon"), GpBelfort.getVtx("Techn' Hom 3")  ,dbExploit.section_getData("Benoit Frachon", "Techn' Hom 3")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 3"), GpBelfort.getVtx("Techn' Hom 2")    ,dbExploit.section_getData("Techn' Hom 3", "Techn' Hom 2")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 2"), GpBelfort.getVtx("IUT")             ,dbExploit.section_getData("Techn' Hom 2", "IUT")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("IUT"), GpBelfort.getVtx("Techn' Hom 1 UTBM")        ,dbExploit.section_getData("IUT", "Techn' Hom 1 UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 1 UTBM"), GpBelfort.getVtx("Follereau")  ,dbExploit.section_getData("Techn' Hom 1 UTBM", "Follereau")))
            #Follereau -> VALDOIE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Follereau"), GpBelfort.getVtx("Techn' Hom 1 UTBM")  ,dbExploit.section_getData("Follereau", "Techn' Hom 1 UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 1 UTBM"), GpBelfort.getVtx("IUT")        ,dbExploit.section_getData("Techn' Hom 1 UTBM", "IUT")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("IUT"), GpBelfort.getVtx("Techn' Hom 2")             ,dbExploit.section_getData("IUT", "Techn' Hom 2")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 2"), GpBelfort.getVtx("Techn' Hom 3")    ,dbExploit.section_getData("Techn' Hom 2", "Techn' Hom 3")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 3"), GpBelfort.getVtx("Benoit Frachon")  ,dbExploit.section_getData("Techn' Hom 3", "Benoit Frachon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Benoit Frachon"), GpBelfort.getVtx("Méchelle")      ,dbExploit.section_getData("Benoit Frachon", "Méchelle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Méchelle"), GpBelfort.getVtx("Blumberg")            ,dbExploit.section_getData("Méchelle", "Blumberg")))
            #Multiplexe -> OEufs Frais
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Multiplexe"), GpBelfort.getVtx("Varonne")           ,dbExploit.section_getData("Multiplexe", "Varonne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Varonne"), GpBelfort.getVtx("Bosmont")              ,dbExploit.section_getData("Varonne", "Bosmont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bosmont"), GpBelfort.getVtx("Jacquot")              ,dbExploit.section_getData("Bosmont", "Jacquot")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jacquot"), GpBelfort.getVtx("Éluard")               ,dbExploit.section_getData("Jacquot", "Éluard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Éluard"), GpBelfort.getVtx("Grottes")               ,dbExploit.section_getData("Éluard", "Grottes")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grottes"), GpBelfort.getVtx("Andelnans Prés")       ,dbExploit.section_getData("Grottes", "Andelnans Prés")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Andelnans Prés"), GpBelfort.getVtx("Port de Botans"),dbExploit.section_getData("Andelnans Prés", "Port de Botans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Port de Botans"), GpBelfort.getVtx("OEufs Frais")   ,dbExploit.section_getData("Port de Botans", "OEufs Frais")))
            #OEufs Frais -> Multiplexe
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("OEufs Frais"), GpBelfort.getVtx("Port de Botans")   ,dbExploit.section_getData("OEufs Frais", "Port de Botans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Port de Botans"), GpBelfort.getVtx("Andelnans Prés"),dbExploit.section_getData("Port de Botans", "Andelnans Prés")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Andelnans Prés"), GpBelfort.getVtx("Grottes")       ,dbExploit.section_getData("Andelnans Prés", "Grottes")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grottes"), GpBelfort.getVtx("Éluard")               ,dbExploit.section_getData("Grottes", "Éluard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Éluard"), GpBelfort.getVtx("Jacquot")               ,dbExploit.section_getData("Éluard", "Jacquot")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jacquot"), GpBelfort.getVtx("Bosmont")              ,dbExploit.section_getData("Jacquot", "Bosmont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bosmont"), GpBelfort.getVtx("Varonne")              ,dbExploit.section_getData("Bosmont", "Varonne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Varonne"), GpBelfort.getVtx("Multiplexe")           ,dbExploit.section_getData("Varonne", "Multiplexe")))   
            #OEufs Frais -> GARE TGV
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("OEufs Frais"), GpBelfort.getVtx("Sévenans UTBM")    ,dbExploit.section_getData("OEufs Frais", "Sévenans UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sévenans UTBM"), GpBelfort.getVtx("Hôpital NFC")    ,dbExploit.section_getData("Sévenans UTBM", "Hôpital NFC")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital NFC"), GpBelfort.getVtx("Moval")            ,dbExploit.section_getData("Hôpital NFC", "Moval")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moval"), GpBelfort.getVtx("Rte de Meroux")          ,dbExploit.section_getData("Moval", "Rte de Meroux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Meroux"), GpBelfort.getVtx("Gare TGV")       ,dbExploit.section_getData("Rte de Meroux", "Gare TGV")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare TGV"), GpBelfort.getVtx("1er RA")              ,dbExploit.section_getData("Gare TGV", "1er RA")))   
            #GARE TGV -> OEufs Frais
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1er RA"), GpBelfort.getVtx("Gare TGV")              ,dbExploit.section_getData("1er RA", "Gare TGV")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare TGV"), GpBelfort.getVtx("Rte de Meroux")       ,dbExploit.section_getData("Gare TGV", "Rte de Meroux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Meroux"), GpBelfort.getVtx("Moval")          ,dbExploit.section_getData("Rte de Meroux", "Moval")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moval"), GpBelfort.getVtx("Hôpital NFC")            ,dbExploit.section_getData("Moval", "Hôpital NFC")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital NFC"), GpBelfort.getVtx("Sévenans UTBM")    ,dbExploit.section_getData("Hôpital NFC", "Sévenans UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sévenans UTBM"), GpBelfort.getVtx("OEufs Frais")    ,dbExploit.section_getData("Sévenans UTBM", "OEufs Frais")))    
            #OEufs Frais -> CHATENOIS
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("OEufs Frais"), GpBelfort.getVtx("Rte de Bermont")   ,dbExploit.section_getData("OEufs Frais", "Rte de Bermont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Bermont"), GpBelfort.getVtx("Conforama")     ,dbExploit.section_getData("Rte de Bermont", "Conforama")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Conforama"), GpBelfort.getVtx("Bascule")            ,dbExploit.section_getData("Conforama", "Bascule")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bascule"), GpBelfort.getVtx("Trévenans")            ,dbExploit.section_getData("Bascule", "Trévenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Trévenans"), GpBelfort.getVtx("Rte de Vourvenans")  ,dbExploit.section_getData("Trévenans", "Rte de Vourvenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Vourvenans"), GpBelfort.getVtx("Châtenois Forges")   ,dbExploit.section_getData("Rte de Vourvenans", "Châtenois Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois Forges"), GpBelfort.getVtx("Complexe Sportif")    ,dbExploit.section_getData("Châtenois Forges", "Complexe Sportif")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Complexe Sportif"), GpBelfort.getVtx("Châtenois")           ,dbExploit.section_getData("Complexe Sportif", "Châtenois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois"), GpBelfort.getVtx("Géhant")                     ,dbExploit.section_getData("Châtenois", "Géhant")))    
            #CHATENOIS -> OEufs Frais        
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Géhant"), GpBelfort.getVtx("Châtenois")                     ,dbExploit.section_getData("Géhant", "Châtenois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois"), GpBelfort.getVtx("Complexe Sportif")           ,dbExploit.section_getData("Châtenois", "Complexe Sportif")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Complexe Sportif"), GpBelfort.getVtx("Châtenois Forges")    ,dbExploit.section_getData("Complexe Sportif", "Châtenois Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois Forges"), GpBelfort.getVtx("Rte de Vourvenans")   ,dbExploit.section_getData("Châtenois Forges", "Rte de Vourvenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Vourvenans"), GpBelfort.getVtx("Trévenans")          ,dbExploit.section_getData("Rte de Vourvenans", "Trévenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Trévenans"), GpBelfort.getVtx("Bascule")                    ,dbExploit.section_getData("Trévenans", "Bascule")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bascule"), GpBelfort.getVtx("Conforama")                    ,dbExploit.section_getData("Bascule", "Conforama")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Conforama"), GpBelfort.getVtx("Rte de Bermont")             ,dbExploit.section_getData("Conforama", "Rte de Bermont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Bermont"), GpBelfort.getVtx("OEufs Frais")           ,dbExploit.section_getData("Rte de Bermont", "OEufs Frais")))
        
        
        
        #FourthLine - PurpleLine
            #FROIDEVAL -> Le Nôtre
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Berger"), GpBelfort.getVtx("L'assise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("L'assise"), GpBelfort.getVtx("St Antonin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("St Antonin"), GpBelfort.getVtx("Pierre Engel")))
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pierre Engel"), GpBelfort.getVtx("Marcel Braun"),dbExploit.section_getData("Pierre Engel", "Marcel Braun")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marcel Braun"), GpBelfort.getVtx("Chênois")     ,dbExploit.section_getData("Marcel Braun", "Chênois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chênois"), GpBelfort.getVtx("Poincaré")         ,dbExploit.section_getData("Chênois", "Poincaré")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Poincaré"), GpBelfort.getVtx("Renan")           ,dbExploit.section_getData("Poincaré", "Renan")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Renan"), GpBelfort.getVtx("Molière")            ,dbExploit.section_getData("Renan", "Molière")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Molière"), GpBelfort.getVtx("Le Nôtre")         ,dbExploit.section_getData("Molière", "Le Nôtre")))
            #Le Nôtre -> FROIDEVAL
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Le Nôtre"), GpBelfort.getVtx("Molière")         ,dbExploit.section_getData("Le Nôtre", "Molière")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Molière"), GpBelfort.getVtx("Renan")            ,dbExploit.section_getData("Molière", "Renan")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Renan"), GpBelfort.getVtx("Poincaré")           ,dbExploit.section_getData("Renan", "Poincaré")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Poincaré"), GpBelfort.getVtx("Chênois")         ,dbExploit.section_getData("Poincaré", "Chênois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chênois"), GpBelfort.getVtx("Marcel Braun")     ,dbExploit.section_getData("Chênois", "Marcel Braun")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marcel Braun"), GpBelfort.getVtx("Pierre Engel"),dbExploit.section_getData("Marcel Braun", "Pierre Engel")))
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pierre Engel"), GpBelfort.getVtx("St Antonin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("St Antonin"), GpBelfort.getVtx("L'assise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("L'assise"), GpBelfort.getVtx("Berger")))
        '''
            #Rabin -> OFFEMONT
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Hôpital")        ,dbExploit.section_getData("Rabin", "Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital"), GpBelfort.getVtx("Mulhouse")     ,dbExploit.section_getData("Hôpital", "Mulhouse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mulhouse"), GpBelfort.getVtx("Bohn")        ,dbExploit.section_getData("Mulhouse", "Bohn")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bohn"), GpBelfort.getVtx("Madagascar")      ,dbExploit.section_getData("Bohn", "Madagascar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madagascar"), GpBelfort.getVtx("Ferrette")  ,dbExploit.section_getData("Madagascar", "Ferrette")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ferrette"), GpBelfort.getVtx("Paul Bert")   ,dbExploit.section_getData("Ferrette", "Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("Parmentier") ,dbExploit.section_getData("Paul Bert", "Parmentier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parmentier"), GpBelfort.getVtx("Courbet")   ,dbExploit.section_getData("Parmentier", "Courbet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Courbet"), GpBelfort.getVtx("Briand")       ,dbExploit.section_getData("Courbet", "Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Centre Commercial") ,dbExploit.section_getData("Briand", "Centre Commercial")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Centre Commercial"), GpBelfort.getVtx("Romaine"),dbExploit.section_getData("Centre Commercial", "Romaine")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Romaine"), GpBelfort.getVtx("Ballon")           ,dbExploit.section_getData("Romaine", "Ballon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballon"), GpBelfort.getVtx("Moulin")            ,dbExploit.section_getData("Ballon", "Moulin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moulin"), GpBelfort.getVtx("Champs Cerisiers")  ,dbExploit.section_getData("Moulin", "Champs Cerisiers")))
            #OFFEMONT -> Rabin
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Champs Cerisiers"), GpBelfort.getVtx("Moulin")  ,dbExploit.section_getData("Champs Cerisiers", "Moulin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moulin"), GpBelfort.getVtx("Ballon")            ,dbExploit.section_getData("Moulin", "Ballon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballon"), GpBelfort.getVtx("Romaine")           ,dbExploit.section_getData("Ballon", "Romaine")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Romaine"), GpBelfort.getVtx("Centre Commercial"),dbExploit.section_getData("Romaine", "Centre Commercial")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Centre Commercial"), GpBelfort.getVtx("Briand") ,dbExploit.section_getData("Centre Commercial", "Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Courbet")           ,dbExploit.section_getData("Briand", "Courbet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Courbet"), GpBelfort.getVtx("Parmentier")       ,dbExploit.section_getData("Courbet", "Parmentier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parmentier"), GpBelfort.getVtx("Paul Bert")     ,dbExploit.section_getData("Parmentier", "Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("Ferrette")       ,dbExploit.section_getData("Paul Bert", "Ferrette")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ferrette"), GpBelfort.getVtx("Madagascar")      ,dbExploit.section_getData("Ferrette", "Madagascar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madagascar"), GpBelfort.getVtx("Bohn")          ,dbExploit.section_getData("Madagascar", "Bohn")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bohn"), GpBelfort.getVtx("Mulhouse")            ,dbExploit.section_getData("Bohn", "Mulhouse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mulhouse"), GpBelfort.getVtx("Hôpital")         ,dbExploit.section_getData("Mulhouse", "Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital"), GpBelfort.getVtx("Rabin")            ,dbExploit.section_getData("Hôpital", "Rabin")))
        
        
        
        #FifthLine - GreenLine
            #ESSERT -> Ballinamuck
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bois Joli"), GpBelfort.getVtx("Ballinamuck")    ,dbExploit.section_getData("Bois Joli", "Ballinamuck")))
            #Ballinamuck -> ESSERT 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballinamuck"), GpBelfort.getVtx("Bois Joli")    ,dbExploit.section_getData("Ballinamuck", "Bois Joli")))
            #La Poste -> Guidon
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Poste"), GpBelfort.getVtx("Carrières")       ,dbExploit.section_getData("La Poste", "Carrières")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Carrières"), GpBelfort.getVtx("Gardey")         ,dbExploit.section_getData("Carrières", "Gardey")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gardey"), GpBelfort.getVtx("Guidon")            ,dbExploit.section_getData("Gardey", "Guidon")))
            #Guidon -> La Poste
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Guidon"), GpBelfort.getVtx("Gardey")            ,dbExploit.section_getData("Guidon", "Gardey")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gardey"), GpBelfort.getVtx("Carrières")         ,dbExploit.section_getData("Gardey", "Carrières")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Carrières"), GpBelfort.getVtx("La Poste")       ,dbExploit.section_getData("Carrières", "La Poste")))
            #Clemenceau -> ELOIE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("Marseille")     ,dbExploit.section_getData("Clemenceau", "Marseille")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marseille"), GpBelfort.getVtx("Les Forges")     ,dbExploit.section_getData("Marseille", "Les Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Forges"), GpBelfort.getVtx("Champ de Mars") ,dbExploit.section_getData("Les Forges", "Champ de Mars")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Champ de Mars"), GpBelfort.getVtx("Briand")     ,dbExploit.section_getData("Champ de Mars", "Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Martinet")          ,dbExploit.section_getData("Briand", "Martinet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Martinet"), GpBelfort.getVtx("Marchegay")       ,dbExploit.section_getData("Martinet", "Marchegay")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marchegay"), GpBelfort.getVtx("Pont Blanc")     ,dbExploit.section_getData("Marchegay", "Pont Blanc")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Blanc"), GpBelfort.getVtx("Paquis")        ,dbExploit.section_getData("Pont Blanc", "Paquis")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paquis"), GpBelfort.getVtx("Savoureuse")        ,dbExploit.section_getData("Paquis", "Savoureuse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Savoureuse"), GpBelfort.getVtx("Turenne")       ,dbExploit.section_getData("Savoureuse", "Turenne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Turenne"), GpBelfort.getVtx("Nallet")           ,dbExploit.section_getData("Turenne", "Nallet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Nallet"), GpBelfort.getVtx("Beurrerie")         ,dbExploit.section_getData("Nallet", "Beurrerie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Beurrerie"), GpBelfort.getVtx("Prés d'Aumont")  ,dbExploit.section_getData("Beurrerie", "Prés d'Aumont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Prés d'Aumont"), GpBelfort.getVtx("Mermoz")     ,dbExploit.section_getData("Prés d'Aumont", "Mermoz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mermoz"), GpBelfort.getVtx("Aubépines")         ,dbExploit.section_getData("Mermoz", "Aubépines")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Aubépines"), GpBelfort.getVtx("Rosemontoise")   ,dbExploit.section_getData("Aubépines", "Rosemontoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rosemontoise"), GpBelfort.getVtx("Route de Sermamagny") ,dbExploit.section_getData("Rosemontoise", "Route de Sermamagny")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Route de Sermamagny"), GpBelfort.getVtx("Eloie"),dbExploit.section_getData("Route de Sermamagny", "Eloie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Eloie"), GpBelfort.getVtx("Verdoyeux")          ,dbExploit.section_getData("Eloie", "Verdoyeux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Verdoyeux"), GpBelfort.getVtx("Chaume")         ,dbExploit.section_getData("Verdoyeux", "Chaume")))
            #ELOIE -> Clemenceau 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chaume"), GpBelfort.getVtx("Verdoyeux")         ,dbExploit.section_getData("Chaume", "Verdoyeux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Verdoyeux"), GpBelfort.getVtx("Eloie")          ,dbExploit.section_getData("Verdoyeux", "Eloie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Eloie"), GpBelfort.getVtx("Route de Sermamagny"),dbExploit.section_getData("Eloie", "Route de Sermamagny")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Route de Sermamagny"), GpBelfort.getVtx("Rosemontoise"),dbExploit.section_getData("Route de Sermamagny", "Rosemontoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rosemontoise"), GpBelfort.getVtx("Aubépines")   ,dbExploit.section_getData("Rosemontoise", "Aubépines")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Aubépines"), GpBelfort.getVtx("Mermoz")         ,dbExploit.section_getData("Aubépines", "Mermoz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mermoz"), GpBelfort.getVtx("Prés d'Aumont")     ,dbExploit.section_getData("Mermoz", "Prés d'Aumont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Prés d'Aumont"), GpBelfort.getVtx("Beurrerie")  ,dbExploit.section_getData("Prés d'Aumont", "Beurrerie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Beurrerie"), GpBelfort.getVtx("Nallet")         ,dbExploit.section_getData("Beurrerie", "Nallet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Nallet"), GpBelfort.getVtx("Turenne")           ,dbExploit.section_getData("Nallet", "Turenne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Turenne"), GpBelfort.getVtx("Savoureuse")       ,dbExploit.section_getData("Turenne", "Savoureuse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Savoureuse"), GpBelfort.getVtx("Paquis")        ,dbExploit.section_getData("Savoureuse", "Paquis")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paquis"), GpBelfort.getVtx("Pont Blanc")        ,dbExploit.section_getData("Paquis", "Pont Blanc")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Blanc"), GpBelfort.getVtx("Marchegay")     ,dbExploit.section_getData("Pont Blanc", "Marchegay")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marchegay"), GpBelfort.getVtx("Martinet")       ,dbExploit.section_getData("Marchegay", "Martinet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Martinet"), GpBelfort.getVtx("Briand")          ,dbExploit.section_getData("Martinet", "Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Champ de Mars")     ,dbExploit.section_getData("Briand", "Champ de Mars")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Champ de Mars"), GpBelfort.getVtx("Les Forges") ,dbExploit.section_getData("Champ de Mars", "Les Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Forges"), GpBelfort.getVtx("Marseille")     ,dbExploit.section_getData("Les Forges", "Marseille")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marseille"), GpBelfort.getVtx("Clemenceau")     ,dbExploit.section_getData("Marseille", "Clemenceau")))
        
        
        
        #EightLine - BrownLineWest
            #1re Armée -> Ballinamuck
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1re Armée"), GpBelfort.getVtx("Paul Bert")      ,dbExploit.section_getData("1re Armée", "Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("Schweitzer")     ,dbExploit.section_getData("Paul Bert", "Schweitzer")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schweitzer"), GpBelfort.getVtx("Cravanche Centre")  ,dbExploit.section_getData("Schweitzer", "Cravanche Centre")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanche Centre"), GpBelfort.getVtx("Cravanchoise"),dbExploit.section_getData("Cravanche Centre", "Cravanchoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanchoise"), GpBelfort.getVtx("Haut des Près")   ,dbExploit.section_getData("Cravanchoise", "Haut des Près")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Haut des Près"), GpBelfort.getVtx("La Forêt")       ,dbExploit.section_getData("Haut des Près", "La Forêt")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Forêt"), GpBelfort.getVtx("Bas du Village")      ,dbExploit.section_getData("La Forêt", "Bas du Village")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bas du Village"), GpBelfort.getVtx("Frezard")       ,dbExploit.section_getData("Bas du Village", "Frezard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Frezard"), GpBelfort.getVtx("Ballinamuck")          ,dbExploit.section_getData("Frezard", "Ballinamuck")))
            #Ballinamuck -> 1re Armée
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballinamuck"), GpBelfort.getVtx("Frezard")          ,dbExploit.section_getData("Ballinamuck", "Frezard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Frezard"), GpBelfort.getVtx("Bas du Village")       ,dbExploit.section_getData("Frezard", "Bas du Village")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bas du Village"), GpBelfort.getVtx("La Forêt")      ,dbExploit.section_getData("Bas du Village", "La Forêt")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Forêt"), GpBelfort.getVtx("Haut des Près")       ,dbExploit.section_getData("La Forêt", "Haut des Près")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Haut des Près"), GpBelfort.getVtx("Cravanchoise")   ,dbExploit.section_getData("Haut des Près", "Cravanchoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanchoise"), GpBelfort.getVtx("Cravanche Centre"),dbExploit.section_getData("Cravanchoise", "Cravanche Centre")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanche Centre"), GpBelfort.getVtx("Schweitzer")  ,dbExploit.section_getData("Cravanche Centre", "Schweitzer")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schweitzer"), GpBelfort.getVtx("Paul Bert")         ,dbExploit.section_getData("Schweitzer", "Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("1re Armée")          ,dbExploit.section_getData("Paul Bert", "1re Armée")))
            #La Poste -> Guidon
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Poste"), GpBelfort.getVtx("Pins")                ,dbExploit.section_getData("La Poste", "Pins")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pins"), GpBelfort.getVtx("Terrasses")               ,dbExploit.section_getData("Pins", "Terrasses")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Terrasses"), GpBelfort.getVtx("Guidon")             ,dbExploit.section_getData("Terrasses", "Guidon")))
            #Guidon -> La Poste
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Guidon"), GpBelfort.getVtx("Terrasses")             ,dbExploit.section_getData("Guidon", "Terrasses")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Terrasses"), GpBelfort.getVtx("Pins")               ,dbExploit.section_getData("Terrasses", "Pins")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pins"), GpBelfort.getVtx("La Poste")                ,dbExploit.section_getData("Pins", "La Poste")))
        
        
        
        #NinthLine - BrownLineEst
        '''
            #République -> Miotte
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("République"), GpBelfort.getVtx("Atria")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Atria"), GpBelfort.getVtx("Miotte")))
            #Miotte -> Miotte
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Miotte"), GpBelfort.getVtx("Clinique")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clinique"), GpBelfort.getVtx("Haute Miotte")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Haute Miotte"), GpBelfort.getVtx("Deshaie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Deshaie"), GpBelfort.getVtx("Picard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Picard"), GpBelfort.getVtx("As de Trèfle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("As de Trèfle"), GpBelfort.getVtx("Miotte")))
            #République -> Miotte
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Miotte"), GpBelfort.getVtx("Atria")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Atria"), GpBelfort.getVtx("République")))
        '''
        
        
        
        
        #####################################################
        #
        #    CommonLines - CityCenter
        #
        #####################################################
        
            #Valdoie area
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Blumberg"), GpBelfort.getVtx("Mairie")                  ,dbExploit.section_getData("Blumberg", "Mairie")))
            #Est area (Ballinamuck -> La Poste)
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballinamuck"), GpBelfort.getVtx("Chemin de la ferme")   ,dbExploit.section_getData("Ballinamuck", "Chemin de la ferme")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chemin de la ferme"), GpBelfort.getVtx("De Gaulle")     ,dbExploit.section_getData("Chemin de la ferme", "De Gaulle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("De Gaulle"), GpBelfort.getVtx("Essert")                 ,dbExploit.section_getData("De Gaulle", "Essert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Essert"), GpBelfort.getVtx("La Poste")                  ,dbExploit.section_getData("Essert", "La Poste")))
            #Est area (La Poste -> Ballinamuck)
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Poste"), GpBelfort.getVtx("Essert")                  ,dbExploit.section_getData("La Poste", "Essert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Essert"), GpBelfort.getVtx("De Gaulle")                 ,dbExploit.section_getData("Essert", "De Gaulle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("De Gaulle"), GpBelfort.getVtx("Chemin de la ferme")     ,dbExploit.section_getData("De Gaulle", "Chemin de la ferme")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chemin de la ferme"), GpBelfort.getVtx("Ballinamuck")   ,dbExploit.section_getData("Chemin de la ferme", "Ballinamuck")))
            #GreenLine/PurlpleLine
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Guidon"), GpBelfort.getVtx("Follereau")                 ,dbExploit.section_getData("Guidon", "Follereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Follereau"), GpBelfort.getVtx("Dubail")                 ,dbExploit.section_getData("Follereau", "Dubail")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Dubail"), GpBelfort.getVtx("Hatry")                     ,dbExploit.section_getData("Dubail", "Hatry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hatry"), GpBelfort.getVtx("4 As")                       ,dbExploit.section_getData("Hatry", "4 As")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("4 As"), GpBelfort.getVtx("Strotz")                      ,dbExploit.section_getData("4 As", "Strotz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strotz"), GpBelfort.getVtx("Rabin")                     ,dbExploit.section_getData("Strotz", "Rabin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Clemenceau")                 ,dbExploit.section_getData("Rabin", "Clemenceau")))
            #PurlpleLine/GreenLine
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("Rabin")                 ,dbExploit.section_getData("Clemenceau", "Rabin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Strotz")                     ,dbExploit.section_getData("Rabin", "Strotz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strotz"), GpBelfort.getVtx("4 As")                      ,dbExploit.section_getData("Strotz", "4 As")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("4 As"), GpBelfort.getVtx("Hatry")                       ,dbExploit.section_getData("4 As", "Hatry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hatry"), GpBelfort.getVtx("Dubail")                     ,dbExploit.section_getData("Hatry", "Dubail")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Dubail"), GpBelfort.getVtx("Follereau")                 ,dbExploit.section_getData("Dubail", "Follereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Follereau"), GpBelfort.getVtx("Guidon")                 ,dbExploit.section_getData("Follereau", "Guidon")))
            #Clemenceau/Gare        
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("République")            ,dbExploit.section_getData("Clemenceau", "République")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("République"), GpBelfort.getVtx("Foch")                  ,dbExploit.section_getData("République", "Foch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Foch"), GpBelfort.getVtx("Schwob")                      ,dbExploit.section_getData("Foch", "Schwob")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schwob"), GpBelfort.getVtx("Denfert Rochereau")         ,dbExploit.section_getData("Schwob", "Denfert Rochereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Denfert Rochereau"), GpBelfort.getVtx("Gare")           ,dbExploit.section_getData("Denfert Rochereau", "Gare")))
            #Gare/Clemenceau
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare"), GpBelfort.getVtx("Denfert Rochereau")           ,dbExploit.section_getData("Gare", "Denfert Rochereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Denfert Rochereau"), GpBelfort.getVtx("Schwob")         ,dbExploit.section_getData("Denfert Rochereau", "Schwob")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schwob"), GpBelfort.getVtx("Foch")                      ,dbExploit.section_getData("Schwob", "Foch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Foch"), GpBelfort.getVtx("République")                  ,dbExploit.section_getData("Foch", "République")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("République"), GpBelfort.getVtx("Clemenceau")            ,dbExploit.section_getData("République", "Clemenceau")))
            #Gare/Le Nôtre
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare"), GpBelfort.getVtx("Fg de Lyon")                  ,dbExploit.section_getData("Gare", "Fg de Lyon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Fg de Lyon"), GpBelfort.getVtx("Madrid")                ,dbExploit.section_getData("Fg de Lyon", "Madrid")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid"), GpBelfort.getVtx("Blum")                      ,dbExploit.section_getData("Madrid", "Blum")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Blum"), GpBelfort.getVtx("Le Nôtre")                    ,dbExploit.section_getData("Blum", "Le Nôtre")))
            #Le Nôtre/Gare
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Le Nôtre"), GpBelfort.getVtx("Blum")                    ,dbExploit.section_getData("Le Nôtre", "Blum")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Blum"), GpBelfort.getVtx("Madrid")                      ,dbExploit.section_getData("Blum", "Madrid")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid"), GpBelfort.getVtx("Fg de Lyon")                ,dbExploit.section_getData("Madrid", "Fg de Lyon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Fg de Lyon"), GpBelfort.getVtx("Gare")                  ,dbExploit.section_getData("Fg de Lyon", "Gare")))
            #Gare/Multiplexe
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare"), GpBelfort.getVtx("Sernam")                      ,dbExploit.section_getData("Gare", "Sernam")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sernam"), GpBelfort.getVtx("Colbert")                   ,dbExploit.section_getData("Sernam", "Colbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colbert"), GpBelfort.getVtx("Multiplexe")               ,dbExploit.section_getData("Colbert", "Multiplexe")))
            #Multiplexe/Gare
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Multiplexe"), GpBelfort.getVtx("Colbert")               ,dbExploit.section_getData("Multiplexe", "Colbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colbert"), GpBelfort.getVtx("Sernam")                   ,dbExploit.section_getData("Colbert", "Sernam")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sernam"), GpBelfort.getVtx("Gare")                      ,dbExploit.section_getData("Sernam", "Gare")))
            #interLineConnexion
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid"), GpBelfort.getVtx("Dubail")                    ,dbExploit.section_getData("Madrid", "Dubail")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Dubail"), GpBelfort.getVtx("Madrid")                    ,dbExploit.section_getData("Dubail", "Madrid")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Savoureuse"), GpBelfort.getVtx("Mairie")                ,dbExploit.section_getData("Savoureuse", "Mairie")))
        
        #Close db access
        dbExploit.db_close()
        
        #Instantiate the adjacency matrix
        CommonKnowledge.adjMtxGraph = MtxGraph(len(GpBelfort.vtxList))
        
        #Insert vertices in the adjacency matrix
        for vtx in GpBelfort.vtxList:
            CommonKnowledge.adjMtxGraph.insert_vtx(vtx)
            
        #Insert edges in the adjacency matrix
        for edg in GpBelfort.edgList:
            CommonKnowledge.adjMtxGraph.insert_edg_EDGE(edg)
            
        #DEBUG
        #Display the adjacency matrix for check
        if(DEBUG_MODE):
            for elmt in CommonKnowledge.adjMtxGraph.get_adjMtx():
                print("{}".format(elmt))
                
        #Set the initial vertex of each ants
        #&& initialize common Knowledge
        #CommonKnowledge.comnKldg_init(GpBelfort.getVtx(warehouse_p))
        
    @staticmethod
    def getVtx(vtxId_p):
        for vtx in GpBelfort.vtxList:
            if vtx.get_ID() == vtxId_p:
                return vtx
        assert False, "element: **{}**,do not exist in the list".format(vtxId_p)
        
        
if DBDEBUG:
    i=0
    dbExploit.init_connection()
    GpBelfort.create()
    #for vtx in GpBelfort.vtxList:
    #    print("idx: {}, value: {}".format(i,vtx.get_ID()))
    #    File.fileWrite("VerticesList.txt", "idx: {}, value: {}".format(i,vtx.get_ID()), "/media/Stock/Workspaces/Py_WS/Ants Powered Auto-routing system/src/Logs/")
    #    i = i+1
    #print(len(GpBelfort.vtxList))
