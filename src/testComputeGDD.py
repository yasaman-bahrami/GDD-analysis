import numpy
import pandas
import sys
from nose.tools import assert_equal

sys.path.append('../')
from computeGDD import computeGDD

def testComputeGDD():
    baseTemp = 10
    sampleData = {'Max Temp' : pandas.Series([20, 18, 16, 14, 22, 24, 26]), 'Min Temp' : pandas.Series([10,  8,  6,  4, 12, 16, 18])}
    sampleDataFrame = pandas.DataFrame(sampleData)
    sampleGDD = computeGDD(sampleDataFrame, baseTemp)
    sampleGDDArray = numpy.array(sampleGDD['GDD'])
    sampleGDDList = list(sampleGDDArray)
    
    expectedGDDList = [5.0, 9.0, 12.0, 14.0, 21.0, 31.0, 43.0]
    
    try:
        assert_equal(sampleGDDList, expectedGDDList, "#1 Test Failed! GDD values are not corerct!" )
        print ('#1 Test Passed! GDD values are corerct!')
    except:
        print ('#1 Test Failed! GDD values are not corerct!')

    expectedGDDList = [0, 9.0, 12.0, 14.0, 21.0, 31.0, 43.0]
    
    try:
        assert_equal(sampleGDDList, expectedGDDList, "#2 Test Failed! GDD values are not corerct!" )
        print ('#2 Test Passed! GDD values are corerct!')
    except:
        print ('#2 Test Failed! GDD values are not corerct!')


testComputeGDD()