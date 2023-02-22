import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

def run():
    N = 5
    DT = 2
    P = 4

    stations = build_station_list()
    update_water_levels(stations)
    at_risk_stations = stations_highest_rel_level(stations, N)

    for station in at_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=DT))

        # plot real data
        date_nums = date2num(dates) - date2num(dates[0])
        plt.plot(date_nums, levels, color="orange")

        # plot line of best fit
        plot_water_level_with_fit(station, dates, levels, P)

        # plot high/low
        plt.axhline(station.typical_range[0], linestyle="dashed", color="green")
        plt.axhline(station.typical_range[1], linestyle="dashed", color="red")

        plt.legend(("Real values", "Best fit", "Typical low", "Typical high"))

        plt.show()



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()