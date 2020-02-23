from matplotlib.dates import date2num
import numpy as np
from datetime import datetime

def polyfit(dates, levels, p):
    """Calculate the polynomial of order p that passes through the data points
    Returns a poly1d object, and the time axis offset"""
    date_nums = date2num(dates)
    # d0 is the shift of the time axis - first date
    d0 = date_nums[0]

    p_coeff = np.polyfit(date_nums - d0, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0

def projected_level_after_dt(dates, levels, dt=1):
    """Draws a straight line of best fit to estimate trend
    Then finds the projected value of that trend after dt days.
    dates is sorted in most-recent-first order"""
    best_fit, d0 = polyfit(dates, levels, 1)
    projected_level = best_fit(dt)

    return projected_level