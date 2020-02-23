from matplotlib.dates import date2num
import numpy as np
from datetime import date, datetime

from floodsystem.analysis import polyfit, projected_level_after_dt

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


def test_projected_level_after_dt():
    """For an example set of ordered dates (most-recent-first), assert that the projected values are correct"""
    dates = np.array([
        datetime(2020, 1, 1, 5),
        datetime(2020, 1, 1, 4),
        datetime(2020, 1, 1, 2)
    ])

    levels = np.array([4, 3, 1])

    # after 0 days, the water level should be equal to most recent result
    assert round(projected_level_after_dt(dates, levels, 0) - levels[0], 6) == 0

    # after 1 hour, the water level will rise to a value of 5 if the trend continues
    dt = 1 / 24
    assert round(projected_level_after_dt(dates, levels, dt) - 5, 6) == 0