import cmath
import numpy as np
import pandas as pd
import random
from patternstorageB import listDataset, percentDiff
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2
from matplotlib import style
import csv
from math import sqrt
from dateutil import parser
from datetime import datetime
import glob
from DatasetClass import Dataset, DT, DT0, FINALATTRIBUTEDIR
from InstanceClass import Instance
from QueueClass import Queue


all  = []


result = np.loadtxt(listDataset[0].getPattern0(), skiprows=0, delimiter = ',', dtype=DT0 )

randomIndexList = []
for i in range(0,200):
    randomIndexList.append(random.randint(0,len(result)))
all.append(randomIndexList)
all.append(" ")
for randomIndex in randomIndexList:
    item = []
    futureData = []
    currentData = []
    matchedResults = []
    futureDataPredicted = []

    for i in DT0.names:
        if (i =='datetime') or (i =='percentile') or (i =='quartile') :
            #print(result[randomIndex][i])
            continue
        elif (i =='5MAfuturepercent') or (i =='15MAfuturepercent') or (i =='30MAfuturepercent') or (i =='60MAfuturepercent') or (i =='120MAfuturepercent'):
            futureData.append(result[randomIndex][i])
        elif (i =='colour') or (i =='candletype') or (i =='5diffpercent') or (i =='15diffpercent') or (i =='30diffpercent') or (i =='60diffpercent') or (i =='120diffpercent') or (i =='fivedayrsi') or (i =='twentydayrsi') or (i =='fiftydayrsi') or (i =='fibonaccipercent'):
            currentData.append(result[randomIndex][i])


    attributePercentDiff = DT0.names[-9:]
    for j in result:
        if j == result[randomIndex]:
            continue
        score = 0
        if j['colour'] == result[randomIndex]['colour']:
            score +=1
        if j['candletype'] == result[randomIndex]['candletype']:
            score +=1
        for attributeName in attributePercentDiff:
            x = j[attributeName]
            y = result[randomIndex][attributeName]
            z = percentDiff(x,y)
            if (z<10) and (z>-10):
                score +=1
        if score>6:
            matchedResults.append(j)


    fiveFutureTotal = 0
    fifteenFutureTotal = 0
    thirtyFutureTotal = 0
    sixtyFutureTotal = 0
    hundredtwentyFutureTotal = 0
    for k in matchedResults:
        #print("yeaoup")
        fiveFutureTotal +=k['5MAfuturepercent']
        fifteenFutureTotal +=k['15MAfuturepercent']
        thirtyFutureTotal +=k['5MAfuturepercent']
        sixtyFutureTotal +=k['60MAfuturepercent']
        hundredtwentyFutureTotal+=k['120MAfuturepercent']


    if len(matchedResults) <3:
        futureDataPredicted.append(0)
        futureDataPredicted.append(0)
        futureDataPredicted.append(0)
        futureDataPredicted.append(0)
        futureDataPredicted.append(0)
    else:
        futureDataPredicted.append(fiveFutureTotal/len(matchedResults))
        futureDataPredicted.append(fifteenFutureTotal/len(matchedResults))
        futureDataPredicted.append(thirtyFutureTotal/len(matchedResults))
        futureDataPredicted.append(sixtyFutureTotal/len(matchedResults))
        futureDataPredicted.append(hundredtwentyFutureTotal/len(matchedResults))


    for l in futureData:
        item.append(l)
    for m in futureDataPredicted:
        item.append(m)
    all.append(item)


file0 = listDataset[0].getPrediction0()
with open(file0, 'w') as csvoutput:
     writer = csv.writer(csvoutput, lineterminator='\n')
     writer.writerows(all)
