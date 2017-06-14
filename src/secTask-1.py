import numpy as np
import pandas as pd
import os
from bokeh.plotting import output_file, show, save
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource
import argparse
from getCSVData import getCSVData
import matplotlib.pyplot as plt
import pdb



def create_plot(source,AverageTemp,Parcentile_5_Min,Parcentile_5_Max,Parcentile_25_Min,Parcentile_25_Max,MinTemp,MaxTemp,plotDate, cityName):
    """Making Bokeh plot"""
    plot_graph = Figure(x_axis_type="datetime", plot_width=1000, title="2016 Daily Growing Degree Days- "+cityName, toolbar_location=None)
    plot_graph.quad(top=Parcentile_25_Max, bottom=Parcentile_25_Min,left='left',right='right', source=source,color="#ADD8E6",legend="percentile 25-75")
    plot_graph.quad(top=Parcentile_5_Max, bottom=Parcentile_5_Min, left='left', right='right', source=source,color="#D2B48C", legend="Percentile 5-95")
    plot_graph.circle(MaxTemp, MinTemp, alpha=0.9, color="#0000FF", fill_alpha=0.2, size=10, source=source,legend='2016')
    plot_graph.line(plotDate,AverageTemp,source=source,line_color='Red', line_width=0.5, legend='Average')
    plot_graph.xaxis.axis_label = "MONTHS"
    plot_graph.yaxis.axis_label = "Daily Accumulation Celcius"
    plot_graph.grid[0].ticker.desired_num_ticks = 12
    return plot_graph


def get_percentile(Max,Min,percent):
    """Subtracts from percentile and return the value"""

    Maximum = int(365*(percent/100))
    Delete_min = Min.argsort()[:-Maximum]
    MinValue= Delete_min[:Maximum]
    for value in MinValue:
        if (value == len(Max)-1):
            Min[value]=(Min[value-1]+Min[value])
        elif (value == 0):
            Min[value]=(Min[value+1]+Min[value])
        else:
            Min[value]=(Min[value-1]+Min[value+1])

        Min[value] = Min[value]/2

    Delete_max = Max.argsort()[-Maximum:]
    Delete_max = Delete_max[:Maximum]
    for value in Delete_max:
        if (value == len(Min)-1):
            Max[value]=(Max[value-1]+Max[value])
        elif (value == 0):
            Max[value]=(Max[value+1]+Max[value])
        else:
            Max[value]=(Max[value-1]+Max[value+1])
        Max[value] = Max[value]/2
    return Min,Max

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*')
    parser.add_argument("-ct", dest="cityName", nargs = '*')
    args = parser.parse_args()
    currPath = os.getcwd()
    for i in range(len(args.stationId)):
        File= '{}/CSVData/{}GDDData.csv'.format(currPath,args.cityName[i])
        Data, Date, Max, Min = getCSVData(File)
        Data['date'] = pd.to_datetime(Date)
        Data['left'] = Data.date - pd.DateOffset(days=0.5)
        Data['right'] = Data.date + pd.DateOffset(days=0.5)
        plotDate = Data['right']
        Data = Data.set_index(['date'])
        Data.sort_index(inplace=True)
        source = ColumnDataSource(data=Data)
        MinTempOrigin1 = []
        MaxTempOrigin2 = []
        for index in range(len(Min)):
	        MinTempOrigin1.append(Min[index])
	        MaxTempOrigin2.append(Max[index])
        MinTempOrigin = np.asarray(MinTempOrigin1)
        MaxTempOrigin = np.asarray(MaxTempOrigin2)
        AverageTemp = []

        Min_5_95, Max_5_95 = get_percentile(Max,Min,percent)
        percent = 25
        Min_25_75, Max_25_75 = get_percentile(MinTempOrigin,MaxTempOrigin,percent)
        plot = create_plot(source,AverageTemp,Min_5_95,Max_5_95,Min_25_75,Max_25_75,Min,Max,plotDate, args.cityName[i])
        #plot.savefig("./reports/secTask-1"+args.cityName[i]+".png")
        output_file("./plots/secTask-1"+args.cityName[i]+".html", title="2016 Daily Growing Degree Days-("+args.cityName[i]+")")
        save(plot)

if __name__ == '__main__':
    Main()
