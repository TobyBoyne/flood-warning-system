import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime

from floodsystem.analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):
    today = date2num(datetime(2020, 1, 29, 8))

    poly, d0 = polyfit(dates, levels, p)

    xs = np.linspace(today - 2, today, 1000)
    ys = poly(xs - d0)

    plt.plot(xs - d0, ys)
    plt.title(station.name + " Water Level")
    plt.show()