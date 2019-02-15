import numpy as np


def get_mean(array, axis=None):
    return np.mean(array, axis=axis)

def get_min(array, axis=None):
    return np.min(array, axis=axis)

def get_max(array, axis=None):
    return np.max(array, axis=axis)

def get_std(array, axis=None):
    return np.std(array, axis=axis)

def get_range(array, axis=None):
    return array.max(axis=axis) - np.abs(array.min(axis=axis))

def get_quantile(array, quantile, axis=None):
    return np.quantile(array, q=quantile, axis=axis)

def get_window_lims(window_size):
    if window_size % 2 == 0:
        w_min, w_max = int(window_size / 2), int(window_size / 2)
    else:
        w_min, w_max = int(window_size / 2), int(window_size / 2) + 1
        
    return w_min, w_max
    