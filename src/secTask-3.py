import numpy as np
import os
import argparse
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from getCSVData import getCSVData

def drawStJohnsDifferentTBase(tempList):
    key = 0
    color = iter(cm.plasma(np.linspace(0, 1, len(tempList))))
    plt.subplot(1, 1, 1)
    X = np.linspace(1, 12, 365, endpoint=True)
    for i in range(len(tempList)):  # computing GDD for different values of Tbase
        c = next(color)
        GDD = []
        File = (os.getcwd() + '/CSVData/St_JohnsGDDData.csv')
        Data, Date, mx, mn = getCSVData(File)
        Data['GDD' + str(i)] = (Data['Max Temp'] + Data['Min Temp']) / 2 - int(tempList[i])
        for j in Data['GDD' + str(i)]:  # checking the values of GDD
            if j >= 0:
                key += j
            GDD.append(key)
        Data['GDD' + str(i)] = GDD
        T_Base = np.array(Data['GDD' + str(i)])
        plt.plot(X, T_Base, c=c, label='T base = ' + str(tempList[i]))
    plt.legend(loc='upper right')
    ax = plt.gca()

    ax.set_xlabel('MONTHS', fontsize=13)
    ax.set_ylabel('GDD on different T bases (Cumulative)', fontsize=13)  # setting plot
    plt.title("Growing Degree Days in St.John's (Accumulated)", fontsize=14)
    plt.savefig("./plots/secTask-3.png")
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-tl", dest="tempList", nargs='*')
    args = parser.parse_args()
    drawStJohnsDifferentTBase(args.tempList)

    
if __name__ == '__main__':
    Main()