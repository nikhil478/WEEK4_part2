import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
birddata = pd.read_csv("bird_tracking.csv")
birddata.info() #to get info
birddata.head() #top5
birddata.tail() #last5
bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize = (7,7))
for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x,y = birddata.longitude[ix],birddata.latitude[ix]
    plt.plot(x,y,".",label = bird_name)
plt.xlabel("longitude")
plt.ylabel("latitude");
plt.legend(loc = "lower right")
#examinig flight speed
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
plt.hist(speed)
#############______DEBBUG_____#######
plt.hist(speed[:10])
# checking non objects by np.isnan
np.isnan(speed)
np.isnan(speed).any()
# how many nan 
np.sum(np.isnan(speed))
# reamking the previous progra btn removing nan objects
ind = np.isnan(speed)
~ind # it changes true to false and false to true
ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
plt.hist(speed[~ind], bins = np.linspace(0,30,20),density = True)
# hiatogram plotoing by using pandas
birddata.speed_2d.plot(kind = "hist", range= [0,30])
plt.xlabel("2d speed");
plt.savefig("pd_hist.pdf")
# using datatime
birddata.columns
date_str = birddata.date_time[0] 
datetime.datetime.strptime(date_str[:-3],"%Y-%m-%d %H:%M:%S")
# now we are making timessams list
timestams = []
for k in range(len(birddata)):
    timestams.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3],"%Y-%m-%d %H:%M:%S"))
        
# dont write answer of that question 2013-8-15 0:18:08
 
# creating a new column by using pandas
birddata["timestams"] = pd.Series(timestams, index = birddata.index)
times = birddata.timestams[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]
# now ploting a graph  x - no of observation and on y axis the amount of time elpased in hours
plt.plot(np.array(elapsed_time) / datetime.timedelta(days = 1))
plt.xlabel("no of observation")
plt.ylabel("no of days")
plt.savefig("hfdu.pdf")
#  calculating daily mean speed

data = birddata[birddata.bird_name == "Eric"]
times = data.timestams
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days = 1)
next_day = 1
inds = []
daily_mean_speed = []
for (i,t) in enumerate(elapsed_time):
    if t < next_day:
        inds.append[i]
    else:
        #compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d(inds)))
        next_day += 1
        inds = []
        
plt.figure(figsize = (7,8))
plt.plot(daily_mean_speed)
plt.xlabel("day")
plt.ylabel("mean speed (m/s)")
plt.savefig("fig.pdf")        

# installing cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
proj = ccrs.Mercator()
plt.figure(figsize = (8,8))
ax = plt.axes(projection = proj)
ax.set_extent((-25.0,20.0,52.0,10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS , linestyle = ":")
for name in bird_names:
    ix = birddata["bird_name"] == name
    x,y = birddata.longitude[ix] , birddata.latitude[ix]
    ax.plot(x,y, ".", transform = ccrs.Geodetic(),label = name) 

plt.legend(loc = "upper left")
plt.savefig("map.pdf")



#######HOMEWORK################################################################################################################################################################################################################################################################################################################################################################################################

    
#1
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv" , index_col = 0)
grouped_birds = birddata.groupby("bird_name")
mean_speeds = grouped_birds.speed_2d.mean()
mean_altitudes = grouped_birds.altitude.mean()

#2
birddata.date_time = pd.to_datetime(birddata.date_time)
birddata["date"] =  birddata.date_time.dt.date
grouped_bydates = birddata.groupby("date")
mean_altitudes_perday = grouped_bydates.altitude.mean()
  

#3
grouped_birdday = birddata.groupby(["bird_name","date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()
mean_altitudes_perday.head()

#4
import matplotlib.pyplot as plt

eric_daily_speed = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]
nico_daily_speed = grouped_birdday.speed_2d.mean()["Nico"]

eric_daily_speed.plot(label = "Eric")
sanne_daily_speed.plot(label = "Sanne")
nico_daily_speed.plot(label = "Nico")

plt.legend(loc = "upper left")
plt.show()



