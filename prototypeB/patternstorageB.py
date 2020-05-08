import cmath
import numpy as np
import pandas as pd
import random
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


#sentdex
def percentDiff(currentInstanceAverage, futureInstanceAverage):
    try:
        x = (((futureInstanceAverage-currentInstanceAverage)/abs(currentInstanceAverage))*100)
        if x == 0.0:
            return 0.0000000001
        else:
            return x
    except:
        return 0.0000000001

txtfiles = []
for file in glob.glob(FINALATTRIBUTEDIR):
    txtfiles.append(file)

listDataset = []
for i in txtfiles:
    D = Dataset(i)
    listDataset.append(D)

# for proc5 in listDataset:
result = np.loadtxt(listDataset[0].getDir(), skiprows=0, delimiter = ',', dtype=DT )

olddate = result[0]['datetime']
olddate = datetime.strptime(olddate, '%Y-%m-%d %H:%M:%S')


all = []
for i in result:
    newdate = i['datetime']
    newdate = datetime.strptime(newdate, '%Y-%m-%d %H:%M:%S')
    if (olddate.date()!=newdate.date() or (i==result[-1])):
        #print(olddate.date())
        olddate = newdate
    item = []
    item.append(i['datetime'])
    item.append(i['close'])

    fiveFuture = percentDiff(i['close'],i['5tickaveragefuture'])
    fifteenFuture = percentDiff(i['close'],i['15tickaveragefuture'])
    thirtyFuture = percentDiff(i['close'],i['30tickaveragefuture'])
    sixtyFuture = percentDiff(i['close'],i['60tickaveragefuture'])
    hundredtwentyFuture = percentDiff(i['close'],i['120tickaveragefuture'])
    item.append(fiveFuture)
    item.append(fifteenFuture)
    item.append(thirtyFuture)
    item.append(sixtyFuture)
    item.append(hundredtwentyFuture)

    item.append(i['percentile'])
    item.append(i['quartile'])
    item.append(i['colour'])
    item.append(i['candletype'])

    fiveDiff = percentDiff(i['close'],i['5tickaverage'])
    fifteenDiff = percentDiff(i['close'],i['15tickaverage'])
    thirtyDiff = percentDiff(i['close'],i['30tickaverage'])
    sixtyDiff = percentDiff(i['close'],i['60tickaverage'])
    hundredtwentyDiff = percentDiff(i['close'],i['120tickaverage'])

    item.append(fiveDiff)
    item.append(fifteenDiff)
    item.append(thirtyDiff)
    item.append(sixtyDiff)
    item.append(hundredtwentyDiff)

    item.append(i['fivedayrsi'])
    item.append(i['twentydayrsi'])
    item.append(i['fiftydayrsi'])
    item.append(i['fibonaccipercent'])


    all.append(item)

file0 = listDataset[0].getPattern0()
with open(file0, 'w') as csvoutput:
     writer = csv.writer(csvoutput, lineterminator='\n')
     writer.writerows(all)






# 
# result = np.loadtxt(listDataset[0].getPattern0(), skiprows=0, delimiter = ',', dtype=DT0 )
#
#
# randomIndexList = []
# # for i in range(0,200):
# #     randomIndexList.append(random.randint(0,len(result)))
# randomIndexList.append(1000)
# for randomIndex in randomIndexList:
#
#
#     futureData = []
#     currentData = []
#     matchedResults = []
#     futureDataPredicted = []
#
#     for i in DT0.names:
#         if (i =='datetime') or (i =='percentile') or (i =='quartile') :
#             #print(result[randomIndex][i])
#             continue
#         elif (i =='5MAfuturepercent') or (i =='15MAfuturepercent') or (i =='30MAfuturepercent') or (i =='60MAfuturepercent') or (i =='120MAfuturepercent'):
#             futureData.append(result[randomIndex][i])
#         elif (i =='colour') or (i =='candletype') or (i =='5diffpercent') or (i =='15diffpercent') or (i =='30diffpercent') or (i =='60diffpercent') or (i =='120diffpercent') or (i =='fivedayrsi') or (i =='twentydayrsi') or (i =='fiftydayrsi') or (i =='fibonaccipercent'):
#             currentData.append(result[randomIndex][i])
#
#
#     attributePercentDiff = DT0.names[-9:]
#     for j in result:
#         if j == result[randomIndex]:
#             continue
#         score = 0
#         if j['colour'] == result[randomIndex]['colour']:
#             score +=1
#         if j['candletype'] == result[randomIndex]['candletype']:
#             score +=1
#         for attributeName in attributePercentDiff:
#             x = j[attributeName]
#             y = result[randomIndex][attributeName]
#             z = percentDiff(x,y)
#             if (z<10) and (z>-10):
#                 score +=1
#         if score>6:
#             matchedResults.append(i)
#
#
#     fiveFutureTotal = 0
#     fifteenFutureTotal = 0
#     thirtyFutureTotal = 0
#     sixtyFutureTotal = 0
#     hundredtwentyFutureTotal = 0
#     for k in matchedResults:
#         fiveFutureTotal +=k['5MAfuturepercent']
#         fifteenFutureTotal +=k['15MAfuturepercent']
#         thirtyFutureTotal +=k['5MAfuturepercent']
#         sixtyFutureTotal +=k['60MAfuturepercent']
#         hundredtwentyFutureTotal+=i['120MAfuturepercent']
#         print(k['5MAfuturepercent'])
#
#     if len(matchedResults) == 0:
#         futureDataPredicted.append(result[randomIndex]['close'])
#         futureDataPredicted.append(result[randomIndex]['close'])
#         futureDataPredicted.append(result[randomIndex]['close'])
#         futureDataPredicted.append(result[randomIndex]['close'])
#         futureDataPredicted.append(result[randomIndex]['close'])
#     else:
#         futureDataPredicted.append(fiveFutureTotal/len(matchedResults))
#         futureDataPredicted.append(fifteenFutureTotal/len(matchedResults))
#         futureDataPredicted.append(thirtyFutureTotal/len(matchedResults))
#         futureDataPredicted.append(sixtyFutureTotal/len(matchedResults))
#         futureDataPredicted.append(hundredtwentyFutureTotal/len(matchedResults))
#
#
#     print("future data ", futureData)
#     print("future data prediction ", futureDataPredicted)
