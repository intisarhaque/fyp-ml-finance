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
class Queue(object):
    def __init__(self):
        self.items=[]
        self.total = 0
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
        if (type(item) is int) or (type(item) is float) or (type(item) is long) or (type(item) is long) or (isinstance(item, np.float64)):
            self.total += item
    def dequeue(self):
        item = self.items.pop()
        if (type(item) is int) or (type(item) is float) or (type(item) is long) or (type(item) is long) or (isinstance(item, np.float64)):
            self.total -=item
        return item
    def size(self):
        return len(self.items)
    def movingtickaverage(self):
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
        if (gain == 0) & (loss == 0):
            rs = 1
        else:
            rs = gain/loss
        rsi = 100 -(100/(1+rs))
        return rsi

    def twentydayrsi(self):
        #mustreview
        diffcollection = []
        for i in range(0,20):
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
        gain = gain/20
        loss = loss/20
        if (gain == 0) & (loss == 0):
            rs = 1
        elif loss == 0:
            rs = 1
        else:
            rs = gain/loss
        rsi = 100 -(100/(1+rs))
        return rsi

    def fiftydayrsi(self):
        #mustreview
        diffcollection = []
        for i in range(0,50):
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
        gain = gain/50
        loss = loss/50
        if (gain == 0) & (loss == 0):
            rs = 1
        else:
            rs = gain/loss
        rsi = 100 -(100/(1+rs))
        return rsi
