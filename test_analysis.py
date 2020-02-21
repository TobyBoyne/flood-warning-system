import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np
from datetime import date

from floodsystem.analysis import polyfit

def test_polyfit():
    dates = np.array([
        date(2020, 1, 2),
        date(2020, 1, 5),
        date(2020, 1, 8),
        date(2020, 1, 14)
    ])

    levels = np.array([2.5, 2, 1.7, 9])

    poly, d0 = polyfit(dates, levels, 5)

    start_time = date2num(date(2020, 1, 1))
    xs = np.linspace(start_time, start_time + 15, 150)
    print(xs - d0)
    ys = poly(xs - d0)

    plt.plot(xs - d0, ys)
    plt.show()

test_polyfit()