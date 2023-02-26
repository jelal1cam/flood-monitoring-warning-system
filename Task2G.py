from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
from matplotlib.dates import date2num

import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    risk_level_severe = []
    risk_level_high = []
    risk_level_moderate = []
    risk_level_low = []
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2))
        today = date2num(dates)
        poly, d0 = polyfit(dates, levels, 4)

        #print(d0)

        x = np.linspace(today - 2, today, 1000)
        #y = poly(x - d0)
        y = poly(x)

        gradient = np.gradient(y)
        print(gradient)

        '''if station.relative_water_level() >= 1:
            risk_level_severe.append(station.town)
        elif station.relative_water_level() > 0.8 and gradient[-1][-1][-1] >0:
            risk_level_high.append(station.town)
        elif station.relative_water_level() > 0.8 :
            risk_level_moderate.append(station.town)
        elif station.relative_water_level()<0.8:
            risk_level_low.append(station.town)
            
    return risk_level_severe, risk_level_high, risk_level_moderate, risk_level_low'''

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

    