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

txtfiles = []
for file in glob.glob("*.csv"):
    txtfiles.append(file)
print(txtfiles)
METRICRESULTS = 2



v = open('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv')
r = csv.reader(v)
row0 = next(r)
print(row0)
all = []
for item in r:
    # for i in range(0,METRICRESULTS):
        # item.append("0")
    item.append("candlestick")
    item.append("0")
    all.append(item)        
with open('output.csv', 'w') as csvoutput:
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
result = np.loadtxt('output.csv', skiprows=1, delimiter = ',', dtype=dt ) 
 
all = []
for i in result:
    date = i['datetime']
    date = date[0:-13]
    date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    i['datetime'] = date
    #print(i['datetime'].time())
    all.append(i)
   
with open('output.csv', 'w') as csvoutput:
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












#https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
#https://cheat.readthedocs.io/en/latest/python/timezones.html
#https://www.youtube.com/watch?v=zY02utxcauo
#https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
#https://stackoverflow.com/questions/20387359/regex-to-delete-whitespace-in-csv-file-with-quotes-to-separate-text
#https://www.machinelearningplus.com/time-series/time-series-analysis-python/
#https://www.quandl.com/data/EOD/AMD-Advanced-Micro-Devices-Inc-AMD-Stock-Prices-Dividends-and-Splits
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory