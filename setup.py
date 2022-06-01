import plotly.express as px
import csv
import numpy as np



def getDataSource(data_path):
     temp = []
     ice_cream_sales = []
     with open(data_path) as csv_file:
          csv_reader = csv.DictReader(csv_file)
          for row in csv_reader:
               temp.append( float( row["Temperature"] ) )
               ice_cream_sales.append(float(row["Ice-cream Sales"]))

     return {"x" : temp, "y": ice_cream_sales}

def findCorrelation(datasource):
     c = np.corrcoef( datasource["x"] , datasource["y"])
     print(f"\ncorrelation between temperature and ice cream sales :  { c[0,1]}")

def setup():
     dp = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
     ds = getDataSource( dp )
     findCorrelation( ds )

setup()

#since value is almost 1 it is directly correlated