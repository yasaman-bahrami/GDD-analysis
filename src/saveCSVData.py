import os
import pdb

# Save the Data as a .csv file into given file path
def saveCSVData(Data, filepath):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except:
            print("Something happen, try later")
    with open(filepath, 'w') as datafile:
        Data.to_csv(filepath, sep=',')
