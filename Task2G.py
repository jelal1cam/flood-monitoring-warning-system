from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from matplotlib.dates import date2num
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations_over_threshold = stations_level_over_threshold(stations, 0.8)#only includes stations with a relative water level over 0.8 to prevent the task taking too long 
    severe_risk =[]
    high_risk = []
    moderate_risk = []
    low_risk = []
    #places each station in a category depending on rel water level over past 2 days
    for station in stations_over_threshold:
        dates, levels = fetch_measure_levels(station[0].measure_id, datetime.timedelta(days=2))
        today = date2num(dates[0])
        p = 4
        poly, p_coeff, d0 = polyfit(dates, levels, p)

        x = np.linspace(today - 2, today, 1000)
        y = poly(x - d0)

        if station[1] > 1:
            severe_risk.append(station[0].town)
        elif 0.8 < station[1] <= 1 and np.gradient(y)[-1] > 0: #gradient used to determine risk
            high_risk.append(station[0].town)
        elif 0.8 < station[1] <= 1:
            moderate_risk.append(station[0].town)
        else:
            low_risk.append(station[0].town)

    print("severe risk: ", severe_risk) #print the severe and high risk towns
    print("high risk:", high_risk)

if __name__ == "__main__":

    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()

    