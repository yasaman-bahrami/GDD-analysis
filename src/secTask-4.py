import pandas
import os
import argparse
import pdb

from bokeh.embed import components
from bokeh.palettes import Spectral11
from bokeh.plotting import Figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, BoxSelectTool
from getCSVData import getCSVData

'''Parse .csv files and process according to the plot requirements'''
def cityPlot(cityInfo):
    ''' producing interactive plot '''
    hover = HoverTool(
        tooltips=[
            ("GDD", "$y"),
            ("Date", "@dateStr")            
        ]
    )
    TOOLS = [BoxSelectTool(), hover]
    plot = Figure(x_axis_type="datetime", plot_width=1000, tools=TOOLS, title="(Accumulated) GDD - CANADA")
    colors = Spectral11[0:len(cityInfo)]
    key = 0
    for src in cityInfo:
        plot.line(x='date', y='GDD', source=cityInfo[src], color=colors[key], line_width=4, legend=src)
        key += 1
    plot.xaxis.axis_label = "MONTHS"
    plot.yaxis.axis_label = "GDD (Accumulated)"
    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12
    return plot


''' reading data from file'''
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*')
    parser.add_argument("-ct", dest="cityName", nargs = '*')
    args = parser.parse_args()
	
    cityData = {}
    cities = { 
        args.cityName[0] : {'ID':args.stationId[0]},
        args.cityName[1] : {'ID':args.stationId[1]},
        args.cityName[2] : {'ID':args.stationId[2]}
    }

    for city in cities.keys():
        FilePath = ('./CSVData/' + city + 'GDDData.csv')
        Data, Date, MaxTemp, MinTemp = getCSVData(FilePath)
        Data['date'] = pandas.to_datetime(Date)
        Data['max'] = MaxTemp
        Data['min'] = MinTemp
        Data['right'] = Data.date + pandas.DateOffset(days=0.5)
        Data['left'] = Data.date - pandas.DateOffset(days=0.5)
        Data['dateStr'] = Date

        NewGDD = Data['GDD']
        del Data['GDD']
        Data['GDD'] = NewGDD
        del Data['Unnamed: 0']
        del Data['Max Temp']
        del Data['Min Temp']
        del Data['Date/Time']
        Data = Data.set_index(['date'])
        Data.sort_index(inplace=True)
        cityData[city] = ColumnDataSource(data=Data)

    plot = cityPlot(cityData)
    output_file("./plots/secTask-4.html", title="Secondary Task 4")
    save(plot)
    scr, div = components(plot)
    fs = open("./plots/secTask-4.scr", 'w')
    fs.write(scr)
    fd = open("./plots/secTask-4.div", 'w')
    fd.write(div)
    print(div) 
	
if __name__ == '__main__':
    Main()


