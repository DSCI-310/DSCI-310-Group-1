"""splits data into training and test splits based on splitsize

Usage: src/splitter.py <input_file> <size> <output_loc>

Options:
<input_file>    Path (including filename) to data file
<size>    Proportion of testing split size
<output_loc>    Path of where to locally write the file
"""

from docopt import docopt
import pandas as pd
from sklearn.model_selection import train_test_split
import os

opt = docopt(__doc__)
DELIMITERS = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()

def splitter(file, size, location):
    df = pd.read_csv("data/raw/student-mat.csv",sep = ";")
    train_df, test_df = train_test_split(df, test_size = size, random_state=100)
    train_df.to_csv(os.path.join(location, "student-mat-train.csv"), sep=";")
    test_df.to_csv(os.path.join(location, "student-mat-test.csv"), sep=";")
    

def main(file, size, location):
    print("running")
    splitter(file, float(size), location)
    print("done")

if __name__ == '__main__':
    main(opt["<input_file>"], opt["<size>"], opt["<output_loc>"])