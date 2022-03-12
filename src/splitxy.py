import numpy as np
import pandas as pd
import warnings as wa

def splitxy(df, desiredfeatures, target):
    # Split data into target and desired features
    #
    # Takes in a dataframe and extracts the desired features used
    # to predict a specified target variable in the 
    #
    # @param df A data frame.
    # @param desiredfeatures Target feature(s) you desire for your analysis in list or string form
    # @param target The target variable(s) you desire for your analysis in list or string form
    #
    # @return Two data frames or series each with number of columns equal to the number of variables passed in
    # as desiredfeatures and target. Whether it's a dataframe or pd.series depends on number of variables passed into
    # the arguments for desiredfeatures and target. If either passes in a list, it will return a dataframe
    # if either passes in a single string, it will return a pd.series.
    #    The dataframe/series (named X_df) contains only the columns listed in desiredfeatures from the input data frame.
    #    The second dataframe/series (named y_df) contains only the columns listed in target from the input data frame.
    #
    # @examples
    # X_train, y_train = split_xy(train_df, ["feature1", "feature2", "feature3"], "G3")
    # X_train, y_train = split_xy(train_df, "G3", ["feature1", "feature2", "feature3"])
    X_df = None
    y_df = None
    
    if isinstance(desiredfeatures, str) and isinstance(target, str):
        if target == desiredfeatures:
            wa.warn("Desiredfeatures and target have features in common. Are you sure?", UserWarning)
    elif any(item in desiredfeatures for item in target) or any(item in target for item in desiredfeatures):
        list1 = set(desiredfeatures)
        both = list1.intersection(target)
        wa.warn("Desiredfeatures and target have features in common. Are you sure?", UserWarning)
    
    if isinstance(df, pd.DataFrame):
        if isinstance(desiredfeatures, str) or isinstance(desiredfeatures, list):
            X_df = df[desiredfeatures]
        else:
            raise TypeError("desiredfeatures is not a list or string")

        if isinstance(target, str) or isinstance(target, list):
            y_df = df[target]
        else:
            raise TypeError("target is not a list or string")
    else:
        raise TypeError("First argument is not a dataframe")
        
    return X_df, y_df