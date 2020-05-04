import cmath
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2
from matplotlib import style
import csv
from math import sqrt
from dateutil import parser
from datetime import datetime
import glob
from DatasetClass import Dataset, BASEDIR, DT
from InstanceClass import Instance
from QueueClass import Queue
import time

#*********************************
txtfiles = []
for file in glob.glob(BASEDIR):
    txtfiles.append(file)

listDataset = []
for i in txtfiles:
    D = Dataset(i)
    listDataset.append(D)

for rawDataSet in listDataset:
    v = open(rawDataSet.csvDir)
    r = csv.reader(v)
    row0 = next(r)
    #print(row0)
    all = []
    for item in r:
        item.append("colour")
        item.append("candletype")
        item.append(0)#5tickmovingaverage
        item.append(0)#100tickmovingaverage
        item.append(0)#200tickmovingaverage
        item.append(0)#450tickmovingaverage
        item.append(0)#1000tickmovingaverage
        item.append(50)#rsi5
        item.append(50)#rsi20
        item.append(50)#rsi50
        item.append(0)#5daymovingaveragefuture
        item.append(0)#100tickmovingaveragefuture
        item.append(0)#200tickmovingaveragefuture
        item.append(0)#450tickmovingaveragefuture
        item.append(0)#1000tickmovingaveragefuture
        item.append(2)#percentile
        item.append(2)#quartile
        item.append(50)#fibonacci
        all.append(item)

    file0 = rawDataSet.getProcessed0()
    with open(file0, 'w') as csvoutput:
         writer = csv.writer(csvoutput, lineterminator='\n')
         writer.writerows(all)
#*********************************

#*********************************
for proc0 in listDataset:
    result = np.loadtxt(proc0.getProcessed0(), skiprows=1, delimiter = ',', dtype=DT )
    all = []
    for i in result:
        date = i['datetime']
        date = date[0:-13]
        date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
        i['datetime'] = date
        #print(i['datetime'].time())
        all.append(i)

    file1 = proc0.getProcessed1()
    with open(file1, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(all)
#*********************************

#*********************************
for proc1 in listDataset:
    result = np.loadtxt(proc1.getProcessed1(), skiprows=1, delimiter = ',', dtype=DT )
    all = []

    q2candle = Queue()#will be queing timeval
    for i in range(0,2):
        timeVal = Instance(10,10,10,10)
        q2candle.enqueue(timeVal)

    for i in result:
        #have to queue from here
        timeVal = Instance(i['open'], i['high'], i['low'], i['close'])
        q2candle.enqueue(timeVal)
        q2candle.dequeue()
        timeVal.setColour()
        colourVal = timeVal.getColour()
        i['colour'] = colourVal
        timeVal.setCandleType(q2candle)
        candletypeVal = timeVal.getCandleType()
        i['candletype'] = candletypeVal
        all.append(i)

    file2 = proc1.getProcessed2()
    with open(file2, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(all)
#*********************************

#*********************************
for proc2 in listDataset:
    result = np.loadtxt(proc2.getProcessed2(), skiprows=1, delimiter = ',', dtype=DT )
    all = []
    start = time.time()
    q5 = Queue()#15seconds
    q100 = Queue()#130seconds
    q200 = Queue()#5minutes
    q450 = Queue()#10minutes
    q1000 = Queue()#30minutes

    q5rsi = Queue()
    q20rsi=Queue()
    q50rsi = Queue()
    for i in range(0,5):
        q5rsi.enqueue(10)
    for i in range(0,20):
        q20rsi.enqueue(10)
    for i in range(0,50):
        q50rsi.enqueue(10)


    closeprev = 0
    for i in result:

        if q5.size() < 5:
            q5.enqueue(i['close'])
        else:
            q5.enqueue(i['close'])
            q5.dequeue()
        if q100.size() < 100:
            q100.enqueue(i['close'])
        else:
            q100.enqueue(i['close'])
            q100.dequeue()
        if q200.size() < 200:
            q200.enqueue(i['close'])
        else:
            q200.enqueue(i['close'])
            q200.dequeue()
        if q450.size() < 450:
            q450.enqueue(i['close'])
        else:
            q450.enqueue(i['close'])
            q450.dequeue()
        if q1000.size() < 1000:
            q1000.enqueue(i['close'])
        else:
            q1000.enqueue(i['close'])
            q1000.dequeue()

        x = np.where(result == i)
        currentIndex = x[0][0]

        average = q5.movingtickaverage()
        i['5tickaverage'] = average
        fivePrev = currentIndex-5
        if (fivePrev)>0:
            result[fivePrev]['5tickaveragefuture'] = average

        average = q100.movingtickaverage()
        i['100tickaverage'] = average
        hundredPrev = currentIndex-100
        if (hundredPrev)>0:
            result[hundredPrev]['100tickaveragefuture'] = average

        average = q200.movingtickaverage()
        i['200tickaverage'] = average
        twohundredprev = currentIndex-200
        if (twohundredprev)>0:
            result[twohundredprev]['200tickaveragefuture'] = average

        average = q450.movingtickaverage()
        i['450tickaverage'] = average
        fourfiftyprev = currentIndex-450
        if (fourfiftyprev)>0:
            result[fourfiftyprev]['450tickaveragefuture'] = average

        average = q1000.movingtickaverage()
        i['1000tickaverage'] = average
        thousandprev = currentIndex-1000
        if (thousandprev)>0:
            result[thousandprev]['1000tickaveragefuture'] = average





        diff = i['close']-closeprev
        closeprev =  i['close']
        q5rsi.enqueue(diff)
        q5rsi.dequeue()
        q20rsi.enqueue(diff)
        q20rsi.dequeue()
        q50rsi.enqueue(diff)
        q50rsi.dequeue()
        rsi5 = q5rsi.fivedayrsi()
        i['fivedayrsi'] = rsi5
        rsi20 = q20rsi.twentydayrsi()
        i['twentydayrsi'] = rsi20
        rsi50 = q50rsi.fiftydayrsi()
        i['fiftydayrsi'] = rsi50

        all.append(i)


    file3 = proc2.getProcessed3()
    with open(file3, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(all)
    end = time.time()
    print(end - start)
#*********************************

#*********************************
for proc3 in listDataset:
    result = np.loadtxt(proc3.getProcessed3(), skiprows=1, delimiter = ',', dtype=DT )
    all = []
    closingPriceList = []
    for i in result:
        closingPriceList.append(i['close'])
    numberOfTicks = len(closingPriceList)

    closingPriceListSorted = sorted(closingPriceList)
    minClosePrice = closingPriceListSorted[0]
    maxClosePrice = closingPriceListSorted[numberOfTicks-1]
    rangeClose = maxClosePrice-minClosePrice

    lowerQuartilePrice = (rangeClose/4)+minClosePrice
    medianQuartilePrice = (rangeClose/2)+minClosePrice
    upperQuartilePrice = (3*rangeClose/4)+minClosePrice

    lowerPercentileIndex = numberOfTicks/4
    medianPercentileIndex = numberOfTicks/2
    UpperPercentileIndex = 3*numberOfTicks/4

    lowerPercentileClose = closingPriceListSorted[lowerPercentileIndex]
    medianPercentileClose = closingPriceListSorted[medianPercentileIndex]
    upperPercentileClose = closingPriceListSorted[UpperPercentileIndex]


    for i in result:
        if i['close'] <=lowerPercentileClose:
            i['percentile'] = 1

        elif (i['close'] >lowerPercentileClose) & (i['close'] <= medianPercentileClose):
            i['percentile'] = 2
        elif (i['close'] >medianPercentileClose) & (i['close'] <= upperPercentileClose):
            i['percentile'] = 3
        elif i['close'] >upperPercentileClose:
            i['percentile'] = 4
        else:
            continue
        if i['close'] <=lowerQuartilePrice:
            i['quartile'] = 1
        elif (i['close'] >lowerQuartilePrice) & (i['close'] <= medianQuartilePrice):
            i['quartile'] = 2
        elif (i['close'] >medianQuartilePrice) & (i['close'] <= upperQuartilePrice):
            i['quartile'] = 3
        elif i['close'] >upperQuartilePrice:
            i['quartile'] = 4
        else:
            continue

        all.append(i)


    file4 = proc3.getProcessed4()
    with open(file4, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(all)
#*********************************

#*********************************
for proc4 in listDataset:
    result = np.loadtxt(proc4.getProcessed4(), skiprows=1, delimiter = ',', dtype=DT )
    all = []
    maxPrice = 0
    minPrice = 10000000
    #calculate for 100 bars concept

    for i in result:
        closingPriceList.append(i['close'])
    numberOfTicks = len(closingPriceList)

    closingPriceListSorted = sorted(closingPriceList)
    minClosePrice = closingPriceListSorted[0]
    maxClosePrice = closingPriceListSorted[numberOfTicks-1]
    fibonacciRange = maxClosePrice-minClosePrice


    for i in result:
        y = (100*(i['close']-minClosePrice)/fibonacciRange)
        i['fibonaccipercent'] = y
        all.append(i)

    file5 = proc4.getProcessed5()
    with open(file5, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        writer.writerows(all)
#*********************************
