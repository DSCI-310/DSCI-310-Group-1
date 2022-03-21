# author: DSCI-310 Group 1
# date: 2022-03-18

#includes the items for the exploratory data analysis and the final analysis 
all : results/figures/explore_numeric.png results/figures/explore_cat.png results/exploratory-stu-mat.csv results/coeff-table.csv results/figures/predvsfinal.png results/cvtable.csv results/finaltable.csv

#get the data from the web
data/raw/student-mat.csv: src/gatherdata.py
	python src/gatherdata.py "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip" "data/raw/student-mat.csv"

#split data into train test splits
data/student-mat-test.csv data/student-mat-train.csv: src/splitter.py data/raw/student-mat.csv
	python src/splitter.py data/raw/student-mat.csv 0.2 "data/"

#get exploratory data analysis tables and figures
results/figures/explore_numeric.png results/figures/explore_cat.png results/exploratory-stu-mat.csv: src/generate_exploratory.py data/student-mat-test.csv data/student-mat-train.csv
	python src/generate_exploratory.py "data/student-mat-train.csv" "results/"

#perform regression and get final tables and plots
results/coeff-table.csv results/figures/predvsfinal.png results/cvtable.csv results/finaltable.csv: src/regression.py data/student-mat-test.csv data/student-mat-train.csv
	python src/regression.py "data/" "results/"

clean :
	rm -f data/raw/student-mat.csv
	rm -f data/*.csv
	rm -f results/*.csv
	rm -f results/figures/*.png
