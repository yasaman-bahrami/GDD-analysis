import os
import wget
import argparse
import numpy as np
import pandas as pd

import pdb

""" If there is no errors, this function will download and then save a csv file 
    that has the required columns for our further computation and plots.
"""

#Read csv file
def downloadData(startYear, endYear, stationId, cityName):
    while (startYear <= endYear):
        originUrl = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID='
        url = originUrl+str(stationId)+'&Year='+str(startYear)+'&Month=12&Day=31&timeframe=2&submit= Download+Data'
        pdb.set_trace()
        try:
            fileName = wget.download(url) # Download daily historical temperature data for several cities automatically
        except:
            print("Sorry, a problem occured during downloading files,please try it later.")
        try:
            cityData = pd.read_csv(fileName, encoding = 'ISO-8859-1', delimiter = ',', skiprows=25)
        except Exception as e:
            print("There is a problem in reading file name", fileName)
            print(e)

        cols = cityData.columns.values
        for i in range(0,len(cols)):
            # if cols[i].find("Max Temp ("):
            #     cols[i]= "Max Temp"
            # elif cols[i].find("Min Temp ("):
            #     cols[i]= "Min Temp"
            if "Max Temp (" in cols[i]:
                cols[i] = "Max Temp"
            if "Min Temp (" in cols[i]:
                cols[i] = "Min Temp"

        cityData.columns = cols
        csvData = pd.DataFrame(cityData, columns=['Date/Time', 'Max Temp', 'Min Temp'])
        csvData.replace('', np.nan, inplace = True)
        #pdb.set_trace()
        #csvData[csvData['Date/Time']=='2016-02-29'] = np.nan
        csvData = csvData.dropna()
        currPath = os.getcwd()
        filePath= (currPath+'/CSVData/'+cityName+'GDDData.csv')
        startYear += startYear
        os.remove(fileName)
