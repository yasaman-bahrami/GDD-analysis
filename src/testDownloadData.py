import sys
import pandas

sys.path.append('../')
from downloadData import downloadData
from saveCSVData import saveCSVData

def testDownloadData():
    startYear=2016
    endYear=2016
    stationId=51459
    cityName='Toronto'
        
    downloadData(startYear, endYear, stationId, cityName)
    try:
        File_Data = pandas.read_csv('CSVData/'+cityName+'GDDData.csv')
        print("Download CSV file TEST PASSED")
    except:
        raise ValueError(cityName+" file is not downloaded or is not a valid csv! TEST FAILED")

testDownloadData()
