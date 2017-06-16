import sys
import pandas as pd

from downloadData import downloadRawData
from saveCSVData import saveCSVData
from computeGDD import computeGDDFile, computeGDDAccumulatedFile


def downloadSave:
	stations = pd.read_csv('Station_Inventory_EN.csv', usecols=['Name', 'Station ID', 'Latitude (Decimal Degrees)','Longitude (Decimal Degrees)'], skiprows=3)
	baseTemp = 10
	raw_data = {'Station': [], 'City': [], 'Lat': [], 'Lon': [], 'Gdd': []}
	locations = [];

	for index, row in stations.iterrows():
		if index > -1:
			downloadRawData(2016, 2016, row[1], row[0])
			computeGDDFile(row[0], row[1], baseTemp)


def generateHeatmapFile:
	stations = pd.read_csv('Station_Inventory_EN.csv', usecols=['Name', 'Station ID', 'Latitude (Decimal Degrees)','Longitude (Decimal Degrees)'], skiprows=3)
	baseTemp = 10
	raw_data = {'Station': [], 'City': [], 'Lat': [], 'Lon': [], 'Gdd': []}
	locations = [];

	for index, row in stations.iterrows():
		if index > -1:
			gdd = round(computeGDDAccumulatedFile(row[0], row[1], baseTemp), 0)
			if gdd > 100:
				raw_data['Station'].append(row[1])
				raw_data['City'].append(row[0])
				raw_data['Lat'].append(row[2])
				raw_data['Lon'].append(row[3])
				raw_data['Gdd'].append(gdd)

	df = pd.DataFrame(raw_data, columns = ['Station', 'City', 'Lat', 'Lon', 'Gdd'])
	df.to_csv('CSVData/_heatmap.csv', index=False)
	df.to_json('CSVData/_heatmap.json')
