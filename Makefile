# author: DSCI-310 Group 1
# date: 2022-03-18

#get the data from the web
data/raw/student-mat.csv data/raw/student-por.csv data/raw/student.txt: src/gatherdata.py 
    python src/gatherdata.py 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip' 'data/raw/student-mat.csv'

#split the data into the train and test splits
