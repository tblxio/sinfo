from copy import deepcopy

import numpy as np


class DummyPreProcessing:
    def transform(self, X):
        return X
    
    def fit(self, X, y=None):
        return X
    
    def fit_transform(self, X, y=None):
        return X


class DeployModel:
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
        prediction = {}
        signals = deepcopy(signals_df)
        
        predictions = {}
        
        for model_name in self.signal_pre_proc_pipe.keys():
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
