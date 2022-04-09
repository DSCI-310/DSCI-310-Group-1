"""splits data into training and test splits based on splitsize

Usage: src/generate_exploratory.py <input_loc> <output_loc>

Options:
<input_loc>    Path to data files
<output_loc>    Path of where to locally write the file
"""
from docopt import docopt 
import pandas as pd
from sklearn.model_selection import train_test_split
import os
from grouponefunctions.grouponefunctions import split_xy, plot_square_data

opt = docopt(__doc__)
DELIMITERS = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()

def main(path, location):
    print("running")
    generator(path, location)
    print("done")

def generator(path, location):

    if not os.path.exists(location):
      # Create a new directory because it does not exist 
      os.makedirs(location)
    
    desiredfeatures = ["studytime", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "goout","romantic","traveltime"]
    train_df = pd.read_csv(path,sep = ";")
    X_train, y_train = split_xy(train_df, desiredfeatures, "G3")

    describer = X_train.describe(include="all")
    describer.to_csv(os.path.join(location, "exploratory-stu-mat.csv"))
    
    generate_figure(X_train, y_train, location)


def generate_figure(X_train, y_train, location):
    figureloc = os.path.join(location, "figures/")
    
    if not os.path.exists(figureloc):
      # Create a new directory because it does not exist 
      os.makedirs(figureloc)
    
    desiredFeatures2 = ["studytime", "Medu", "Fedu", "goout", "traveltime"]
    titles = ["study time vs grade", "Mother education vs grade", "Father education vs grade", 
                                         "time spent with friends vs grade", "travel time vs grade"]
    txt = "Figure 2 A series of plots examining the numeric features compared to predicted grade"
    _,fig1=plot_square_data(X_train, y_train, desiredFeatures2, titles, txt) 
    
    fig1.savefig(os.path.join(figureloc, "explore_numeric.png"))

    desiredFeatures3 = ["Pstatus", "Mjob", "Fjob", "romantic"]
    titles2 = ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"]
    txt2 = "Figure 3 A series of histograms examining the distribution of categorical features"
    _,fig2 = plot_square_data(X_train, y_train, desiredFeatures3, titles2, txt2)
    
    fig2.savefig(os.path.join(figureloc, "explore_cat.png"))
    
if __name__ == '__main__':
    main(opt["<input_loc>"], opt["<output_loc>"])