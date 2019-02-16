import os

from glob import glob

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.ndimage import label
from IPython.display import display


_LABEL_MAP = {'normal': 0, 'aggressive_long_accel': 1, 
              'aggressive_turn': 2, 'aggressive_bump': 3}
_COL_NAMES = ['timestamp', 'accel_x', 'accel_y', 
              'accel_z', 'gyro_roll', 'gyro_pitch', 
              'gyro_yaw', 'label']


def load_data(path, col_names, events_names):
    """ 
    Loads the data from a set of CSV files.

    Parameters
    ----------
    path: string
        Path to the directory with the CSV files.

    col_names : list
        List with the column names of the columns that should be loaded.

    events_names: list
        The names of the events that should be loaded.

    Returns
    -------
    Dict
        Dictionary with the dataframe for each event.
    """
    files = sorted(glob(os.path.join(path, '*.csv')))
    data = {signal_name: None for signal_name in events_names}
    
    normal_df = None
    for f in files:
        df = pd.read_csv(f)[col_names]
        
        if 'normal' in f and 'normal' in events_names:
            if data['normal'] is not None:
                data['normal'] = data['normal'].append(df)
            else:
                data['normal'] = df
                
        if 'aggressive_longitudinal_acceleration' in f\
                and 'aggressive_long_accel' in events_names:
            idx = np.nonzero(df['label'].values)[0]
            min_i, max_i = int(idx.min()), int(idx.max())
            if data['aggressive_long_accel'] is not None:
                data['aggressive_long_accel'] = \
                    data['aggressive_long_accel'].append(df[min_i: max_i])
            else:
                data['aggressive_long_accel'] = df[min_i: max_i]
                
        if 'aggressive_turn' in f and 'aggressive_turn' in events_names:
            idx = np.nonzero(df['label'].values)[0]
            min_i, max_i = int(idx.min()), int(idx.max())
            if data['aggressive_turn'] is not None:
                data['aggressive_turn'] = \
                    data['aggressive_turn'].append(df[min_i: max_i])
            else:
                data['aggressive_turn'] = df[min_i: max_i]
                
        if 'aggressive_bump' in f and 'aggressive_bump' in events_names:
            idx = np.nonzero(df['label'].values)[0]
            min_i, max_i = int(idx.min()), int(idx.max())
            if data['aggressive_bump'] is not None:
                data['aggressive_bump'] = \
                    data['aggressive_bump'].append(df[min_i: max_i])
            else:
                data['aggressive_bump'] = df[min_i: max_i]
                
    print('Data loaded with the following shapes:')
    for key, values in data.items():
        print('\t{}: {}.'.format(key, values.shape))
        
    return data


def split_train_val_test(data, percs=(0.7, 0.15, 0.15), 
                         n_points_discard=20):
    """ 
    Splits the data into training, validation, and test.

    Parameters
    ----------
    data: Dict
        Dictionary with the data of each event.

    percs : tuple
        The percentage of the data to consider for each set.

    n_points_discard: int
        Number of points to discard between each set to avoid overlap 
        and data leak.

    Returns
    -------
    Dict
        Dictionary with training dataframes for each event.
    Dict
        Dictionary with validation dataframes for each event.
    Dict
        Dictionary with test dataframes for each event.
    """
    assert np.sum(percs) == 1
    assert len(percs) == 3
    train, val, test = {}, {}, {}
    
    for key, values in data.items():
        n_samples = values.shape[0]
        
        lower_lim = 0
        top_lim = n_samples * percs[0]
        train[key] = values[lower_lim: int(top_lim - n_points_discard)]
        
        lower_lim = top_lim + n_points_discard
        top_lim = top_lim + n_samples * percs[1]
        val[key] = values[int(lower_lim): int(top_lim - n_points_discard)]
        
        lower_lim = top_lim + n_points_discard
        top_lim = top_lim + n_samples * percs[2]
        test[key] = values[int(lower_lim): int(top_lim - n_points_discard)]
        
        print('\nNumber of points in {}:'.format(key))
        print('Train: {}.'.format(train[key].shape[0]))
        print('Validation: {}.'.format(val[key].shape[0]))
        print('Test: {}.'.format(test[key].shape[0]))
        
        if key != 'normal':
            print('Number of aggressive events:')
            _, n_labels = label(train[key]['label'].values)
            print('\tTrain: {}.'.format(n_labels))
            _, n_labels = label(val[key]['label'].values)
            print('\tValidation: {}.'.format(n_labels))
            _, n_labels = label(test[key]['label'].values)
            print('\tTest: {}.'.format(n_labels))
        
    return train, val, test


def join_data(dataframes_dict, signal_columns, label_column):
    """ 
    Joins the data of all events into a single dataframe and array of labels.

    Parameters
    ----------
    dataframes_dict: Dict
        Dictionary with the dataframes of the data each event in a given set.

    signal_columns : list
        List of strings of the columns names to keep.

    label_column: string
        The name of the column with the labels.

    Returns
    -------
    pandas dataframe
        Dataframe with the signals of all types of events appended.
    numpy array
        The array with the labels of each row of the data. The label number 
        is defined by _LABEL_MAP
    """
    for i, (key, values) in enumerate(dataframes_dict.items()):
        if i == 0:
            join_X = values[signal_columns]
            join_y = np.zeros(values.shape[0]) \
                     + _LABEL_MAP[key] * values[label_column]
        else:
            join_X = join_X.append(values[signal_columns])
            join_y = np.append(join_y, 
                               np.zeros(values.shape[0]) + \
                               _LABEL_MAP[key] * values[label_column],
                               axis=0)
            
    return join_X, join_y


def events_size(manual_labels, bins=60):
    """ 
    Plots the histogram of the size of the events (number of points) of the 
    events.

    Parameters
    ----------
    manual_labels: numpy array
        The array with labels. Note that this labels should be binary. 
        E.g. the array with labels only for harsh acceleration.

    bins : int
        Number of bins of the histogram.
    """
    labeled_array, n_labels = label(manual_labels)
    sizes = np.zeros(n_labels)
    
    for i in range(1, n_labels + 1):
        sizes[i - 1] = np.count_nonzero(labeled_array == i)
        
    plt.hist(sizes, bins=bins)
    plt.ylabel('Number of events.')
    plt.xlabel('Number of points of event.')
    plt.show()


class DummyPreProcessing:
    """This is an example of how to define a data transform class to be 
    integrated into sklearn's pipeline.

    In this example, it just returns the data as is, for demonstrations 
    purposes.
    
    This class must have 3 methods: transform, fit, and fir transform.
    """
    def transform(self, X, y=None):
        """Transforms the data. This method only makes sense after calling 
        the fit method.

        Parameters
        ----------
        X: numpy array
            The array with features. Rows are the samples and columns the 
            features..

        y : numpy
            The array of labels. Most of the time it is not necessary at 
            pre-processing time.

        Returns
        -------
        numpy array
            Array of shape [1, n_features] with the computed features.
        """
        return X
    
    def fit(self, X, y=None):
        """Estimates the parameters of the pre-processing.

        Parameters
        ----------
        X: numpy array
            The array with features. Rows are the samples and columns the 
            features.

        y : numpy
            The array of labels. Most of the time it is not necessary at 
            pre-processing time.
        """
        pass
    
    def fit_transform(self, X, y=None):
        """Estimates the parameters of the pre-processing and applies it to 
        the data. This may be handy at training time.

        Parameters
        ----------
        X: numpy array
            The array with features. Rows are the samples and columns the 
            features..

        y : numpy
            The array of labels. Most of the time it is not necessary at 
            pre-processing time.

        Returns
        -------
        numpy array
            Array of shape [1, n_features] with the computed features.
        """
        self.fit(X=X, y=y)
        return self.transform(X=X, y=y)


def general_report(results):
    """ 
    Prints the metrics for the given datasets and classifiers.

    Parameters
    ----------
    results: Dictionary
        Dict of dicts with the metrics. Keys are the names of the datasets. 
        Then, for each dataset there is another dictionary where keys are the 
        classifiers and this dict has the metrics.
    """
    for set_key, set_values in results.items():
        print('\n{}'.format(set_key))
        df = pd.DataFrame.from_dict(results[set_key]).T
        display(df)
