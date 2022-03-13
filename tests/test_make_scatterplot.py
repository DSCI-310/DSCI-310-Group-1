#!/usr/bin/env python
from matplotlib.testing.decorators import image_comparison
import pytest
import urllib.request
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
from pandas.testing import assert_frame_equal, assert_series_equal
import numpy as np
import matplotlib.pyplot as plt
import warnings as wa
from src import splitxy
from src import plotSquareData
import warnings as wa

URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
urllib.request.urlretrieve(URL, "data/raw/student.zip")
compressed_file = zipfile.ZipFile('data/raw/student.zip')
csv_file = compressed_file.open('student-mat.csv')
df = pd.read_csv(csv_file,sep = ";")

train_df, test_df = train_test_split(df, test_size = 0.2, random_state=100)
desiredfeatures = ["studytime", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "goout","romantic","traveltime"]
X_train, y_train = splitxy.splitxy(train_df, desiredfeatures, "G3")


class Test_make_scatterplot:
    
