import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime, timedelta

try:
    from .analysis import polyfit  # noqa
except ImportError:
    from analysis import polyfit

def plot_water_levels(station, dates, levels):
    "Displays a plot of the water levels as a function of time for a station, also includes typical high and low water levels"
    low = station.typical_range[0]
    high = station.typical_range[1]

    plt.plot(dates, levels)
    plt.axhline(low, linestyle = "dashed", c ="red")
    plt.axhline(high, linestyle = "dashed", c = "yellow")
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)


    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots a graph of dates against time on the current figure
    Note that this DOES NOT show the figure - must call plt.plot() after this function
    This allows for data to be added to the plot after this function is called"""
    today = date2num(dates[0])
    poly, d0 = polyfit(dates, levels, p)

    xs = np.linspace(today - 2, today, 1000)
    ys = poly(xs - d0)

    plt.plot(xs - d0, ys)

    plt.title(station.name)
    plt.xlim(-2, 0)
    plt.xlabel("Days since last reading")
    plt.ylabel("water level (m)")