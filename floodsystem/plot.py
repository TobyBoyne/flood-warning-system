import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime

from floodsystem.analysis import polyfit

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