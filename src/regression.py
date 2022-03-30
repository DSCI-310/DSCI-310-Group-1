"""takes the split data and trains a Regression model on the data

Usage: src/gatherdata.py <input_loc> <output_loc>

Options:
<input_loc>     website of URL
<output_loc>    Path (including filename) of where to locally write the file
"""

from docopt import docopt
import splitxy
import listfun
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import (
    cross_validate,
    train_test_split,
    RandomizedSearchCV
)
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.impute import SimpleImputer

opt = docopt(__doc__)
DELIMITERS = ". , ; : ? $ @ ^ < > # % ` ! * - = ( ) [ ] { } / \" '".split()

def main(inloc, location):
    print("running")
    
    desiredfeatures = ["studytime", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "goout","romantic","traveltime"]
    train_df = pd.read_csv(os.path.join(inloc, "student-mat-train.csv"),sep = ";")
    test_df = pd.read_csv(os.path.join(inloc, "student-mat-test.csv"),sep = ";")
    X_train, y_train = splitxy.split_xy(train_df, desiredfeatures, "G3")
    X_test, y_test = splitxy.split_xy(test_df, desiredfeatures, "G3")
    
    numeric_features = ["studytime", "Medu", "Fedu", "goout", "traveltime"]
    categorical_features = ["Mjob", "Fjob"]
    binary_features = ["Pstatus", "romantic"]

    preprocessor = make_column_transformer(
        (make_pipeline(SimpleImputer(), StandardScaler()), numeric_features), 
        (make_pipeline(SimpleImputer(strategy="constant", fill_value="missing"), OneHotEncoder(handle_unknown="ignore", sparse=False)), categorical_features),
        (make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(drop="if_binary", dtype=int)), binary_features),
    )
    
    #make cross validation model
    cvmodel = make_model(preprocessor)
    
    #do crossvalidation and get back the dataframe of results
    crossval,df = perform_crossval(cvmodel,  X_train, y_train, location)
    
    #perform analysis
    finalmodel = make_model(preprocessor, crossval.best_params_['ridge__alpha'],)
    predictions, finalscore = perform_testing(finalmodel, X_train, y_train, X_test, y_test)
    
    #make results plot
    make_plot(predictions, y_test, location)
    
    #make coefficient table
    coeff_table(location, preprocessor, numeric_features, categorical_features, binary_features, finalmodel)
    

    #make results table
    df = df[df.rank_test_score == df.rank_test_score.min()].drop(["mean_score_time",
                                                             "std_score_time",
                                                             "split0_test_score",
                                                             "split1_test_score",
                                                             "split2_test_score",
                                                             "split3_test_score",
                                                             "split4_test_score"], axis=1)
    df["final score"] = -finalscore
    df.to_csv(os.path.join(location, "finaltable.csv"), sep = ";")
    
    print("done")
    
    
def make_model(preprocessor, alpha=1.0):
    pipelr = make_pipeline(preprocessor, Ridge(alpha, random_state=123))
    
    return pipelr

def perform_crossval(pipeline, X_train, y_train, location):
    hyperparams = np.exp(np.random.uniform(-3, 3, 10))

    param_dist = {"ridge__alpha": hyperparams}

    rand_search = RandomizedSearchCV(pipeline, param_dist, n_jobs = -1, scoring = "neg_root_mean_squared_error")
    rand_search.fit(X_train, y_train)
    
    df_results = pd.DataFrame(rand_search.cv_results_)
    df_results2 = df_results[df_results.rank_test_score < 5].drop(["mean_score_time",
                                                             "std_score_time",
                                                             "split0_test_score",
                                                             "split1_test_score",
                                                             "split2_test_score",
                                                             "split3_test_score",
                                                             "split4_test_score"], axis=1)
    df_results2.to_csv(os.path.join(location, "cvtable.csv"), sep = ";")
    return rand_search, df_results

def perform_testing(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)

    predicted = model.predict(X_test)
    rms = mean_squared_error(y_test, predicted, squared=False)
    return predicted, rms

def make_plot(predicted, y_test, location):
    figureloc = os.path.join(location, "figures/")
    
    plt.title("Predicted Grade vs True Grade")
    plt.scatter(y_test, predicted, alpha=0.3)
    grid = np.linspace(y_test.min(), y_test.max(), 1000)
    plt.plot(grid, grid, "--k")
    plt.xlabel("true grade")
    plt.ylabel("predicted grade")
    txt = "Figure 4. A plot displaying the relation between the predicted grade and the actual grade"
    plt.figtext(0.5, -0.05, txt, wrap=True, horizontalalignment='center', fontsize=12)
    fig1 = plt.gcf()
    fig1.savefig(os.path.join(figureloc, "predvsfinal.png"))
    
def coeff_table(location, preprocessor, numeric_features, categorical_features, binary_features, finalmodel):
    ohe_columns = listfun.list_abs(preprocessor, "pipeline-2", "onehotencoder", categorical_features)
    ohe_columns2 = listfun.list_abs(preprocessor, "pipeline-3", "onehotencoder", binary_features)

    new_columns = numeric_features + ohe_columns + ohe_columns2

    df_coeff = pd.DataFrame(
        data={
            "features": new_columns,
            "coefficients": finalmodel.named_steps["ridge"].coef_,
        }
    )
    df2 = df_coeff.sort_values("coefficients",ascending=False)
    
    df2.to_csv(os.path.join(location, "coeff-table.csv"), sep = ";")

if __name__ == '__main__':
    main(opt["<input_loc>"], opt["<output_loc>"])