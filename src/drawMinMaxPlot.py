import numpy as np
import matplotlib.pyplot as plt


def drawMinMaxPlot(mn, mx, cityName):
    mnLen = len(mn)
    min_space = np.linspace(1, mnLen, mnLen)
    mxLen = len(mx)
    max_space = np.linspace(1, mxLen, mxLen)
    plt.subplot(1, 1, 1)
    plt.grid(True)
    plt.plot(min_space, mn, color="blue", label="Min Temperature")
    plt.plot(max_space, mx, color="red", label="Max Temperature")
    plt.legend(loc='upper right')
    ax = plt.gca()
    plt.title('Min and Max Temperatures in 2015 for ' + cityName, color="black", fontsize=14)  # *******
    ax.set_axis_bgcolor('yellow')
    ax.set_xlabel('Days', fontsize=11)
    ax.set_ylabel('Temperature', fontsize=11)

    return plt

#----------------------------Main------------------------------
def Main():
        Max_Min_Plot = drawMinMaxPlot()


if __name__ == '__main__':
    Main()
