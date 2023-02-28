import numpy as np
from matplotlib.dates import date2num
from datetime import datetime


def polyfit(dates, levels, p):
    x = date2num(dates)
    d0 = x[0]
    p_coeff = np.polyfit(x - d0, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, p_coeff, d0



