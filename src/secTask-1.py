import pandas as pd
import os
from bokeh.plotting import output_file, show, save
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource
import argparse
from getCSVData import getCSVData
from bokeh.models import Legend
import pdb

def cleanData(temp, percent):
    lenTemp = len(temp) - 1
    Maximum = int(365 * (int(percent) / 100))
    DeleteTemp = temp.argsort()[:-Maximum]
    DeleteTemp = DeleteTemp[:Maximum]
    for value in DeleteTemp:
        if (value == lenTemp):
            temp[value] = (temp[value - 1] + temp[value])
        elif (value == 0):
            temp[value] = (temp[value + 1] + temp[value])
        else:
            temp[value] = (temp[value - 1] + temp[value + 1])
            temp[value] = temp[value] / 2
    return temp

def getComputePercentage(minTemp,maxTemp,percent):
    """Subtracts from percentile and return the value"""
    minTemp = cleanData(minTemp, percent)
    maxTemp = cleanData(maxTemp, percent)
    return minTemp,maxTemp

def prepareCSVData(cityName):
    filePath = (os.getcwd() + '/CSVData/' + cityName + 'GDDData.csv')
    Data, Date, maxTemp, minTemp = getCSVData(filePath)
    Data['date'] = pd.to_datetime(Date)
    Data['left'] = Data.date - pd.DateOffset(days=0.5)
    Data['right'] = Data.date + pd.DateOffset(days=0.5)
    Data = Data.set_index(['date'])
    Data.sort_index(inplace=True)
    return Data, Date, maxTemp, minTemp

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*')
    parser.add_argument("-ct", dest="cityName", nargs = '*')
    parser.add_argument("-pr", dest="percentage", nargs = '*')
    parser.add_argument("-tc1", dest="taskColor1", nargs = '*')
    args = parser.parse_args()
    for i in range(len(args.stationId)):
        Data, Date, Max, Min = prepareCSVData(args.cityName[i])
        plotDate = Data['right']
        source = ColumnDataSource(data=Data)
        AverageTemp = []
        for index in range(len(Min)):
	        Average=(Min[index]+Max[index])/2
	        AverageTemp.append(Average)
        plot_graph = Figure(x_axis_type="datetime", plot_width=1000,title="2016 Daily Growing Degree Days- " + args.cityName[i], toolbar_location=None)
        color = "#ADD8E6"
        for j in range(len(args.percentage)):
            minPer,MaxPer =  getComputePercentage(Min, Max, args.percentage[j])
            plot_graph.quad(top=MaxPer, bottom=minPer, left='left', right='right', source=source, color=color,legend="percentile "+str(args.percentage[j])+"-"+str(100-int(args.percentage[j])))
            color = "#D2B48C"
        plot_graph.circle(Max, Min, alpha=0.9, color="#0000FF", fill_alpha=0.2, size=10, source=source,legend='2016')
        plot_graph.line(plotDate, AverageTemp, source=source, line_color='Red', line_width=0.5, legend='Average')
        plot_graph.xaxis.axis_label = "MONTHS"
        plot_graph.yaxis.axis_label = "Daily Accumulation Celcius"
        plot_graph.grid[0].ticker.desired_num_ticks = 12

        output_file("./plots/secTask-1"+args.cityName[i]+".html", title="2016 Daily Growing Degree Days-("+args.cityName[i]+")")
        save(plot_graph)

if __name__ == '__main__':
    Main()
