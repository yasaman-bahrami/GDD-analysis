import pandas as pd
import os
import argparse
from bokeh.palettes import Blues4
from bokeh.plotting import Figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, BoxSelectTool
from getCSVData import getCSVData
import pdb


def make_plot(src, city):
    hover = HoverTool(
        tooltips=[
            ("GDD", "$y"),
            ("Date", "@dateStr")
        ],
        mode='vline'
    )
    TOOLS = [BoxSelectTool(), hover]
    plot = Figure(x_axis_type="datetime", plot_width=700, tools=TOOLS, title= city)
    colors = Blues4[0:3]
    plot.line(x='date', y='GDD',source=src, line_width=4)
    plot.xaxis.axis_label = "Months"
    plot.yaxis.axis_label = "Accumulated GDD"
    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12
    return plot


def Main():
   parser = argparse.ArgumentParser()
   parser.add_argument("-st", dest="stationId", nargs = '*')
   parser.add_argument("-ct", dest="cityName", nargs = '*')
   args = parser.parse_args()
   currPath = os.getcwd()
   for i in range(len(args.stationId)):
       File = '{}/CSVData/{}GDDData.csv'.format(currPath, args.cityName[i])
       Data, Date, Max, Min = getCSVData(File)
       Data['date'] = pd.to_datetime(Date)
       Data['left'] = Data.date - pd.DateOffset(days=0.5)
       Data['right'] = Data.date + pd.DateOffset(days=0.5)
       Data = Data.set_index(['date'])
       Data.sort_index(inplace=True)
       source = ColumnDataSource(data=Data)

   for i in range(len(args.stationId)):
       plot = make_plot(source, args.cityName[i])
       output_file("./plots/secTask-5" + args.cityName[i] + ".html",title="2016 Daily Growing Degree Days-(" + args.cityName[i] + ")")
       save(plot)

if __name__ == '__main__':
    Main()

