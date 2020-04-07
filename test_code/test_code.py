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
METRICRESULTS = 2

#*********************************
class Dataset:

    def __init__(self, csvRaw):
        self.csvRaw = csvRaw
        self.csvProcessed0 = csvRaw[0:-4] + ".Processed0.csv" #file with 2 columns
        self.csvProcessed1 = csvRaw[0:-4] + ".Processed1.csv" #file with correct data
        self.csvProcessed2 = csvRaw[0:-4] + ".Processed2.csv" #file with candletype/colour
        self.csvProcessed3 = csvRaw[0:-4] + ".Processed3.csv" #file with movingaverage
        self.csvProcessed4 = csvRaw[0:-4] + ".Processed4.csv" #file with quartile

    def myfunc(a):
        print("raw= " + a.csvRaw + "\nprocessed= " + a.csvProcessed0)

    def getProcessed0(a):
        x = ""
        x += a.csvProcessed0
        return x

    def getProcessed1(a):
        x = ""
        x += a.csvProcessed1
        return x

    def getProcessed2(a):
        x = ""
        x += a.csvProcessed2
        return x

    def getProcessed3(a):
        x = ""
        x += a.csvProcessed3
        return x

    def getProcessed4(a):
        x = ""
        x += a.csvProcessed4
        return x
#*********************************


#*********************************
class Candle:
    def __init__(self, open, high, low, close):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.colour = "neither"
        self.candletype = "none"
        self.fivedayaverage = 0
        self.rsi = 50
        self.quartile = 50

    def getColour(a):
        return a.colour
        #green is open>close
        #red is open<close

    def setColour(a):
        if a.open > a.close:
            a.colour = "black"
        elif a.open < a.close:
            a.colour = "white"
        else:
            a.colour = "neither"

    def getCandleType(a):
        return a.candletype

    def setCandleType(a):
        if (a.getColour() == "white") & (a.high == a.close) & (a.open == a.low):
            a.candletype = "whiteMaruboxu"
        if (a.getColour() == "black") & (a.high == a.open) & (a.close == a.low):
            a.candletype = "blackMaruboxu"
        if (a.open == a.close):
            a.candletype = "doji"

    def getCandleFiveDayAve(a):
        return a.fivedayaverage

    def setCandleFiveDayAve(a, item):
        a.fivedayaverage = item

    def getrsi(a):
        return a.rsi

    def setrsi(a, item):
        a.rsi = item
#*********************************

#*********************************
class Queue(object):
    def __init__(self):
        self.items=[]
        self.total = 0
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
        self.total += item
    def dequeue(self):
        item = self.items.pop()
        self.total -=item
        return item
    def size(self):
        return len(self.items)
    def fivedayaverage(self):
        return self.total/self.size()
    def fivedayrsi(self):
        #mustreview
        diffcollection = []
        for i in range(0,5):
            x = self.items.pop()
            diffcollection.append(x)
            self.items.insert(0,x)
        gain = 0
        loss = 0
        for i in diffcollection:
            if i>0:
                gain +=i
            else:
                loss += (i*-1)
        gain = gain/5
        loss = loss/5
        rs = gain/loss
        rsi = 100 -(100/(1+rs))
        return rsi





#*********************************



#*********************************
txtfiles = []
for file in glob.glob("C:\\Users\\arsen\\Documents\\fyp-ml-finance\\dataset\\tempdatasetraw/*"):
    txtfiles.append(file)
#for file in glob.glob("H:/Documents/fyp-ml-finance/dataset/tempdatasetraw/*"):
#for file in glob.glob("C:\\Users\\arsen\\Documents\\fyp-ml-finance\\dataset\\tempdatasetraw/*"):
listDataset = []
for i in txtfiles:
    D = Dataset(i)
    #D.myfunc()
    #print("\n")
    listDataset.append(D)
#*********************************

#*********************************
v = open(listDataset[0].csvRaw)
r = csv.reader(v)
row0 = next(r)
#print(row0)
all = []
for item in r:
    item.append("colour")
    item.append("candletype")
    item.append(0)#5daymovingaverage
    item.append(50)#rsi
    item.append(2)#quartile
    all.append(item)

file0 = listDataset[0].getProcessed0()
with open(file0, 'w') as csvoutput:
     writer = csv.writer(csvoutput, lineterminator='\n')
     writer.writerows(all)
#*********************************

#*********************************
dt = np.dtype( [
    ('datetime', object),
    ('open', float),
    ('high', float),
    ('low', float),
    ('close', float),
    ('volume', float),
    ('colour', object),
    ('candletype', object),
    ('fivedayaverage', float),
    ('fivedayrsi', float),
    ('quartile', float)])
result = np.loadtxt(listDataset[0].getProcessed0(), skiprows=1, delimiter = ',', dtype=dt )

all = []
for i in result:
    date = i['datetime']
    date = date[0:-13]
    date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    i['datetime'] = date
    #print(i['datetime'].time())
    all.append(i)

file1 = listDataset[0].getProcessed1()
with open(file1, 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    writer.writerows(all)
#*********************************

#*********************************
all = []
result = np.loadtxt(listDataset[0].getProcessed1(), skiprows=1, delimiter = ',', dtype=dt )
for i in result:
    timeVal = Candle(i['open'], i['high'], i['low'], i['close'])
    timeVal.setColour()
    colourVal = timeVal.getColour()
    i['colour'] = colourVal
    timeVal.setCandleType()
    candletypeVal = timeVal.getCandleType()
    i['candletype'] = candletypeVal
    all.append(i)

file2 = listDataset[0].getProcessed2()
with open(file2, 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    writer.writerows(all)
#*********************************

#*********************************
all = []
result = np.loadtxt(listDataset[0].getProcessed2(), skiprows=1, delimiter = ',', dtype=dt )
q5 = Queue()
q5rsi = Queue()
q5rsi.enqueue(0)
q5rsi.enqueue(0)
q5rsi.enqueue(0)
q5rsi.enqueue(0)
q5rsi.enqueue(0)
closeprev = 0
for i in result:
    diff = i['close']-closeprev
    closeprev =  i['close']
    q5rsi.enqueue(diff)
    q5rsi.dequeue()
    if q5.size() < 5:
        q5.enqueue(i['close'])
    else:
        #can possibly be done with just a running total as opposed to a queue.
        #with more moving indicators, a queue can be more useful
        q5.enqueue(i['close'])
        q5.dequeue()


    average = q5.fivedayaverage()
    i['fivedayaverage'] = average

    rsi = q5rsi.fivedayrsi()
    i['fivedayrsi'] = rsi

    #print(rsi)
    all.append(i)


file3 = listDataset[0].getProcessed3()
with open(file3, 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    writer.writerows(all)
#*********************************


all = []
result = np.loadtxt(listDataset[0].getProcessed3(), skiprows=1, delimiter = ',', dtype=dt )
closingPriceList = []
for i in result:
    closingPriceList.append(i['close'])
numberOfTicks = len(closingPriceList)

closingPriceListSorted = sorted(closingPriceList)
minClosePrice = closingPriceListSorted[0]
maxClosePrice = closingPriceListSorted[numberOfTicks-1]

lowerQuartileIndex = numberOfTicks/4
medianIndex = numberOfTicks/2
UpperQuartileIndex = 3*numberOfTicks/4

lowerQuartileClose = closingPriceListSorted[lowerQuartileIndex]
medianClose = closingPriceListSorted[medianIndex]
upperQuartileClose = closingPriceListSorted[UpperQuartileIndex]

for i in result:
    if i['close'] <=lowerQuartileClose:
        i['quartile'] = 1
    elif (i['close'] >lowerQuartileClose) & (i['close'] <= medianClose):
        i['quartile'] = 2
    elif (i['close'] >medianClose) & (i['close'] <= upperQuartileClose):
        i['quartile'] = 3
    elif i['close'] >upperQuartileClose:
        i['quartile'] = 4
    else:
        continue
    all.append(i)


file4 = listDataset[0].getProcessed4()
with open(file4, 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    writer.writerows(all)
# xaxis = result['datetime']
# yaxismu = result['close']
# plt.figure(0)
# plt.plot(xaxis, yaxismu)
# plt.xlabel('Time')
# plt.ylabel('Close')
# plt.title('Mu against Frequency to determine device stability')
# plt.show()











# p1 = Person("John", 36)
# p1.myfunc()
#https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
#https://cheat.readthedocs.io/en/latest/python/timezones.html
#https://www.youtube.com/watch?v=zY02utxcauo
#https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
#https://stackoverflow.com/questions/20387359/regex-to-delete-whitespace-in-csv-file-with-quotes-to-separate-text
#https://www.machinelearningplus.com/time-series/time-series-analysis-python/
#https://www.quandl.com/data/EOD/AMD-Advanced-Micro-Devices-Inc-AMD-Stock-Prices-Dividends-and-Splits
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
#https://www.thinkmarkets.com/tfxmain/media/img/pdf/Candlestick_Patterns_Trading_Guide.pdf
#https://books.google.co.uk/books?id=lfEPBwAAQBAJ&printsec=frontcover&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false
#https://pdfs.semanticscholar.org/049c/dd8c897e98213394de6ad8fb441291f8e80a.pdf
#https://www.reddit.com/r/algotrading/comments/doz9kl/isnt_there_a_program_anyone_sells_that_recognizes/
#https://medium.com/analytics-vidhya/recognizing-over-50-candlestick-patterns-with-python-4f02a1822cb5
#https://github.com/mrjbq7/ta-lib/tree/master/talib
#https://fxgears.com/index.php?threads/recommended-books-for-algo-trading-in-2020.1243/
#https://www.youtube.com/watch?v=8ILZZpIJSYs


#timeseries
#https://www.youtube.com/watch?v=e8Yw4alG16Q
#https://www.youtube.com/watch?v=bn8rVBuIcFg
#https://otexts.com/fpp2/graphics.html
#file:///C:/Users/arsen/Documents/Y3S1/Project%20shit/papers/pdfslide.net_expert-system-for-predicting-stock-market-timing-using-a-candlestick-chart.pdf  expert system, predfined rules of candlestick, i want rules to change
#file:///C:/Users/arsen/Documents/Y3S1/Project%20shit/papers/88ee95e16dac7a2e4d65aa095199bbc3439f.pdf
#file:///C:/Users/arsen/Documents/Y3S1/Project%20shit/papers/Using_Machine_Learning_Techniques_to_Combine_Forec.pdf
