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

BASEDIR = "C:\\Users\\arsen\\Documents\\Y3S1\\Project shit\\fyp-ml-finance\\prototypeB\\datasetRaw\*"
PROC0DIR = "C:\\Users\\arsen\\Documents\\Y3S1\\Project shit\\fyp-ml-finance\\prototypeB\\datasetProc0\\"
PROC1DIR = "C:\\Users\\arsen\\Documents\\Y3S1\\Project shit\\fyp-ml-finance\\prototypeB\\datasetProc1\\"
PROC2DIR = "C:\\Users\\arsen\\Documents\\Y3S1\\Project shit\\fyp-ml-finance\\prototypeB\\datasetProc2\\"
PROC3DIR = "C:\\Users\\arsen\\Documents\\Y3S1\\Project shit\\fyp-ml-finance\\prototypeB\\datasetProc3\\"
PROC4DIR = "C:\\Users\\arsen\\Documents\\Y3S1\\Project shit\\fyp-ml-finance\\prototypeB\\datasetProc4\\"
PROC5DIR = "C:\\Users\\arsen\\Documents\\Y3S1\\Project shit\\fyp-ml-finance\\prototypeB\\datasetProc5\\"


DT = np.dtype( [
    ('datetime', object),
    ('open', float),
    ('high', float),
    ('low', float),
    ('close', float),
    ('volume', float),
    ('colour', object),
    ('candletype', object),
    ('5tickaverage', float),
    ('100tickaverage', float),
    ('200tickaverage', float),
    ('450tickaverage', float),
    ('1000tickaverage', float),
    ('fivedayrsi', float),#rename all day to tick
    ('twentydayrsi', float),
    ('fiftydayrsi', float),
    ('5tickaveragefuture', float),
    ('100tickaveragefuture', float),
    ('200tickaveragefuture', float),
    ('450tickaveragefuture', float),
    ('1000tickaveragefuture', float),
    ('percentile', int),
    ('quartile', int),
    ('fibonaccipercent', float)])



class Dataset:
    def __init__(self, csvDir):
        self.csvRaw = csvDir[-55:]
        self.csvDir = csvDir
        self.csvProcessed0 = PROC0DIR + self.csvRaw[0:-4] + ".processed0.csv" #file with all columbns
        self.csvProcessed1 = PROC1DIR + self.csvRaw[0:-4] + ".Processed1.csv" #file with correct data
        self.csvProcessed2 = PROC2DIR + self.csvRaw[0:-4] + ".Processed2.csv" #file with candletype/colour
        self.csvProcessed3 = PROC3DIR + self.csvRaw[0:-4] + ".Processed3.csv" #file with movingaverage
        self.csvProcessed4 = PROC4DIR + self.csvRaw[0:-4] + ".Processed4.csv" #file with percentile
        self.csvProcessed5 = PROC5DIR + self.csvRaw[0:-4] + ".Processed5.csv" #file with fibonacci


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

    def getProcessed5(a):
        x = ""
        x += a.csvProcessed5
        return x
