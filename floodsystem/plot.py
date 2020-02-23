import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime, timedelta

from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Displays a plot of the water level data against time for a station, including
    plot lines for typical low and high levels"""
    low = station.typical_range[0]
    high = station.typical_range[1]

    plt.plot(dates, levels)

    plt.axhline(station.typical_range[0], linestyle="dashed", color="green")
    plt.axhline(station.typical_range[1], linestyle="dashed", color="red")

    plt.legend(("Water level", "Typical low", "Typical high"))
    plt.xlabel("Dates")
    plt.ylabel("Water level data (m)")
    plt.title(station.name + " Water Level")
    plt.xticks(rotation=45)

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

    plt.title(station.name + " Water Level")
    plt.xlim(-2, 0)
    plt.xlabel("Time until last reading (days)")
    plt.ylabel("Level measurement")