from matplotlib.dates import date2num
import numpy as np
from datetime import date

from floodsystem.analysis import polyfit

def test_polyfit():
    """For an example set of dates, assert that the level at the date is equal to the level predicted
    by the polyfit function at that point"""
    dates = np.array([
        date(2020, 1, 1),
        date(2020, 1, 4),
        date(2020, 1, 8)
    ])

    levels = np.array([1.1, 7.6, 2.7])

    # a polynomial of order 1 less than the total number of datapoints will pass through them all
    N = len(dates) - 1
    poly, d0 = polyfit(dates, levels, N)

    # iterate through the dates, and compare the actual level to the estimate value from poly
    for i, d in enumerate(dates):
        d_num = date2num(d)
        assert round(levels[i] - poly(d_num - d0), 6) == 0