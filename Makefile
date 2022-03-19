# author: DSCI-310 Group 1
# date: 2022-03-18

#get the data from the web
data/raw/student-mat.csv: src/gatherdata.py
	python src/gatherdata.py "archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip" "data/raw/student-mat.csv"
    
data/raw/student-mat-train.csv data/raw/student-mat-test.csv : src/splitter.py
	python src/splitter.py "data/raw/student-mat.csv" 0.2 "data"

clean :
	rm -f data/raw/student-mat.csv
