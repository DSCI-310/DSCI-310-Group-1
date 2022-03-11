import pytest
import urllib.request
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
from pandas.testing import assert_frame_equal, assert_series_equal
import numpy as np
import matplotlib.pyplot as plt

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

class Test_Square_Plot:
    def check_axs_equal(self, ax1, ax2):
        retval = True
        if ax1.getGeometry() != ax2.getGeometry():
            return False
        for i in range(ax1.getGeometry()[0]):
            for j in range(ax1.getGeometry()[1]):
                if ax1[i,j].title() != ax2[i,j].title():
                    return False
        return True
        
    def test_good_5items_incomplete(self):
        
        fig, axs = plt.subplots(2, 3, figsize=(10,10))
        axs[0, 0].scatter(X_train["studytime"], y_train)
        axs[0, 0].set_title('study time vs grade')
        axs[0, 1].scatter(X_train["Medu"], y_train)
        axs[0, 1].set_title('Mother education vs grade')
        axs[0, 2].scatter(X_train["Fedu"], y_train)
        axs[0, 2].set_title('Father education vs grade')
        axs[1, 0].scatter(X_train["goout"], y_train)
        axs[1, 0].set_title('time spent with friends vs grade')
        axs[1, 1].scatter(X_train["traveltime"], y_train)
        axs[1, 1].set_title('travel time vs grade')
        txt = "Figure 2 A series of plots examining the numeric features compared to predicted grade"
        plt.figtext(0.5, 0.05, txt, wrap=True, horizontalalignment='center', fontsize=12)

        test_axs = plot_square_data(X_train, y_train, ["studytime", "Medu", "Fedu", "goout", "traveltime"], 
                                    ["study time vs grade", "Mother education vs grade", "Father education vs grade", 
                                     "time spent with friends vs grade", "travel time vs grade"], txt)
        
        
        
        print("testing whether a set of 5 plots plots correctly in size and title (plots have some room for placement case)" )
        assert self.check_axs_equal(self, axs, test_axs)
    
    def test_good_4items_complete(self):
        
        fig, axs = plt.subplots(2, 2, figsize=(10,10))
        axs[0, 0].hist(X_train["Pstatus"])
        axs[0, 0].set_title('P status vs grade')
        axs[0, 1].hist(X_train["Mjob"])
        axs[0, 1].set_title('Mother job vs grade')
        axs[1, 0].hist(X_train["Fjob"])
        axs[1, 0].set_title('Father Job vs grade')
        axs[1, 1].hist(X_train["romantic"])
        axs[1, 1].set_title('Relationship status vs grade')
        txt = "Figure 3 A series of histograms examining the distribution of categorical features"
        plt.figtext(0.5, 0.05, txt, wrap=True, horizontalalignment='center', fontsize=12)

        test_axs = plot_square_data(X_train, y_train, ["Pstatus", "Mjob", "Fjob", "romantic"], 
                                    ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"], txt)
        
        
        
        print("testing whether a set of 4 plots plots correctly in size and title (every plot in perfect square)" )
        assert self.check_axs_equal(self, axs, test_axs)
        
    # TODO FROM THIS POINT
    def test_bad_not_dataframes(self):
        
        print("testing ..." )
        
        with pytest.raises(TypeError) as e_info:
            test_axs = plot_square_data(X_train, y_train, ["Pstatus", "Mjob", "Fjob", "romantic"], 
                                    ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"], txt)
            assert str(exc_info.value) == 'The first two arguments are not dataframes of equal length'
    
    def test_bad_not_equal_length(self):
        
        print("testing ..." )
        
        with pytest.raises(TypeError) as e_info:
            test_axs = plot_square_data(X_train, y_train, ["Pstatus", "Mjob", "Fjob", "romantic"], 
                                    ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"], txt)
            assert str(exc_info.value) == 'The first two arguments are not dataframes of equal length'
            
    def test_bad_not_desired_not_list(self):
        
        print("testing ..." )
        
        with pytest.raises(TypeError) as e_info:
            test_axs = plot_square_data(X_train, y_train, ["Pstatus", "Mjob", "Fjob", "romantic"], 
                                    ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"], txt)
            assert str(exc_info.value) == 'desiredFeatures is not a list of strings length at least 1'
            
    def test_bad_not_txt_not_string(self):
        
        print("testing ..." )
        
        with pytest.raises(TypeError) as e_info:
            test_axs = plot_square_data(X_train, y_train, ["Pstatus", "Mjob", "Fjob", "romantic"], 
                                    ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"], txt)
            assert str(exc_info.value) == 'The last argument is not a string'
            
    def test_bad_feature_dne(self):
        
        print("testing ..." )
        
        with pytest.raises(TypeError) as e_info:
            test_axs = plot_square_data(X_train, y_train, ["Pstatus", "Mjob", "Fjob", "romantic"], 
                                    ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"], txt)
            assert str(exc_info.value) == 'desiredFeature is not in dependent dataframe'
            
