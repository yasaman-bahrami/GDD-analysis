import numpy
import os
import pandas
import sys

sys.path.append('../')
from getCSVData import getCSVData

def testGetCSVData():
    cityName = 'Toronto'
    
    try:
        FilePath= ('CSVData/'+cityName+'GDDData.csv')
        a, b, c, d= getCSVData(FilePath)
        FileData = pandas.read_csv(FilePath, encoding = 'ISO-8859-1', delimiter = ',' ,skiprows=0)
        Data = pandas.DataFrame(FileData)
        Data.replace('', numpy.nan, inplace = True)
        Data = Data.dropna()
        Index = Data.keys()
        Date, maxTemp, minTemp = numpy.array(Data[Index[1]]),numpy.array(Data[Index[2]]), numpy.array(Data[Index[3]])
    
        if b.all() != Date.all() or c.all() != maxTemp.all() or d.all() != minTemp.all():
            raise ValueError("Data is corrupted! TEST FAILED")
        else:
            print ("CSV Data extraction TEST PASSED")
    except:
        print (cityName + " File is not availble TEST FAILED")
       
testGetCSVData()
