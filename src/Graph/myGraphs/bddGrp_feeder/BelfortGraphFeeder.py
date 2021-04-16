'''
Created on 14 avr. 2021

@author: promet
'''

import pymongo
import chardet
import csv



#constant port for db connection
DBPORT = 27017

#connection to MOngoDB
client = pymongo.MongoClient('localhost', DBPORT)

#target the working data base
myDb = client.GraphBelfort

#target the working collection
fstCollec = myDb.Optimo_meanDay
 
        
####################################################
#
#  Extract data of CSV file and push it on mongoDB
#
####################################################

db_csv = '/media/Stock/Projets/Suratram/Ressources/Traces_WS/GoogleEarth/lineSynth_data/db_traces.csv'

#detect what the character encoding is
with open(db_csv, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
#print(result)


#read the csv file
with open(db_csv, 'r', encoding= result["encoding"]) as csvfile:
    csvRd = csv.reader(csvfile, delimiter=';')
    
    #slice csv row
    for row in csvRd:
        # print(row)
        # print(row[0])
        # print(row[1])
        # print(float(row[2].replace(',','.')))
        # print(float(row[3].replace(',','.')))
        # print(float(row[4].replace(',','.')))
        # print(row[5])
        # db_entry = "busStop1: {}, busStop2: {}, nrj: {}, km: {}, min: {}, line_nbr: {}".format(row[0], row[1], row[2], row[3], row[4], row[5])
        # print(db_entry)
        

        #Define section classification
        entry = {"busStop1": row[0],
                   "busStop2": row[1],
                    "NRJ_Wh": float(row[2].replace(',','.')),
                    "Distance_km": float(row[3].replace(',','.')),
                    "time_min": float(row[4].replace(',','.')),
                    "line_nbr": row[5]
                    }
                    
        fstCollec.insert_one(entry)
        
        # for j in fstCollec.find():
            # print(j)

        