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
    self.csvProcessed2 = csvRaw[0:-4] + ".Processed1.csv" #file with candlestick


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
#*********************************


#*********************************
class Candle:
    def __init__(self, open, high, low, close):
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    def getCandleClass(a):
        if a.open > a.close:
            return "green"
        elif a.open < a.close:
            return "red"
        else:
            return "neither"

        #green is open>close
        #red is open<close
#*********************************




#*********************************
txtfiles = []
for file in glob.glob("C:\\Users\\arsen\\Documents\\fyp-ml-finance\\dataset\\tempdatasetraw/*"):
    txtfiles.append(file)
#for file in glob.glob("H:/Documents/fyp-ml-finance/dataset/tempdatasetraw/*"):


listDataset = []
for i in txtfiles:
    D = Dataset(i)
    #D.myfunc()
    print("\n")
    listDataset.append(D)
#*********************************


v = open(listDataset[0].csvRaw)
r = csv.reader(v)
row0 = next(r)
#print(row0)
all = []
for item in r:
    item.append("candlestick")
    item.append("0")
    all.append(item)

file0 = listDataset[0].getProcessed0()
print("file0 is " + file0)

with open(file0, 'w') as csvoutput:
     writer = csv.writer(csvoutput, lineterminator='\n')
     writer.writerows(all)


dt = np.dtype( [
    ('datetime', object),
    ('open', float),
    ('high', float),
    ('low', float),
    ('close', float),
    ('volume', float),
    ('candlestick', object),
    ('score', int)])
result = np.loadtxt(listDataset[0].getProcessed0(), skiprows=1, delimiter = ',', dtype=dt )

all = []
for i in result:
    date = i['datetime']
    date = date[0:-13]
    date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    i['datetime'] = date
    #print(i['datetime'].time())
    timeVal = Candle(i['open'], i['high'], i['low'], i['close'])
    candleVal = timeVal.getCandleClass()
    i['candlestick'] = candleVal
    all.append(i)

file1 = listDataset[0].getProcessed1()
with open(file1, 'w') as csvoutput:
    writer = csv.writer(csvoutput, lineterminator='\n')
    writer.writerows(all)








# for i in all:
#     print(i)

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
