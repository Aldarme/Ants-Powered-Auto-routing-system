"""
Created on 31 mai 2021

@author: promet
"""
import random

class DelivListGen:
    
    buStop = ["La Douce", "Signoret", "Schuman", "Bruxelles", "Jaurès Hôpital", "Strasbourg", "Colmar", "Roseraie", "Marché Vosges",
              "Salbert", "Rubans", "La Dame", "La Belle", "Bavilliers", "Pont Canal", "Mozart", "Bonneff", "Mieg", "Saget", "Ste Thérèse", "Grand' Combe",
              "Laurent Thierry", "Alstom Étang", "Techn' Hom Cravanche", "Les Perches", "Altkirch", "Sellier", "Parant",
              "Cimetière Militaire", "Laurencie", "CFA", "Bichat", "Hauts de Belfort", "Camus", "1er RA", "Gare TGV",
              "Rte de Meroux", "Moval", "Hôpital NFC", "Sévenans UTBM", "Géhant", "Châtenois", "Complexe Sportif",
              "Châtenois Forges", "Rte de Vourvenans", "Trévenans", "Bascule", "Conforama", "Rte de Bermont", "OEufs Frais",
              "Port de Botans", "Andelnans Prés", "Grottes", "Éluard", "Jacquot", "Bosmont", "Varonne","Techn' Hom 1 UTBM",
              "IUT", "Techn' Hom 2", "Techn' Hom 3", "Benoit Frachon", "Méchelle", "Pierre Engel", "Marcel Braun", "Chênois", "Poincaré", "Renan", "Molière", "Hôpital", "Mulhouse", "Bohn", "Madagascar",
              "Ferrette", "Parmentier", "Courbet", "Centre Commercial", "Romaine", "Ballon", "Moulin", "Champs Cerisiers", "Bois Joli",
              "Carrières", "Gardey", "Marseille", "Les Forges", "Champ de Mars", "Martinet", "Marchegay", "Pont Blanc", "Paquis",
              "Savoureuse", "Turenne", "Nallet", "Beurrerie", "Prés d'Aumont", "Mermoz", "Aubépines", "Rosemontoise", "Route de Sermamagny",
              "Eloie", "Verdoyeux", "Chaume", "Schweitzer", "Cravanche Centre", "Cravanchoise", "Haut des Près", "La Forêt", "Bas du Village",
              "Frezard", "Pins", "Terrasses", "Mairie", "Blumberg", "1re Armée", "Paul Bert", "Briand", "Clemenceau", "Rabin", "République", "Foch", "Schwob", "Denfert Rochereau",
              "Strotz", "4 As", "Hatry", "Dubail", "Follereau", "Guidon", "Madrid", "Blum", "Fg de Lyon", "Gare", "Sernam", "Colbert",
              "Multiplexe", "Le Nôtre", "La Poste", "Essert", "De Gaulle", "Chemin de la ferme", "Ballinamuck"
              ]
    
    debugList = ["Madrid", "Foch", "République", "Briand", "Mairie", "Follereau"]
    
    @staticmethod
    def run(delivPtsNbr_p = 1, warehouse_vertex_p=""):
        """
        Select wanted number of delivery point.
        maximum value = 
        """
        #work on local copy
        tmpList = DelivListGen.buStop.copy()
        
        #remove the deposit vertex to avoid Dijkstra to search on it and crash
        tmpList.remove(warehouse_vertex_p)
        
        finalList = []
        
        #get specific number of bus Stop, according to the parameter
        for i in range(0, delivPtsNbr_p):#len(tmpList)
            tmpString = random.choice(tmpList)
            finalList.append(tmpString)
            tmpList.remove(tmpString)
        
        return finalList
    
        
    print(len(buStop))     