from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
"""m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)"""
m = Basemap(width=8000000,height=6500000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.shadedrelief()

meridians = np.arange(-180.,181.,10.)
parallels = np.arange(-90.,91.,5.)
# Label the meridians and parallels
m.drawparallels(parallels,labels=[True,False,False,False])
m.drawmeridians(meridians,labels=[True,False,False,True])
lon = []
lat = []
gdd = []

with open("_heatmap.csv") as f:
    for line in f:
        cur_line = line.strip().split(',')
        lat.append(float(cur_line[2]))
        lon.append(float(cur_line[3]))
        #day_out.append(float(cur_line[2]))
        gdd.append(float(cur_line[4]))


plt.title("Canada GDD 2016 ")
# Define a colormap
jet = plt.cm.get_cmap('jet')
# Transform points into Map's projection
x,y = m(lon, lat)
# Color the transformed points!
sc = plt.scatter(x,y, c=gdd, vmin=600, vmax =1800, cmap=jet, s=20, edgecolors='none')
# And let's include that colorbar
cbar = plt.colorbar(sc, shrink = 0.5)
cbar.set_label('temp')
plt.show()