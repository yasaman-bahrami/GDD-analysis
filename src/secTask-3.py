import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from getCSVData import getCSVData

list_t = [10, 12, 14, 16, 18]  # Tbase values


def Main():
    key = 0
    color = iter(cm.plasma(np.linspace(0, 1, len(list_t))))
    plt.subplot(1, 1, 1)
    X = np.linspace(1, 12, 365, endpoint=True)
    for i in range(len(list_t)):  # computing GDD for different values of Tbase
        c = next(color)
        GDD = []
        Path = os.getcwd()
        File = '{}/CSVData/St_JohnsGDDData.csv'.format(Path)
        Data, Date, mx, mn = getCSVData(File)
        Data['GDD' + str(i)] = (Data['Max Temp'] + Data['Min Temp']) / 2 - list_t[i]
        for j in Data['GDD' + str(i)]:  # checking the values of GDD
            if j >= 0:
                key += j
            GDD.append(key)
        Data['GDD' + str(i)] = GDD
        T_Base = np.array(Data['GDD' + str(i)])

        plt.plot(X, T_Base, c=c, label='T base = ' + str(list_t[i]))
    plt.legend(loc='upper right')
    ax = plt.gca()

    ax.set_xlabel('MONTHS', fontsize=13)
    ax.set_ylabel('GDD on different T bases (Cumulative)', fontsize=13)  # setting plot
    plt.title("Growing Degree Days in St.John's (Accumulated)", fontsize=14)
    plt.savefig("./plots/secTask-3.png")


if __name__ == '__main__':
    Main()