import pandas as pd
import numpy as np

def hours_of_daylight(date, axis=23.44, latitude=47.61):
    """Compute the hours of daylight for the given date"""
    diff = date - pd.datetime(2000, 12, 21)
    day = diff.total_seconds() / 24. / 3600
    day %= 365.25
    m = 1. - np.tan(np.radians(latitude)) * np.tan(np.radians(axis) * np.cos(day * np.pi / 182.625))
    m = max(0, min(m, 2))
    return 24. * np.degrees(np.arccos(1 - m)) / 180.


def print_rms(var):
	"""Calculates and prints the root-mean-square about the trend line"""
	rms = np.std(var)
	print('Root-mean-square about trend: {0: .0f} riders'.format(rms))

def csnap(df, fn=lambda x: x.shape, msg=None):
    """ 
    Custom Help function to print things in method chaining.
    Returns back the df to further use in chaining.
    """
    if msg:
        print(msg)
    display(fn(df))
    return df