import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

def run():
    number_stations = 5
    dt = 2
    p =4