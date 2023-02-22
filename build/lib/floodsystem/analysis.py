import numpy as np
from matplotlib.dates import date2num
from datetime import datetime


def polyfit(dates, levels, p):
    x = date2num(dates)
    x[0] = d0
    p_coeff = np.polyfit(x - d0, levels, p)"Finds the coefficient for the best fit polynomial of degree p"
    poly = np.poly1d(p_coeff)"Converts the coefficient into a polynomial which can be evaluated"

    return poly, d0 "returns the polynomial object and shift of the time axis as a tuple"


