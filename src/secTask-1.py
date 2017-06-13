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
        for index in range(len(Min)):
	        Average=(Min[index]+Max[index])/2
	        AverageTemp.append(Average)
        percent = 5
        Min_5_95, Max_5_95 = get_computePercentage(Max,Min,percent)
        percent = 25
        Min_25_75, Max_25_75 = get_computePercentage(MinTempOrigin,MaxTempOrigin,percent)
        #plot = create_plot(source,AverageTemp,Min_5_95,Max_5_95,Min_25_75,Max_25_75,Min,Max,plotDate, args.cityName[i])
        plot_graph = Figure(x_axis_type="datetime", plot_width=1000,title="2016 Daily Growing Degree Days- " + args.cityName[i], toolbar_location=None)
        plot_graph.quad(top=Max_25_75, bottom=Min_25_75, left='left', right='right', source=source,color="#ADD8E6", legend="percentile 25-75")
        plot_graph.quad(top=Max_5_95, bottom=Min_5_95, left='left', right='right', source=source,color="#D2B48C", legend="Percentile 5-95")
        plot_graph.circle(Max, Min, alpha=0.9, color="#0000FF", fill_alpha=0.2, size=10, source=source,legend='2016')
        plot_graph.line(plotDate, AverageTemp, source=source, line_color='Red', line_width=0.5, legend='Average')
        plot_graph.xaxis.axis_label = "MONTHS"
        plot_graph.yaxis.axis_label = "Daily Accumulation Celcius"
        plot_graph.grid[0].ticker.desired_num_ticks = 12

        output_file("./plots/secTask-1"+args.cityName[i]+".html", title="2016 Daily Growing Degree Days-("+args.cityName[i]+")")
        save(plot_graph)

if __name__ == '__main__':
    Main()
