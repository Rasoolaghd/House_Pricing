

from sklearn.base import BaseEstimator, TransformerMixin

# a transformer that gets the desired attributes and converting Dataframe to numpy array.
class DataFrameSelector(BaseEstimator, TransformerMixin):

    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values

num_attributes = list(housing_num)
