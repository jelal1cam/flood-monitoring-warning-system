import matplotlib.pyplot as plt
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_rel_water_level_stations = stations_highest_rel_level(stations, 5)

    for station in highest_rel_water_level_stations:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=10))
        plot_water_levels(station[0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()