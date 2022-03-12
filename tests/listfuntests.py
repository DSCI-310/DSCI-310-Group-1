import pytest
import urllib.request
import zipfile
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
urllib.request.urlretrieve(URL, "student.zip")
compressed_file = zipfile.ZipFile('student.zip')
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



class Test_listfun:
    def test_listfun(self):
        testout1 = listfun.list_abs(preprocessor, "pipeline-2", "onehotencoder", categorical_features)
        testout2 = listfun.list_abs(preprocessor, "pipeline-3", "onehotencoder", binary_features)
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
        expectout2 = ['Pstatus_T', 'romantic_yes']
        print("Testing if testout1 is the same as expected")
        assert_frame_equal(testout1, expectout1)
        print("Testing if testout1 is the same as expected")
        assert_frame_equal(testout2, expectout2)
        print("All tests passed for listfuntests")