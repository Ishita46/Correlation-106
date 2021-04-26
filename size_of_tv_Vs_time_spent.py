import csv 
import numpy as np


def getDataSource(data_path):
    size_of_tv = []
    time_spent = []
    with open(data_path) as csv_files:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of tv"]))
            #float means pointing vaues.
            #append means adding at the last
            time_spent.append(float(row["Time Spent"]))

    return{"x" :  size_of_tv, "y" : time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of tv and time spent :- \n--->", correlation[0,1])

def setup():
    data_path = "tv.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()