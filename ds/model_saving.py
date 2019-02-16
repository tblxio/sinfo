import joblib

import numpy as np

from copy import deepcopy


def save_model(model, save_path):
    """ 
    Saves the model.

    Parameters
    ----------
    model: object
        The object to be saved. It can be an instance of a sklearn model or 
        an instance of DeployModel, or any python object, actually.

    save_path: string
        The saving path, including filename and extension.
    """
    joblib.dump(model, save_path)


def load_model(load_path):
    """ 
    Loads a model.

    Actually, any python object that was serialized with joblib can be 
    loaded in this way.

    Parameters
    ----------
    load_path: string
        The path to the file that will be loaded.

    Returns
    -------
    object
        The object that was deserialized, which, in principle, should
        be a model.
    """
    return joblib.load(load_path)


class DeployModel:
    """Class that aggregates the models for all the detected events.

    This is handy for deployment in our app because it embeds all the logic
    with signal pre-processing, feature extraction and model prediction.

    Attributes
    ----------
    signal_pre_proc_pipe_dict: Dict
        Dictionary with the pre-processing for each of the selected signals 
        of each event. The keys are the names of each event.
    feature_extraction_funcs_dict: Dict
        Dictionary with the functions for computing the features 
        of each event. The keys are the names of each event.
    decision_pipe_dict: Dict
        Dictionary with the decision related pipeline: feature 
        pre-processing and model prediction. The keys are the names of
        each event.
    window_size_dict: Dict
        Dictionary with the window sizes used for each of the events. 
        The keys are the names of each event.
    signals_dict: Dict
        Dictionary with the signals that each event should use.
        The keys are the names of each event.
    all_signals_name: Dict
        Dictionary with the names of all the available signals. 
        The keys are the names of each event.
    """
    def __init__(self, signal_pre_proc_pipe_dict, 
                 feature_extraction_funcs_dict,
                 decision_pipe_dict, window_size_dict, 
                 signals_dict, all_signals_name):
        
        self.signal_pre_proc_pipe = signal_pre_proc_pipe_dict
        self.feature_extraction_funcs = feature_extraction_funcs_dict
        self.decision_pipe = decision_pipe_dict
        self.window_size = window_size_dict
        self.signals_dict = signals_dict
        self.all_signals_name = all_signals_name
        
        assert len(self.signal_pre_proc_pipe.keys()) == \
            len(self.feature_extraction_funcs.keys())
        assert len(self.signal_pre_proc_pipe.keys()) == \
            len(self.decision_pipe.keys())
        assert len(self.signal_pre_proc_pipe.keys()) == \
            len(self.window_size.keys())
        assert len(self.signal_pre_proc_pipe.keys()) == \
            len(self.signals_dict.keys())
        
        for key in self.signal_pre_proc_pipe.keys():
            assert key in list(self.feature_extraction_funcs.keys())
            assert key in list(self.decision_pipe.keys())
            assert key in list(self.window_size.keys())
            assert key in list(self.signals_dict.keys())
                                    
    def extract_window_features(self, signals_array, feature_funcs, 
                                window_size):
        """Extracts the features from a window, which are the last 
        window_size samples of the signals array.

        Parameters
        ----------
        signals_array: numpy array
            The array of shape [n_samples, n_signals]. Only the last 
            window_size points are used for computing the features.

        feature_funcs : list
            List with the functions that will be computed.

        window_size : list
            Size of the window that will be computed (number of points).

        Returns
        -------
        numpy array
            Array of shape [1, n_features] with the computed features.
        """
        window_signals = signals_array[-window_size:, :]
        n_features = len(feature_funcs)
        n_signals = signals_array.shape[1]
        
        feats = np.zeros((1, n_features * n_signals))
        for signal_i in range(signals_array.shape[1]):
            for feature_i, feature in enumerate(feature_funcs):
                feats[0, signal_i * n_features + feature_i] = \
                    feature(array=window_signals[:, signal_i: signal_i + 1], 
                            axis=0)
                
        return feats
        
    def predict(self, signals_df):
        """Computes the prediction over some given signals.

        Parameters
        ----------
        signals_df: dataframe
            Dataframe with the data of the signals from which predictions 
            will be computed.

        Returns
        -------
        Dictionary
            Dict with the predictions. The keys are the names of the events.
        """
        predictions = {}
        
        for model_name in self.signal_pre_proc_pipe.keys():
            signals = deepcopy(signals_df)
            if signals.shape[0] < self.window_size[model_name]:
                return -1
            
            #signal pre-processing
            sig_pre_proc = self.signal_pre_proc_pipe[model_name]
            signals[self.all_signals_name[model_name]] = \
                sig_pre_proc.transform(signals[\
                    self.all_signals_name[model_name]].values)
                        
            signals_array = signals[self.signals_dict[model_name]].values
            
            # Feature extraction
            feature_funcs = self.feature_extraction_funcs[model_name]
            window_size = self.window_size[model_name]
            X = self.extract_window_features(signals_array, feature_funcs, 
                                             window_size)
            
            decision_pipe = self.decision_pipe[model_name]
            prediction = decision_pipe.predict(X)[0]
            
            predictions[model_name] = prediction
        
        return predictions
