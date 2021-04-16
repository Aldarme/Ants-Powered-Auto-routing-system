'''
Created on 21 mai 2020

@author: promet
'''

from Graph.Vertex import Vertex
from Graph.Edge import Edge 
from Utilities.File import File
from Algorithms.VRP.ACO.CommonKnowledge import CommonKnowledge
from Graph.MtxGraph import MtxGraph


DEBUG = False

class GpBelfort:
    
    vtxList = []
    edgList = []
    
    @staticmethod
    def create( ):
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
        GpBelfort.vtxList.append(Vertex("Miotte"))
        GpBelfort.vtxList.append(Vertex("Atria"))
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
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Douce"), GpBelfort.getVtx("Signoret")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Signoret"), GpBelfort.getVtx("Schuman")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schuman"), GpBelfort.getVtx("Bruxelles")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bruxelles"), GpBelfort.getVtx("Madrid")))
            #Madrid -> RESIDENCES
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid"), GpBelfort.getVtx("Bruxelles")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bruxelles"), GpBelfort.getVtx("Schuman")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schuman"), GpBelfort.getVtx("Signoret")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Signoret"), GpBelfort.getVtx("La Douce")))
            #Clemenceau -> VALDOIE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("Jaurès Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jaurès Hôpital"), GpBelfort.getVtx("Strasbourg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strasbourg"), GpBelfort.getVtx("Colmar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colmar"), GpBelfort.getVtx("Roseraie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Roseraie"), GpBelfort.getVtx("Marché Vosges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marché Vosges"), GpBelfort.getVtx("1re Armée")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1re Armée"), GpBelfort.getVtx("Salbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Salbert"), GpBelfort.getVtx("Rubans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rubans"), GpBelfort.getVtx("Blumberg")))
            #VALDOIE -> Clemenceau
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mairie"), GpBelfort.getVtx("Rubans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rubans"), GpBelfort.getVtx("Salbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Salbert"), GpBelfort.getVtx("1re Armée")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1re Armée"), GpBelfort.getVtx("Marché Vosges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marché Vosges"), GpBelfort.getVtx("Roseraie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Roseraie"), GpBelfort.getVtx("Colmar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colmar"), GpBelfort.getVtx("Strasbourg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strasbourg"), GpBelfort.getVtx("Jaurès Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jaurès Hôpital"), GpBelfort.getVtx("Clemenceau")))
        
        
        
        #SecondLine - OrangeLine
            #JUSTICE ->  Multiplexe
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hauts de Belfort"), GpBelfort.getVtx("Camus")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Camus"), GpBelfort.getVtx("CFA")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("CFA"), GpBelfort.getVtx("Laurencie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurencie"), GpBelfort.getVtx("Cimetière Militaire")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cimetière Militaire"), GpBelfort.getVtx("Parant")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parant"), GpBelfort.getVtx("Sellier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sellier"), GpBelfort.getVtx("Altkirch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Altkirch"), GpBelfort.getVtx("Les Perches")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Perches"), GpBelfort.getVtx("Multiplexe")))
            #Multiplexe -> JUSTICE  
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Multiplexe"), GpBelfort.getVtx("Les Perches")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Perches"), GpBelfort.getVtx("Altkirch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Altkirch"), GpBelfort.getVtx("Sellier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sellier"), GpBelfort.getVtx("Parant")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parant"), GpBelfort.getVtx("Cimetière Militaire")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cimetière Militaire"), GpBelfort.getVtx("Laurencie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurencie"), GpBelfort.getVtx("CFA")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("CFA"), GpBelfort.getVtx("Bichat")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bichat"), GpBelfort.getVtx("Hauts de Belfort")))
            #BAVILLIERS -> Bavilliers
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Dame"), GpBelfort.getVtx("La Belle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Belle"), GpBelfort.getVtx("Bavilliers")))
            #Bavilliers -> BAVILLIERS
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bavilliers"), GpBelfort.getVtx("La Belle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Belle"), GpBelfort.getVtx("La Dame")))
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
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bavilliers"), GpBelfort.getVtx("Pont Canal")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Canal"), GpBelfort.getVtx("Mozart")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mozart"), GpBelfort.getVtx("Bonneff")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bonneff"), GpBelfort.getVtx("Le Nôtre")))
            #Le Nôtre -> Bavilliers 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Le Nôtre"), GpBelfort.getVtx("Bonneff")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bonneff"), GpBelfort.getVtx("Mozart")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mozart"), GpBelfort.getVtx("Pont Canal")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Canal"), GpBelfort.getVtx("Bavilliers")))
            #Rabin -> CRAVANCHE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Mieg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mieg"), GpBelfort.getVtx("Saget")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Saget"), GpBelfort.getVtx("Ste Thérèse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ste Thérèse"), GpBelfort.getVtx("Grand' Combe")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grand' Combe"), GpBelfort.getVtx("Laurent Thierry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurent Thierry"), GpBelfort.getVtx("Alstom Étang")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Alstom Étang"), GpBelfort.getVtx("Techn' Hom Cravanche")))
            #CRAVANCHE -> Rabin 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom Cravanche"), GpBelfort.getVtx("Alstom Étang")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Alstom Étang"), GpBelfort.getVtx("Laurent Thierry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Laurent Thierry"), GpBelfort.getVtx("Grand' Combe")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grand' Combe"), GpBelfort.getVtx("Ste Thérèse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ste Thérèse"), GpBelfort.getVtx("Saget")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Saget"), GpBelfort.getVtx("Mieg")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mieg"), GpBelfort.getVtx("Rabin")))
        
        
        
        #ThirdLine - BlueLine
            #VALDOIE -> Follereau
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mairie"), GpBelfort.getVtx("Méchelle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Méchelle"), GpBelfort.getVtx("Benoit Frachon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Benoit Frachon"), GpBelfort.getVtx("Techn' Hom 3")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 3"), GpBelfort.getVtx("Techn' Hom 2")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 2"), GpBelfort.getVtx("IUT")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("IUT"), GpBelfort.getVtx("Techn' Hom 1 UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 1 UTBM"), GpBelfort.getVtx("Follereau")))
            #Follereau -> VALDOIE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Follereau"), GpBelfort.getVtx("Techn' Hom 1 UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 1 UTBM"), GpBelfort.getVtx("IUT")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("IUT"), GpBelfort.getVtx("Techn' Hom 2")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 2"), GpBelfort.getVtx("Techn' Hom 3")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Techn' Hom 3"), GpBelfort.getVtx("Benoit Frachon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Benoit Frachon"), GpBelfort.getVtx("Méchelle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Méchelle"), GpBelfort.getVtx("Blumberg")))
            #Multiplexe -> OEufs Frais
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Multiplexe"), GpBelfort.getVtx("Varonne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Varonne"), GpBelfort.getVtx("Bosmont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bosmont"), GpBelfort.getVtx("Jacquot")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jacquot"), GpBelfort.getVtx("Éluard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Éluard"), GpBelfort.getVtx("Grottes")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grottes"), GpBelfort.getVtx("Andelnans Prés")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Andelnans Prés"), GpBelfort.getVtx("Port de Botans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Port de Botans"), GpBelfort.getVtx("OEufs Frais")))
            #OEufs Frais -> Multiplexe
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("OEufs Frais"), GpBelfort.getVtx("Port de Botans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Port de Botans"), GpBelfort.getVtx("Andelnans Prés")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Andelnans Prés"), GpBelfort.getVtx("Grottes")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Grottes"), GpBelfort.getVtx("Éluard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Éluard"), GpBelfort.getVtx("Jacquot")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Jacquot"), GpBelfort.getVtx("Bosmont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bosmont"), GpBelfort.getVtx("Varonne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Varonne"), GpBelfort.getVtx("Multiplexe")))   
            #OEufs Frais -> GARE TGV
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("OEufs Frais"), GpBelfort.getVtx("Sévenans UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sévenans UTBM"), GpBelfort.getVtx("Hôpital NFC")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital NFC"), GpBelfort.getVtx("Moval")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moval"), GpBelfort.getVtx("Rte de Meroux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Meroux"), GpBelfort.getVtx("Gare TGV")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare TGV"), GpBelfort.getVtx("1er RA")))   
            #GARE TGV -> OEufs Frais
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1er RA"), GpBelfort.getVtx("Gare TGV")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare TGV"), GpBelfort.getVtx("Rte de Meroux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Meroux"), GpBelfort.getVtx("Moval")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moval"), GpBelfort.getVtx("Hôpital NFC")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital NFC"), GpBelfort.getVtx("Sévenans UTBM")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sévenans UTBM"), GpBelfort.getVtx("OEufs Frais")))    
            #OEufs Frais -> CHATENOIS
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("OEufs Frais"), GpBelfort.getVtx("Rte de Bermont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Bermont"), GpBelfort.getVtx("Conforama")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Conforama"), GpBelfort.getVtx("Bascule")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bascule"), GpBelfort.getVtx("Trévenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Trévenans"), GpBelfort.getVtx("Rte de Vourvenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Vourvenans"), GpBelfort.getVtx("Châtenois Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois Forges"), GpBelfort.getVtx("Complexe Sportif")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Complexe Sportif"), GpBelfort.getVtx("Châtenois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois"), GpBelfort.getVtx("Géhant")))    
            #CHATENOIS -> OEufs Frais        
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Géhant"), GpBelfort.getVtx("Châtenois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois"), GpBelfort.getVtx("Complexe Sportif")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Complexe Sportif"), GpBelfort.getVtx("Châtenois Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Châtenois Forges"), GpBelfort.getVtx("Rte de Vourvenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Vourvenans"), GpBelfort.getVtx("Trévenans")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Trévenans"), GpBelfort.getVtx("Bascule")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bascule"), GpBelfort.getVtx("Conforama")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Conforama"), GpBelfort.getVtx("Rte de Bermont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rte de Bermont"), GpBelfort.getVtx("OEufs Frais")))
        
        
        
        #FourthLine - PurpleLine
            #FROIDEVAL -> Le Nôtre
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Berger"), GpBelfort.getVtx("L'assise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("L'assise"), GpBelfort.getVtx("St Antonin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("St Antonin"), GpBelfort.getVtx("Pierre Engel")))
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pierre Engel"), GpBelfort.getVtx("Marcel Braun")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marcel Braun"), GpBelfort.getVtx("Chênois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chênois"), GpBelfort.getVtx("Poincaré")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Poincaré"), GpBelfort.getVtx("Renan")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Renan"), GpBelfort.getVtx("Molière")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Molière"), GpBelfort.getVtx("Le Nôtre")))
            #Le Nôtre -> FROIDEVAL
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Le Nôtre"), GpBelfort.getVtx("Molière")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Molière"), GpBelfort.getVtx("Renan")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Renan"), GpBelfort.getVtx("Poincaré")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Poincaré"), GpBelfort.getVtx("Chênois")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chênois"), GpBelfort.getVtx("Marcel Braun")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marcel Braun"), GpBelfort.getVtx("Pierre Engel")))
        '''
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pierre Engel"), GpBelfort.getVtx("St Antonin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("St Antonin"), GpBelfort.getVtx("L'assise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("L'assise"), GpBelfort.getVtx("Berger")))
        '''
            #Rabin -> OFFEMONT
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital"), GpBelfort.getVtx("Mulhouse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mulhouse"), GpBelfort.getVtx("Bohn")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bohn"), GpBelfort.getVtx("Madagascar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madagascar"), GpBelfort.getVtx("Ferrette")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ferrette"), GpBelfort.getVtx("Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("Parmentier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parmentier"), GpBelfort.getVtx("Courbet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Courbet"), GpBelfort.getVtx("Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Centre Commercial")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Centre Commercial"), GpBelfort.getVtx("Romaine")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Romaine"), GpBelfort.getVtx("Ballon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballon"), GpBelfort.getVtx("Moulin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moulin"), GpBelfort.getVtx("Champs Cerisiers")))
            #OFFEMONT -> Rabin
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Champs Cerisiers"), GpBelfort.getVtx("Moulin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Moulin"), GpBelfort.getVtx("Ballon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballon"), GpBelfort.getVtx("Romaine")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Romaine"), GpBelfort.getVtx("Centre Commercial")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Centre Commercial"), GpBelfort.getVtx("Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Courbet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Courbet"), GpBelfort.getVtx("Parmentier")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Parmentier"), GpBelfort.getVtx("Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("Ferrette")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ferrette"), GpBelfort.getVtx("Madagascar")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madagascar"), GpBelfort.getVtx("Bohn")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bohn"), GpBelfort.getVtx("Mulhouse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mulhouse"), GpBelfort.getVtx("Hôpital")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hôpital"), GpBelfort.getVtx("Rabin")))
        
        
        
        #FifthLine - GreenLine
            #ESSERT -> Ballinamuck
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bois Joli"), GpBelfort.getVtx("Ballinamuck")))
            #Ballinamuck -> ESSERT 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballinamuck"), GpBelfort.getVtx("Bois Joli")))
            #La Poste -> Guidon
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Poste"), GpBelfort.getVtx("Carrières")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Carrières"), GpBelfort.getVtx("Gardey")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gardey"), GpBelfort.getVtx("Guidon")))
            #Guidon -> La Poste
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Guidon"), GpBelfort.getVtx("Gardey")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gardey"), GpBelfort.getVtx("Carrières")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Carrières"), GpBelfort.getVtx("La Poste")))
            #Clemenceau -> ELOIE
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("Marseille")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marseille"), GpBelfort.getVtx("Les Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Forges"), GpBelfort.getVtx("Champ de Mars")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Champ de Mars"), GpBelfort.getVtx("Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Martinet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Martinet"), GpBelfort.getVtx("Marchegay")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marchegay"), GpBelfort.getVtx("Pont Blanc")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Blanc"), GpBelfort.getVtx("Paquis")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paquis"), GpBelfort.getVtx("Savoureuse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Savoureuse"), GpBelfort.getVtx("Turenne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Turenne"), GpBelfort.getVtx("Nallet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Nallet"), GpBelfort.getVtx("Beurrerie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Beurrerie"), GpBelfort.getVtx("Prés d'Aumont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Prés d'Aumont"), GpBelfort.getVtx("Mermoz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mermoz"), GpBelfort.getVtx("Aubépines")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Aubépines"), GpBelfort.getVtx("Rosemontoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rosemontoise"), GpBelfort.getVtx("Route de Sermamagny")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Route de Sermamagny"), GpBelfort.getVtx("Eloie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Eloie"), GpBelfort.getVtx("Verdoyeux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Verdoyeux"), GpBelfort.getVtx("Chaume")))
            #ELOIE -> Clemenceau 
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chaume"), GpBelfort.getVtx("Verdoyeux")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Verdoyeux"), GpBelfort.getVtx("Eloie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Eloie"), GpBelfort.getVtx("Route de Sermamagny")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Route de Sermamagny"), GpBelfort.getVtx("Rosemontoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rosemontoise"), GpBelfort.getVtx("Aubépines")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Aubépines"), GpBelfort.getVtx("Mermoz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Mermoz"), GpBelfort.getVtx("Prés d'Aumont")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Prés d'Aumont"), GpBelfort.getVtx("Beurrerie")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Beurrerie"), GpBelfort.getVtx("Nallet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Nallet"), GpBelfort.getVtx("Turenne")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Turenne"), GpBelfort.getVtx("Savoureuse")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Savoureuse"), GpBelfort.getVtx("Paquis")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paquis"), GpBelfort.getVtx("Pont Blanc")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pont Blanc"), GpBelfort.getVtx("Marchegay")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marchegay"), GpBelfort.getVtx("Martinet")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Martinet"), GpBelfort.getVtx("Briand")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Briand"), GpBelfort.getVtx("Champ de Mars")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Champ de Mars"), GpBelfort.getVtx("Les Forges")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Les Forges"), GpBelfort.getVtx("Marseille")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Marseille"), GpBelfort.getVtx("Clemenceau")))
        
        
        
        #EightLine - BrownLineWest
            #1re Armée -> Ballinamuck
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("1re Armée"), GpBelfort.getVtx("Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("Schweitzer")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schweitzer"), GpBelfort.getVtx("Cravanche Centre")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanche Centre"), GpBelfort.getVtx("Cravanchoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanchoise"), GpBelfort.getVtx("Haut des Près")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Haut des Près"), GpBelfort.getVtx("La Forêt")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Forêt"), GpBelfort.getVtx("Bas du Village")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bas du Village"), GpBelfort.getVtx("Frezard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Frezard"), GpBelfort.getVtx("Ballinamuck")))
            #Ballinamuck -> 1re Armée
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballinamuck"), GpBelfort.getVtx("Frezard")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Frezard"), GpBelfort.getVtx("Bas du Village")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Bas du Village"), GpBelfort.getVtx("La Forêt")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Forêt"), GpBelfort.getVtx("Haut des Près")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Haut des Près"), GpBelfort.getVtx("Cravanchoise")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanchoise"), GpBelfort.getVtx("Cravanche Centre")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Cravanche Centre"), GpBelfort.getVtx("Schweitzer")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schweitzer"), GpBelfort.getVtx("Paul Bert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Paul Bert"), GpBelfort.getVtx("1re Armée")))
            #La Poste -> Guidon
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Poste"), GpBelfort.getVtx("Pins")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pins"), GpBelfort.getVtx("Terrasses")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Terrasses"), GpBelfort.getVtx("Guidon")))
            #Guidon -> La Poste
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Guidon"), GpBelfort.getVtx("Terrasses")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Terrasses"), GpBelfort.getVtx("Pins")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Pins"), GpBelfort.getVtx("La Poste")))
        
        
        
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
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Blumberg"), GpBelfort.getVtx("Mairie")))
            #Est area (Ballinamuck -> La Poste)
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Ballinamuck"), GpBelfort.getVtx("Chemin de la ferme")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chemin de la ferme"), GpBelfort.getVtx("De Gaulle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("De Gaulle"), GpBelfort.getVtx("Essert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Essert"), GpBelfort.getVtx("La Poste")))
            #Est area (La Poste -> Ballinamuck)
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("La Poste"), GpBelfort.getVtx("Essert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Essert"), GpBelfort.getVtx("De Gaulle")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("De Gaulle"), GpBelfort.getVtx("Chemin de la ferme")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Chemin de la ferme"), GpBelfort.getVtx("Ballinamuck")))
            #GreenLine/PurlpleLine
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Guidon"), GpBelfort.getVtx("Follereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Follereau"), GpBelfort.getVtx("Dubail")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Dubail"), GpBelfort.getVtx("Hatry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hatry"), GpBelfort.getVtx("4 As")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("4 As"), GpBelfort.getVtx("Strotz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strotz"), GpBelfort.getVtx("Rabin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Clemenceau")))
            #PurlpleLine/GreenLine
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("Rabin")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Rabin"), GpBelfort.getVtx("Strotz")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Strotz"), GpBelfort.getVtx("4 As")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("4 As"), GpBelfort.getVtx("Hatry")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Hatry"), GpBelfort.getVtx("Dubail")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Dubail"), GpBelfort.getVtx("Follereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Follereau"), GpBelfort.getVtx("Guidon")))
            #Clemenceau/Gare        
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Clemenceau"), GpBelfort.getVtx("République")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("République"), GpBelfort.getVtx("Foch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Foch"), GpBelfort.getVtx("Schwob")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schwob"), GpBelfort.getVtx("Denfert Rochereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Denfert Rochereau"), GpBelfort.getVtx("Gare")))
            #Gare/Clemenceau
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare"), GpBelfort.getVtx("Denfert Rochereau")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Denfert Rochereau"), GpBelfort.getVtx("Schwob")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Schwob"), GpBelfort.getVtx("Foch")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Foch"), GpBelfort.getVtx("République")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("République"), GpBelfort.getVtx("Clemenceau")))
            #Gare/Le Nôtre
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare"), GpBelfort.getVtx("Fg de Lyon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Fg de Lyon"), GpBelfort.getVtx("Madrid")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid"), GpBelfort.getVtx("Blum")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Blum"), GpBelfort.getVtx("Le Nôtre")))
            #Le Nôtre/Gare
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Le Nôtre"), GpBelfort.getVtx("Blum")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Blum"), GpBelfort.getVtx("Madrid")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid"), GpBelfort.getVtx("Fg de Lyon")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Fg de Lyon"), GpBelfort.getVtx("Gare")))
            #Gare/Multiplexe
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Gare"), GpBelfort.getVtx("Sernam")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sernan"), GpBelfort.getVtx("Colbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colbert"), GpBelfort.getVtx("Multiplexe")))
            #Multiplexe/Gare
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Multiplexe"), GpBelfort.getVtx("Colbert")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Colbert"), GpBelfort.getVtx("Sernan")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Sernan"), GpBelfort.getVtx("Gare")))
            #interLineConnexion
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Madrid"), GpBelfort.getVtx("Dubail")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Dubail"), GpBelfort.getVtx("Madrid")))
        GpBelfort.edgList.append(Edge(GpBelfort.getVtx("Savoureuse"), GpBelfort.getVtx("Mairie")))
        
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
        if(GpBelfort.DEBUG):
            for elmt in CommonKnowledge.adjMtxGraph.get_adjMtx():
                print("{}".format(elmt))
        
    @staticmethod
    def getVtx(vtxId_p):
        for vtx in GpBelfort.vtxList:
            if vtx.get_ID() == vtxId_p:
                return vtx
        assert False, "element: **{}**,do not exist in the list".format(vtxId_p)
        
        
if DEBUG == True:
    i=0
    GpBelfort.create()
    for vtx in GpBelfort.vtxList:
        print("idx: {}, value: {}".format(i,vtx.get_ID()))
        File.fileWrite("VerticesList.txt", "idx: {}, value: {}".format(i,vtx.get_ID()), "/media/Stock/Workspaces/Py_WS/Ants Powered Auto-routing system/src/Logs/")
        i = i+1
    print(len(GpBelfort.vtxList))
