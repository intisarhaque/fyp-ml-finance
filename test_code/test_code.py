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


txtfiles = []
for file in glob.glob("H:/Documents/fyp-ml-finance/dataset/tempdatasetraw/*"):
    txtfiles.append(file)

listDataset = []
class Dataset:
  def __init__(self, csvRaw):
    self.csvRaw = csvRaw
    self.csvProcessed0 = csvRaw[0:-4] + ".Processed0.csv"

  def myfunc(a):
    print("raw= " + a.csvRaw + "\nprocessed= " + a.csvProcessed0)
    
  def getProcessed0(a):
    x = ""
    x += a.csvProcessed0
    return x


for i in txtfiles:
    D = Dataset(i)
    D.myfunc()
    print("\n")
    listDataset.append(D)
    
# p1 = Person("John", 36)
# p1.myfunc()


 


v = open(listDataset[0].csvRaw)
r = csv.reader(v)
row0 = next(r)
print(row0)
all = []
for item in r:
    item.append("candlestick")
    item.append("0")
    all.append(item)       

file0 = listDataset[0].getProcessed0()
print(file0)

with open(file0, 'w') as csvoutput:
     writer = csv.writer(csvoutput, lineterminator='\n')
     writer.writerows(all)


# dt = np.dtype( [
    # ('datetime', object), 
    # ('open', float), 
    # ('high', float),
    # ('low', float),
    # ('close', float),
    # ('volume', float),
    # ('candlestick', object),
    # ('score', int)])   
# result = np.loadtxt('output.csv', skiprows=1, delimiter = ',', dtype=dt ) 
 
# all = []
# for i in result:
    # date = i['datetime']
    # date = date[0:-13]
    # date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    # i['datetime'] = date
    #print(i['datetime'].time())
    # all.append(i)
   
# with open('output.csv', 'w') as csvoutput:
    # writer = csv.writer(csvoutput, lineterminator='\n')
    # writer.writerows(all)
    
# for i in all:
    # print(i)
    
# xaxis = result['datetime']
# yaxismu = result['close']
# plt.figure(0)
# plt.plot(xaxis, yaxismu)
# plt.xlabel('Time')
# plt.ylabel('Close')
# plt.title('Mu against Frequency to determine device stability')
# plt.show()












#https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
#https://cheat.readthedocs.io/en/latest/python/timezones.html
#https://www.youtube.com/watch?v=zY02utxcauo
#https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
#https://stackoverflow.com/questions/20387359/regex-to-delete-whitespace-in-csv-file-with-quotes-to-separate-text
#https://www.machinelearningplus.com/time-series/time-series-analysis-python/
#https://www.quandl.com/data/EOD/AMD-Advanced-Micro-Devices-Inc-AMD-Stock-Prices-Dividends-and-Splits
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory