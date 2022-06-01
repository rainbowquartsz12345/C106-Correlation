import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    mark = []
    days = []
    with open(data_path) as cf:
        cr = csv.DictReader(cf)
        for g in cr:
            mark.append(float(g["Marks In Percentage"]))
            days.append(float(g["Days Present"]))

    return{'x': mark, "y": days}

def findCorrelation(datasource):
    c = np.corrcoef( datasource["x"], datasource["y"])
    print(f"The correlation is {c[0, 1]}")

def setup():
    dp = "Student Marks vs Days Present.csv"
    ds = getDataSource(dp)
    findCorrelation(ds)

setup()
    
#This is a direct correlation