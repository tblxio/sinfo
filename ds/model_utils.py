import numpy as np
import pandas as pd

from sklearn.metrics import (make_scorer, f1_score, precision_score, 
                             recall_score, confusion_matrix)
from sklearn.model_selection import RandomizedSearchCV


def randomized_hyperparameter_search(X_train, y_train, X_val, y_val, 
                                     pipeline, params, n_iter, 
                                     score_func, n_jobs, seed):
    """ 
    Performs Randomized Search over the hyperparameters of a pipeline.
    Then, chooses the best parameters and trains the pipeline in the
    complete training set.

    Parameters
    ----------
    X_train: numpy array
        The training set in the form [n_train_samples, n_features].

    y_train: numpy array
        The true labels of the training set.
        
    X_train: column of Dataframe
        The validation set in the form [n_val_samples, n_features].

    y_val: numpy array
        The true labels of the validation set.
        
    pipeline: instantiated Pipeline
        The ML pipeline.
        
    params: dict
        The parameters and ranges.
        
    n_iter: int
        The number of iterations.
        
    score_func: function
        The function that computes the metric to be optimized.
        
    n_jobs: int
        The number of parallel jobs.
        
    seed: int
        The random seed.

    Returns
    -------
    pipeline: sklearn Pipeline
        The pipeline after being trained in the complete Training set
        together with validation.
    """
    def train_val_iter(y_train, y_val):       
        yield np.arange(0, y_train.size), \
            np.arange(y_train.size, y_train.size + y_val.size)
        
    data_iter = iter(train_val_iter(y_train, y_val))
    
    random_search = RandomizedSearchCV(pipeline,
                                       param_distributions=params,
                                       n_iter=n_iter,
                                       scoring=make_scorer(score_func),
                                       n_jobs=n_jobs,
                                       random_state=seed,
                                       cv=data_iter, refit=False)
    
    X = np.append(X_train, X_val, axis=0)
    y = np.append(y_train, y_val)
    
    random_search.fit(X, y)
    best_params = random_search.best_params_
    print('Random search best score:', 
          round(random_search.best_score_, 3))
    print('Best parameters:')
    print(best_params)
    
    pipeline.set_params(**best_params)
    pipeline.fit(X, y)
    
    return pipeline


def binarize_prob(prediction_prob, threshold=0.5):
    """ 
    Given probabilistic predictions, returns binary predictions.

    Parameters
    ----------
    prediction_prob: numpy array
        A vector containing the probabilistic predictions.

    threshold : float
        The probabilities threshold to binarize the predictions.

    Returns
    -------
    numpy array
        The binarized hard predictions.
    """
    assert prediction_prob.ndim in (1, 2)
    
    if prediction_prob.ndim == 2:
        hard_prediction = prediction_prob[:, 1] >= threshold
    elif prediction_prob.ndim == 1:
        hard_prediction = prediction_prob >= threshold
    else:
        raise ValueError
        
    return hard_prediction.astype(np.int)


def get_predictions(pipeline, X, prob_threshold):
    """ 
    Given a trained pipeline and dataset, performs prediction.

    Parameters
    ----------
    pipeline: sklearn Pipeline
        The trained pipeline.
        
    X: column of Dataframe
        The samples.
        
    prob_threshold: float
        The probabilities threshold for binarization

    Returns
    -------
    numpy array
        The hard classifications.
    numpy array
        The probabilistic predictions.
    """
    prediction_prob = pipeline.predict_proba(X)
    prediction = binarize_prob(prediction_prob=prediction_prob, 
                               threshold=prob_threshold)
    
    return prediction, prediction_prob[:, 1]


def metrics_report(prediction, y):
    """ 
    Prints the Recall, Precision, F1 score, and plots 
    a confusion matrix.

    Parameters
    ----------
    prediction: numpy array
        The hard predictions.

    y : numpy array
        The true labels.
    """
    recall = round(recall_score(y, prediction), 3)
    precision = round(precision_score(y, prediction), 3)
    f1 = round(f1_score(y, prediction), 3)
    print('Recall:', recall)
    print('Precision:', precision)
    print('F1-score:', f1)
    
    print('\nConfusion Matrix')
    cm = confusion_matrix(y_true=y, y_pred=prediction, 
                          labels=[0, 1])
    cm = pd.DataFrame(cm)
    cm = cm.rename({0: 'True no event', 1: 'True event'}, axis='index')
    cm = cm.rename({0: 'Pred no event', 1: 'Pred event'}, axis='columns')
    print(cm)
    
    return recall, precision, f1
