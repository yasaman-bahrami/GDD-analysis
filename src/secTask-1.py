import numpy as np
import pandas as pd
import os
from bokeh.plotting import output_file, show, save
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource




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


