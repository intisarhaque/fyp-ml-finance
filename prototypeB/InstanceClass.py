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
class Instance:
    def __init__(self, open, high, low, close):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.colour = "neither"
        self.candletype = "none"
        self.fivedayaverage = 0
        self.rsi5 = 50
        self.rsi20 = 50
        self.rsi50 = 50
        self.percentile = 2
        self.quartile = 2

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

    def setCandleType(a, q2candle):
        aprev = q2candle.items[1]
        if (a.getColour() == "white") & (a.high == a.close) & (a.open == a.low):
            a.candletype = "whiteMaruboxu"
        if (a.getColour() == "black") & (a.high == a.open) & (a.close == a.low):
            a.candletype = "blackMaruboxu"
        if (a.open == a.close):
            a.candletype = "doji"
        if ((aprev.close > aprev.open) & (a.open > a.close) & (a.open >= aprev.close)
        & (aprev.open >=a.close) & ((a.open-a.close)>(aprev.close-aprev.open))):
            a.candletype = "blackEngulfing"
        if ((aprev.close < aprev.open) & (a.open < a.close) & (a.close >= aprev.open)
        & (aprev.close >=a.open) & ((a.close-a.open)>(aprev.open-aprev.close))):
            a.candletype = "whiteEngulfing"
        if ((aprev.close>aprev.open) & (a.open>a.close) & (a.open<aprev.close)
        & (aprev.open <= a.close) & ((a.open-a.close)<(aprev.close-aprev.open))):
            a.candletype = "blackHarami"
        if ((aprev.close<aprev.open) & (a.open<a.close) & (a.close<aprev.open)
        & (aprev.close <= a.open) & ((a.close-a.open)<(aprev.open-aprev.close))):
            a.candletype = "whiteHarami"

    def instancedisplay(a):
        print(a.close)

    def getCandleFiveDayAve(a):
        return a.fivedayaverage

    def setCandleFiveDayAve(a, item):
        a.fivedayaverage = item

    def getrsi5(a):
        return a.rsi5

    def setrsi5(a, item):
        a.rsi5 = item

    def getrsi20(a):
        return a.rsi20

    def setrsi20(a, item):
        a.rsi20 = item

    def getrsi50(a):
        return a.rsi50

    def setrsi50(a, item):
        a.rsi50 = item
