import pytest
import urllib.request
import zipfile
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

import sys
sys.path.append("..")
from src import listfun

URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
urllib.request.urlretrieve(URL, "data/raw/student.zip")
compressed_file = zipfile.ZipFile('data/raw/student.zip')
csv_file = compressed_file.open('student-mat.csv')

df = pd.read_csv(csv_file,sep = ";")
numeric_features = ["studytime", "Medu", "Fedu", "goout", "traveltime"]
categorical_features = ["Mjob", "Fjob"]
binary_features = ["Pstatus", "romantic"]

preprocessor = make_column_transformer(
    (make_pipeline(SimpleImputer(), StandardScaler()), numeric_features), 
    (make_pipeline(SimpleImputer(strategy="constant", fill_value="missing"), OneHotEncoder(handle_unknown="ignore", sparse=False)), categorical_features),
    (make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(drop="if_binary", dtype=int)), binary_features),
)

train_df, test_df = train_test_split(df, test_size = 0.2, random_state=100)
X_train = train_df.drop(columns = ["G3"])
y_train = train_df["G3"]

preprocessor.fit_transform(X_train,y_train)
print(preprocessor)

class Test_listfun:
    def test_listfun1(self):
        testout1 = listfun.list_abs(preprocessor, "pipeline-2", "onehotencoder", categorical_features)
        expectout1 = ['Mjob_at_home',
                     'Mjob_health',
                     'Mjob_other',
                     'Mjob_services',
                     'Mjob_teacher',
                     'Fjob_at_home',
                     'Fjob_health',
                     'Fjob_other',
                     'Fjob_services',
                     'Fjob_teacher']
        
        print("Testing if testout1 is the same as expected")
        assert testout1 == expectout1
        
        
    def test_listfun2(self):
        testout2 = listfun.list_abs(preprocessor, "pipeline-3", "onehotencoder", binary_features)
        expectout2 = ['Pstatus_T', 'romantic_yes']
        print("Testing if testout1 is the same as expected")
        assert testout2 == expectout2
        
    def test_incorrect_param1(self):
        with pytest.raises(TypeError):
            testout = listfun.list_abs(preprocessor, 1, "onehotencoder", binary_features)
            
            
    def test_incorrect_param2(self):
        with pytest.raises(TypeError):
            testout = listfun.list_abs(preprocessor, "string", 1, binary_features)
            
    def test_incorrect_param3(self):
        with pytest.raises(TypeError):
            testout = listfun.list_abs(preprocessor, "string", 1, "string")