import os
import pdb
import csv
import collections
import pdb
'''making CSV file to and store them on the disk'''

def saveCSVData(csv_data, file_directory):
    # with open(csv_data, 'rb') as f:
    #     data = list(csv.reader(f)
    # counter = collections.defaultdict(int)
    # for row in data:
    #     counter[row[0]] += 1
    #
    # writer = csv.writer(open(file_directory, 'w'))
    # for row in data:
    #     if counter[row[0]] >= len(csv_data):
    #         writer.writerow(row)

    if not os.path.exists(file_directory):
        try:
            os.makedirs(file_directory)# Check if there is no directory in that path, we shoould make it
        except:
            print("Oops! there is problem during making dirctory, please try later.")
    with open(file_directory, 'w') as datafile:
        csv_data.to_csv(file_directory, sep=',')

    with open('thefile.csv', 'rb') as f:
        data = list(csv.reader(f))


