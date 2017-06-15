from bokeh.charts import Donut, show, output_file
from bokeh.charts.utils import df_from_json
from bokeh.sampledata.olympics2014 import data
from bokeh.charts import Bar, output_file, show, save
import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import argparse
from getCSVData import getCSVData
from saveCSVData import saveCSVData
import wget
import pdb

base_temp = 10


def make_plot(Data,city_name):
    # pdb.set_trace()
    plt.suptitle('Final Task   '+city_name)
    plt.subplot(1, 2, 1)
    plt.plot(Data['GDD'], Data['Mean Temp'], 'r-')
    plt.title('mean temp vs GDD')
    plt.xlabel('GDD')
    plt.ylabel('Mean Temp')
    plt.grid()
    plt.subplot(1, 2, 2)
    plt.title('Total recip vs GDD')
    plt.grid()
    plt.plot(Data['GDD'], Data['Total Precip'], 'b-')
    plt.xlabel('GDD')
    plt.ylabel('Total Precip')
    plt.savefig('./reports/finalTask'+city_name+'.png')
    plt.clf()
    plt.close()

#****************************************************
''' producing the items we want from the data which has downloaded'''

def cleanCSV(gddData):
    Data = pd.DataFrame(gddData)
    Data.replace('', np.nan, inplace=True)
    Data = Data.dropna()
    Date, maxTemp, minTemp, mean_temp, total_Rain, total_Precip = np.array(Data['Date/Time']), np.array(Data['Max Temp']), np.array(Data['Min Temp']),np.array(Data['Mean Temp']),np.array(Data['Total Rain']),np.array(Data['Total Precip'])
    return Data, Date, maxTemp, minTemp, mean_temp, total_Rain, total_Precip

def getCSVData(filePath):
    gddData = pd.read_csv(filePath, delimiter = ',' ,skiprows=0)
    Data, Date, maxTemp, minTemp, mean_temp, total_Rain, total_Precip = cleanCSV(gddData)
    return Data, Date, maxTemp, minTemp, mean_temp, total_Rain, total_Precip


#**********************************************
'''downloading the data  '''

def downloadData(startYear, endYear, stationId, cityName):  # Download form the url
    while (startYear <= endYear):
        url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=' + str(
            stationId) + '&Year=' + str(startYear) + '&Month=12&Day=31&timeframe=2&submit= Download+Data'
        # pdb.set_trace()
        try:
            filename = wget.download(url)
        except:
            print("Sorry, a problem occured during downloading files,please try it later.")
        try:
            cityData = pd.read_csv(filename, encoding='ISO-8859-1', delimiter=',', skiprows=25)
        except Exception as e:
            print("Error in Reading", filename)
            print(e)

        cols = cityData.columns.values  # adjusting the columns
        for i in range(0, len(cols)):
            if "Max Temp (" in cols[i]:
                cols[i] = "Max Temp"
            if "Min Temp (" in cols[i]:
                cols[i] = "Min Temp"
            if "Mean Temp (" in cols[i]:
                cols[i] = "Mean Temp"
            if "Total Rain (" in cols[i]:
                cols[i] = "Total Rain"
            if "Total Precip (" in cols[i]:
                cols[i] = "Total Precip"

        cityData.columns = cols
        Data = pd.DataFrame(cityData, columns=['Date/Time', 'Max Temp', 'Min Temp', 'Mean Temp', 'Total Rain', 'Total Precip'])

        Data.replace('', np.nan, inplace=True)
        Data = Data.dropna()
        startYear = startYear + 1
        currentpath = os.getcwd()
        filepath = (currentpath + '/CSVData/' + cityName + 'GDDDataII.csv')

        '''Saving to .csv file.'''
        saveCSVData(Data, filepath)
        '''Removing unnecessary downloaded files.'''
        os.remove(filename)

'''------------------------------------------------------------------------------'''
'''compute GDD'''
def computeGDD(Data, baseTemp):
    key=0
    GDD=[]
    Data['GDD'] = ((Data['Max Temp'] + Data['Min Temp'])/2)- baseTemp
    for item in Data['GDD']:
        if item>=0:
            key+=item
        GDD.append(key)
    Data['GDD'] = GDD
    return Data


'''------------------------------------------------Main--------------------------------------------'''
def Main():
    '''getting initial values '''

    parser = argparse.ArgumentParser()

    parser.add_argument("-st", dest="stationId", nargs='*')
    parser.add_argument("-ct", dest="cityName", nargs='*')

    args = parser.parse_args()

    station_id_list = args.stationId
    city_name_list = args.cityName
    start_year = 2016
    end_year = 2016

    for i in range(len(station_id_list)):
        downloadData(start_year, end_year, station_id_list[i], city_name_list[i])
        CurrentPath = os.getcwd()
        FilePath = (CurrentPath + '/CSVData/' + city_name_list[i] + 'GDDDataII.csv')
        Data, Date, MaxTemp, MinTemp, mean_temp, total_Rain, total_Precip = getCSVData(FilePath)
        # pdb.set_trace()
        Data = computeGDD(Data, base_temp)
        # Index = Data.keys()
        # pdb.set_trace()
        make_plot(Data,city_name_list[i])


if __name__ == '__main__':
    Main()