import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.io import show

from sklearn.metrics import (precision_recall_curve,
                             average_precision_score)
from sklearn.utils.fixes import signature


def plot_signals(dataframe, columns):
    """Plots the signals.

    Parameters
    ----------
    dataframe : pandas dataframe
        The dataframe with the signals. Rows represent samples/points and 
        the columns are the signals.

    columns: list
        List of strings with the name of the signals that will be plotted.
    """
    figs = []
    for i, col in enumerate(columns):
        if i == 0:
            s = figure(plot_width=250, plot_height=250, title=col)
        else:
            s = figure(plot_width=250, plot_height=250, title=col, 
                       x_range=s.x_range)
        s.line(np.arange(dataframe.shape[0]), dataframe[col].values)
        figs.append(s)
        
    p = gridplot([figs[:3], figs[3:]])
    show(p)


def pair_plot(data, label, var_columns, figsize=None):
    """Plots variables in pairs for pair plots.

    Parameters
    ----------
    data : pandas dataframe
        The dataframe with the data. Rows represent samples/points and 
        the columns are the variables/signals/features.

    label: numpy array
        The array with the label of each sample.

    var_columns: list
        List with the names of the variables to plot, which are the names
        of the columns of the dataframe.

    figsize: None, tuple
        Size of the plots figure.
    """
    plt.figure(figsize=figsize)
    tmp = data
    tmp['label'] = label
    sns.pairplot(tmp, vars=var_columns, hue='label')
    plt.show()


def precision_recall_plot(prediction_prob, y, figsize=(15, 7)):
    """Plots a precision-recall curve.

    Parameters
    ----------
    prediction_prob: numpy array
        The classifier's predicted probabilities.

    y: numpy array
        The real labels of the samples.

    figsize: None, tuple
        Size of the plots figure.
    """
    precision, recall, thresholds = precision_recall_curve(y, prediction_prob)

    average_precision = average_precision_score(y, prediction_prob)
    
    plt.figure(figsize=figsize)
    step_kwargs = ({'step': 'post'}
                   if 'step' in signature(plt.fill_between).parameters
                   else {})
    plt.step(recall, precision, color='b', alpha=0.2,
             where='post')
    plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
              average_precision))


def plot_rf_pipe_feature_importance(rf_pipe, signal_names, 
                                    feature_names, rf_name='rf',
                                    figsize=(8, 8)):
    """Plots a Random Forest's feature importance.

    Parameters
    ----------
    rf_pipe: sklearn pipeline's instance
        The sklearn's classification pipeline that includes a RF.

    signal_names: list
        A list with the signal's names that are being considered for 
        computing features.

    feature_names: list
        A list with the name of the features.

    rf_name: string
        The name of the random forest instance in the pipeline.

    figsize: None, tuple
        Size of the plots figure.
    """
    names = []
    for signal_name in signal_names:
        for feature_name in feature_names:
            names.append('{} {}'.format(signal_name, 
                                        feature_name))
            
    feat_importances = \
        rf_pipe.get_params(rf_name)[rf_name].feature_importances_
    sort_ind = np.argsort(feat_importances)
    sort_names = [names[i] for i in sort_ind]
    
    plt.figure(figsize=figsize)
    plt.title("RF feature importances")
    plt.barh(range(feat_importances.shape[0]), feat_importances[sort_ind],
             color="r", align="center")

    plt.yticks(range(feat_importances.shape[0]), sort_names)
    plt.xlabel('Feature importance')
    plt.ylabel('Features')
    plt.show()

