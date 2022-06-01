import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    size = []
    time = []
    with open(data_path) as cf:
        cr = csv.DictReader(cf)
        for h in cr:
            size.append(float(h["Size of TV"]))
            time.append(float(h["Average time spent watching TV in a week (hours)"]))
    return{"x": size, "y": time}

def findCorrelation(datasource):
    c = np.corrcoef( datasource["x"]  , datasource["y"] )
    print(f"The correlation is {c[0, 1]}")

def setup(  ):
    dp = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    ds = getDataSource(dp)
    findCorrelation(ds)

setup()
#This has no correlation