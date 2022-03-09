import numpy as np
import pandas as pd

def splitxy(train, test, desiredfeatures, target):
    X_train = train[desiredfeatures]
    y_train = train[target]

    X_test = test[desiredfeatures]
    y_test = test[target]
    return X_train, y_train, X_test, y_test