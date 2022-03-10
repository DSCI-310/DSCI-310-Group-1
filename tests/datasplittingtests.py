import pytest
import urllib.request
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
from pandas.testing import assert_frame_equal, assert_series_equal
import numpy as np

import os
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
print(os.getcwd())
import sys
sys.path.append("./src")
from splitxy import split_xy

URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
urllib.request.urlretrieve(URL, "student.zip")
compressed_file = zipfile.ZipFile('student.zip')
csv_file = compressed_file.open('student-mat.csv')
df = pd.read_csv(csv_file,sep = ";")

train_df, test_df = train_test_split(df, test_size = 0.2, random_state=100)

#make training and testing split
desiredfeatures = ["studytime", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "goout","romantic","traveltime"]
X_train, y_train = split_xy(train_df, desiredfeatures, "G3")
X_test, y_test = split_xy(test_df, desiredfeatures, "G3")

class Test_splitxy:
    def test_desiredfeatures_list(self):
        X_train2 = train_df[desiredfeatures]
        X_test2 = test_df[desiredfeatures]
        
        print("testing whether passing in a list of desiredfeatures produces correct output" )
        assert_frame_equal(X_train, X_train2)
        assert_frame_equal(X_test, X_test2)
    
    def test_desiredfeatures_string(self):
        X_train2 = train_df["studytime"]
        X_test2 = test_df["studytime"]
        
        print("testing whether passing in a list of desiredfeatures produces correct output" )
        X_train, _= split_xy(train_df, "studytime", "G3")
        X_test, _ = split_xy(test_df, "studytime", "G3")
        assert_series_equal(X_train, X_train2)
        assert_series_equal(X_test, X_test2)
    
    def test_target_list(self):
        # making a new list of features
        samplefeatures = ["studytime", "Pstatus", "Medu"]
        y_train2 = train_df[samplefeatures]
        y_test2 = test_df[samplefeatures]
        
        print("testing whether passing in a single produces correct output")
        _, y_train= split_xy(train_df, "studytime", samplefeatures)
        _, y_test = split_xy(test_df, "studytime", samplefeatures)
        assert_frame_equal(y_train, y_train2)
        assert_frame_equal(y_test, y_test2)
    
    def test_target_string(self):
        y_train2 = train_df["G3"]
        y_test2 = test_df["G3"]
        
        print("testing whether passing in a single produces correct output")
        _, y_train = split_xy(train_df, desiredfeatures, "G3")
        _, y_test = split_xy(test_df, desiredfeatures, "G3")
        assert_series_equal(y_train, y_train2)
        assert_series_equal(y_test, y_test2)
    
    def test_faultyvariable_in_list(self):
        print("make sure that we properly get an error when inputting desired/target feature we don't have within a list")
        with pytest.raises(KeyError):
            X_train, y_train = split_xy(train_df, ["studytime", "asodfiajsdofi"], "G3")
            X_train, y_train = split_xy(train_df, "G3", ["studytime", "asodfiajsdofi"])
    
    def test_faulty_single_variable(self):
        print("make sure that we properly get an error when inputting single desired/target feature we don't have")
        with pytest.raises(KeyError):
            X_train, y_train = split_xy(train_df, desiredfeatures, "There_will_be_nothing_here")
            X_train, y_train = split_xy(train_df, "There_will_be_nothing_here", desiredfeatures)
    
    def test_incorrect_inputtype(self):
        print("make sure that each of our inputs correctly throws a type error")
        print("throw type error when first input is not a df")
        print("throw type error when second or third input is not a list/str")
        with pytest.raises(TypeError):
            X_train, y_train = split_xy(3, desiredfeatures, "G3")
            X_train, y_train = split_xy(train_df, np.array([1, 2, 3, 4]), "G3")
            X_train, y_train = split_xy(train_df, "G3", np.array([1, 2, 3, 4]))
    
