import numpy as np


def get_mean(array, axis=None):
    """ 
    Computes the mean of an array, along a given axis.

    Parameters
    ----------
    array: numpy array
        The array over which the operation will be done.

    axis : None, int
        Axis along which the operation will be done.

    Returns
    -------
    numpy array
        The array after the computing operation.
    """
    return np.mean(array, axis=axis)


def get_min(array, axis=None):
    """ 
    Computes the minimum of an array, along a given axis.

    Parameters
    ----------
    array: numpy array
        The array over which the operation will be done.

    axis : None, int
        Axis along which the operation will be done.

    Returns
    -------
    numpy array
        The array after the computing operation.
    """
    return np.min(array, axis=axis)


def get_max(array, axis=None):
    """ 
    Computes the maximum of an array, along a given axis.

    Parameters
    ----------
    array: numpy array
        The array over which the operation will be done.

    axis : None, int
        Axis along which the operation will be done.

    Returns
    -------
    numpy array
        The array after the computing operation.
    """
    return np.max(array, axis=axis)


def get_std(array, axis=None):
    """ 
    Computes the standard deviation of an array, along a 
    given axis.

    Parameters
    ----------
    array: numpy array
        The array over which the operation will be done.

    axis : None, int
        Axis along which the operation will be done.

    Returns
    -------
    numpy array
        The array after the computing operation.
    """
    return np.std(array, axis=axis)


def get_range(array, axis=None):
    """ 
    Computes the range of an array, along a given axis.

    Parameters
    ----------
    array: numpy array
        The array over which the operation will be done.

    axis : None, int
        Axis along which the operation will be done.

    Returns
    -------
    numpy array
        The array after the computing operation.
    """
    return array.max(axis=axis) - np.abs(array.min(axis=axis))


def get_quantile(array, quantile, axis=None):
    """ 
    Computes the value of a given quantile of an array, 
    along a given axis.

    Parameters
    ----------
    array: numpy array
        The array over which the operation will be done.

    axis : None, int
        Axis along which the operation will be done.

    Returns
    -------
    numpy array
        The array after the computing operation.
    """
    return np.quantile(array, q=quantile, axis=axis)


def get_window_lims(window_size):
    """Computes the limits of the window.

    This is half of the window size, and it differs if the
    window size is odd or pair.

    Parameters
    ----------
    window_size : int
        The size of the window, i.e., the number of samples
        that it considers.

    Returns
    -------
    int
        Considering the window is centered on the point,
        how many elements to consider backwards.
    int
        Considering the window is centered on the point,
        how many elements to consider forward.
    """
    if window_size % 2 == 0:
        w_min, w_max = int(window_size / 2), int(window_size / 2)
    else:
        w_min, w_max = int(window_size / 2), int(window_size / 2) + 1
        
    return w_min, w_max


def get_features(signals, labels, window_size, 
                 feature_list, idx,
                 label_pos='center'):
    """Computes the features.

    Given an array of indexes where windows should be extracted, and a
    list of functions for computing features, returns the features
    for all the selected samples.

    Parameters
    ----------
    signals : numpy array
        Array with shape [n_signal_points, n_signals] with the signals
        of interest acquisitions.
    labels: numpy array
        Array of shape [n_signal_points] with the labels of the event
        of interest, where 0 is non-event and 1 is event.
    window_size: int
        The size of the considered window.
    feature_list: list
        A list of functions, where each function computes one feature.
        The function is expected to receive an array of shape
        [n_selected_windows, window_size].
    idx: numpy array
        Array with the index of the signal samples around which the
        window will be extracted.
    label_pos: string
        The point from which to extract the label. If center, it is the point
        in the middle of the window. Otherwise, with end it is the last
        point.

    Returns
    -------
    numpy array
        2D array with shape [n_samples, n_features] with the features.
    numpy array
        The array with the label of the samples.
    """
    assert label_pos in ('center', 'end')
    
    n_samples = idx.size
    
    n_features = len(feature_list)
    n_signals = signals.shape[1]
    feats = np.zeros((n_samples, n_features * n_signals))
    y = np.zeros(n_samples, dtype=np.int)
    
    w_min, w_max = get_window_lims(window_size=window_size)
    if label_pos == 'center':
        pad = int(np.max([w_min, w_max]))
    else:
        pad = window_size
    idx = idx + pad
    
    pad_labels = np.pad(labels.copy(), pad, 'constant', 
                        constant_values=0)
    
    for signal_i in range(signals.shape[1]):
        signal_windows = np.zeros((n_samples, window_size))
        signal = signals[:, signal_i]
        signal = np.pad(signal, pad, mode='reflect')
        
        for i in range(n_samples):
            if label_pos == 'center':
                y[i] = pad_labels[idx[i]]
                signal_windows[i, :] = \
                    signal[idx[i] - w_min: idx[i] + w_max]
            else:
                y[i] = pad_labels[idx[i]]
                signal_windows[i, :] = \
                    signal[idx[i] - window_size + 1: idx[i] + 1]
        
        # vectorized computation
        for feature_i, feature in enumerate(feature_list):
            feats[:, signal_i * n_features + feature_i] = \
                feature(array=signal_windows, axis=1)
            
    return feats, y