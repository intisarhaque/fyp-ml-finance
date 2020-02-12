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

METRICRESULTS = 3


# date = "02.01.2018 14:30:00.000 GMT-0000"
# date = date[0:-13]
# date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')

# v = open('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv')
# w = open('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv', 'w')
# r = csv.reader(v)
# all = []
# row0 = next(r)
# for item in r:
    # for i in range(0,METRICRESULTS):
        # item.append("0")
    # item.append("0")
    # all.append(row)
    print(item)

v = open('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv')
r = csv.reader(v)
row0 = next(r)
print(row0)
for item in r:
    for i in range(0,METRICRESULTS):
        item.append("0")
    print(item)

# with open('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv','r') as csvinput:
    # with open('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv', 'w') as csvoutput:
        # writer = csv.writer(csvoutput)
        # v = open('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv')
        # r = csv.reader(v)
        # all = []
        # row0 = next(r)
        # all.append(row)

        # for row in r:
            # item.append("0")
            # all.append(row)

        # writer.writerows(all)


dt = np.dtype( [
    ('datetime', object), 
    ('open', float), 
    ('high', float),
    ('low', float),
    ('close', float),
    ('volume', float)])
    

# df = pd.read_csv('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv')
# df['Local time'] = df['Local time'].str.Substring(22, -1)


result = np.loadtxt('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv', skiprows=1, delimiter = ',', dtype=dt ) 
print(result[12]['open'])

for i in result:
    date = i['datetime']
    date = date[0:-13]
    date = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
    i['datetime'] = date
    #print(i['datetime'].time())


    
    
# print(result[0]['high'])
# print(date.time())







# xaxis = result['time']
# yaxismu = result['close']
# plt.figure(0)
# plt.plot(xaxis, yaxismu)
# plt.xlabel('Time')
# plt.ylabel('Close')
# plt.axhline(y=1, color='r', linestyle='-') # Plotting the constant Y at mu=1.
# plt.title('Mu against Frequency to determine device stability')
# plt.show()



#https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
#https://cheat.readthedocs.io/en/latest/python/timezones.html
#https://www.youtube.com/watch?v=zY02utxcauo
#https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
#https://stackoverflow.com/questions/20387359/regex-to-delete-whitespace-in-csv-file-with-quotes-to-separate-text
#https://www.machinelearningplus.com/time-series/time-series-analysis-python/
#https://www.quandl.com/data/EOD/AMD-Advanced-Micro-Devices-Inc-AMD-Stock-Prices-Dividends-and-Splits
