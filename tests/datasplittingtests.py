import pytest
import urllib.request
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
from pandas.testing import assert_frame_equal, assert_series_equal

import os
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
print(os.getcwd())
import sys
sys.path.append("./src")
from splitxy import splitxy

URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
urllib.request.urlretrieve(URL, "student.zip")
compressed_file = zipfile.ZipFile('student.zip')
csv_file = compressed_file.open('student-mat.csv')
df = pd.read_csv(csv_file,sep = ";")

train_df, test_df = train_test_split(df, test_size = 0.2, random_state=100)

#make training and testing split
desiredfeatures = ["studytime", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "goout","romantic","traveltime"]
X_train, y_train, X_test, y_test = splitxy(train_df, test_df, desiredfeatures, "G3")

#manually creating the dataframe we want to compare with the function
X_train2 = train_df[desiredfeatures]
y_train2 = train_df["G3"]

X_test2 = test_df[desiredfeatures]
y_test2 = test_df["G3"]


class Test_splitxy:
    def test_Xtrain(self):
        assert_frame_equal(X_train, X_train2)

    def test_Xtest(self):
        assert_frame_equal(X_test, X_test2)
    
    def test_ytrain(self):
        assert_series_equal(y_train, y_train2)
    
    def test_ytest(self):
        assert_series_equal(y_test, y_test2)
