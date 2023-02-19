import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    "Displays a plot of the water levels as a function of time for a station, also includes typical high and low water levels"
    low = station.typical_range[0]
    high = station.typical_range[1]

    plt.plot(dates, levels)
    plt.axhline(low, linestyle = "-", c ="red")
    plt.axhline(high, linestyle = "-", c = "yellow")
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()