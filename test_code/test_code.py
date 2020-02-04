import cmath
import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import pyplot as plt1
# from matplotlib import pyplot as plt2
# from matplotlib import style
import csv
from math import sqrt
from dateutil import parser
from datetime import datetime

print("f")

date = "02.01.2018 14:30:00.000 GMT-0000"
date = datetime.strptime(date[:-9], '%d.%m.%y %H:%M:%S.%f')
dt = np.dtype( [('time', str), #Data type created to read in CSV file and be able to
    ('open', float), 
    ('high', float),
    ('low', float),
    ('close', float),
    ('volume', float)])
    
result = np.loadtxt('AMD.USUSD_Candlestick_1_s_BID_02.01.2018-02.01.2018.csv', skiprows=1, delimiter = ',', dtype=dt ) 
#result = np.loadtxt('HMC636ST89.csv', delimiter = ',', dtype=dt ) 

print(result[0]['high'])
print(date[:-9])