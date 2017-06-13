import pandas as pd
import os
import argparse
from bokeh.embed import components
from bokeh.palettes import Spectral11
from bokeh.plotting import Figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool, BoxSelectTool
from getCSVData import getCSVData
import pdb


def city_plot(city_info):
    ''' producing interactive plot '''

    plot = Figure(x_axis_type="datetime", plot_width=1000, title="GDD of cities of Canada (Accumulated)")
    colors = Spectral11[0:len(city_info)]
    key = 0
    for src in city_info:
        plot.line(x='DATE', y='GDD', source=city_info[src], color=colors[key], line_width=4, legend=src)
        key += key

    plot.grid.grid_line_alpha = 0.3
    plot.grid[0].ticker.desired_num_ticks = 12
    return plot


''' reading data from file'''
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-st", dest="stationId", nargs = '*')
    parser.add_argument("-ct", dest="cityName", nargs = '*')
    args = parser.parse_args()


    plot = city_plot(cityData)
    output_file("./plots/secTask-4.html", title="Secondary Task 4 ")
    save(plot)
    scr, div = components(plot)
    fs = open("./plots/secTask-4.scr", 'w')
    fs.write(scr)
    fd = open("./plots/secTask-4.div", 'w')
    fd.write(div)
    print(div) 
	
if __name__ == '__main__':
    Main()


