'''
Created on 31 mai 2021

@author: promet
'''
from numpy import empty
from random import *
import enum
from Simulator.DEBUG import DEBUG

class PackgListGen:
    
    LS_weight = {1:0.100, 2:0.250, 3:0.500}
    PS_weight = {1:0.250, 2:0.500, 3:1, 4:1.5, 5:2, 6:3, 7:4, 8:5, 9:6, 10:7, 11:8, 12:9, 13:10, 14:11, 15:12}
    SP_weight = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:15, 12:20, 13:25, 14:30}
    
    LS_volume = 0.0018975
    PS_volume = 0.03978
    SP_volume = 0.432
    
    @staticmethod
    def run():
        
        pgList = []

        #generate random value to determine the number of package
        rdPackNbr = randint(1, 6)
        
        for i in range(0, rdPackNbr):
            pgList.append(PackgListGen.genPackage())
            
        if True:
            for elm in pgList:
                print("Package Type: {}".format(elm.type))
                print("Package Volume: {}".format(elm.volume))
                print("Package Weight: {}".format(elm.weight))
                print("################")
            
        return pgList
    
    @staticmethod
    def genPackage():
        """
        Generate package Type, Volume and weight according to associate probability
        """
        
        #generate value to determine package type
        rdVal = randint(0, 100)
        
        #standard Letter
        if rdVal >= 0 and rdVal <= 50:
            
            #select package type according to random value
            pgType = PackageType.LetterStandard
            
            #define Volume according to given proba.
            pgVol = PackgListGen.LS_volume
            
            #define Weight according to given proba.
            rdWei = randint(1, 3)
            pgWght = PackgListGen.LS_weight.get(rdWei)
            
            #return new create package
            return Package(pgType, pgVol, pgWght)
            
        #standard package
        if rdVal >= 51 and rdVal <= 85:
            
            #select package type according to random value
            pgType = PackageType.PackageStandard
            
            #define Volume according to given proba.
            pgVol = PackgListGen.PS_volume
            
            #define Weight according to given proba.
            rdWei = randint(1, 15)
            pgWght = PackgListGen.PS_weight.get(rdWei)
            
            #return new create package
            return Package(pgType, pgVol, pgWght)
        
        #standard Oversize package
        if rdVal >= 86 and rdVal <= 100:
            
            #select package type according to random value
            pgType = PackageType.SurdPackgStandard
            
            #define Volume according to given proba.
            pgVol = PackgListGen.SP_volume
            
            #define Weight according to given proba.
            rdWei = randint(1, 14)
            pgWght = PackgListGen.SP_weight.get(rdWei)
            
            #return new create package
            return Package(pgType, pgVol, pgWght)
    
    
class Package:
    """
    class package
    """
    
    def __init__(self, pgType_p = empty, volume_p = 0.0, weight_p = 0.0):
        self.type = pgType_p
        self.volume = volume_p
        self.weight = weight_p
        
        
        
class PackageType(enum.Enum):
    """
    Enum class to have a standart package type available
    """
    
    LetterStandard = 1
    PackageStandard = 2
    SurdPackgStandard = 3
    
    
    
#####################################
#debug part
for i in range(0, 100):
    PackgListGen.run()

