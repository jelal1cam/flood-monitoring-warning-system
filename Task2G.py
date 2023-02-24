from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import risk_allocation_town

import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    risk_level = risk_allocation_town(stations, 20)
    for town, risk in risk_level:
        print(town + ": " + risk)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

    