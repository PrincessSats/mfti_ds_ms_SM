import numpy as np

class SimplifiedBaggingRegressor:
    def __init__(self, num_bags, oob=False):
        self.num_bags = num_bags
        self.oob = oob
        
    def _generate_splits(self, data: np.ndarray):
        '''
        Generate indices for every bag and store in self.indices_list list
        '''
        self.indices_list = []
        data_length = len(data)
        for bag in range(self.num_bags):
            # Your Code Here
            bag_indices = np.random.choice(data_length, size=data_length, replace=True)
            self.indices_list.append(bag_indices)
            
        
    def fit(self, model_constructor, data, target):
        '''
        Fit model on every bag.
        Model constructor with no parameters (and with no ()) is passed to this function.
        
        example:
        
        bagging_regressor = SimplifiedBaggingRegressor(num_bags=10, oob=True)
        bagging_regressor.fit(LinearRegression, X, y)
        '''
        self.data = None
        self.target = None
        self._generate_splits(data)
        assert len(set(list(map(len, self.indices_list)))) == 1, 'All bags should be of the same length!'
        assert list(map(len, self.indices_list))[0] == len(data), 'All bags should contain `len(data)` number of elements!'
        self.models_list = []
        for bag in range(self.num_bags):
            model = model_constructor()
            data_bag, target_bag = data[self.indices_list[bag]], target[self.indices_list[bag]]
            self.models_list.append(model.fit(data_bag, target_bag)) # store fitted models here
        if self.oob:
            self.data = data
            self.target = target
        
    def predict(self, data):
        '''
        Get average prediction for every object from passed dataset
        '''
        # Your code here
        predictions = np.zeros((len(data), self.num_bags))
        for i, model in enumerate(self.models_list):
            predictions[:, i] = model.predict(data)  # Predict using each model
        return np.mean(predictions, axis=1)
    
    def _get_oob_predictions_from_every_model(self):
        '''
        Generates list of lists, where list i contains predictions for self.data[i] object
        from all models, which have not seen this object during training phase
        '''
        list_of_predictions_lists = [[] for _ in range(len(self.data))]
        # Your Code Here
        for i, model in enumerate(self.models_list):
            oob_indices = np.setdiff1d(np.arange(len(self.data)), self.indices_list[i])
            for idx in oob_indices:
                list_of_predictions_lists[idx].append(model.predict(self.data[idx].reshape(1, -1))[0])
        
        
        self.list_of_predictions_lists = np.array(list_of_predictions_lists, dtype=object)
    
    def _get_averaged_oob_predictions(self):
        '''
        Compute average prediction for every object from training set.
        If object has been used in all bags on training phase, return None instead of prediction
        '''
        self._get_oob_predictions_from_every_model()
        self.oob_predictions = []
        for predictions in self.list_of_predictions_lists:
            if len(predictions) > 0:
                self.oob_predictions.append(np.mean(predictions))
            else:
                self.oob_predictions.append(None)
        # Convert oob_predictions to a NumPy array for proper indexing later
        self.oob_predictions = np.array(self.oob_predictions, dtype=object)
        
        
    def OOB_score(self):
        '''
        Compute mean square error for all objects, which have at least one prediction
        '''
        self._get_averaged_oob_predictions()
        valid_indices = [i for i, pred in enumerate(self.oob_predictions) if pred is not None]
        if len(valid_indices) == 0:
            return None  # No valid OOB predictions
        true_values = self.target[valid_indices]
        oob_preds = self.oob_predictions[valid_indices]
        mse = np.mean((true_values - oob_preds) ** 2)
        return mse