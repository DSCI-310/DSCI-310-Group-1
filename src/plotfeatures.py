import matplotlib.pyplot as plt
from src import plotSquareData

'''
Documentation
'''


def plot_numeric(x_train, y_train, out_path):
    desiredFeatures = ["studytime", "Medu", "Fedu", "goout", "traveltime"]
    titles = ["study time vs grade", "Mother education vs grade", "Father education vs grade", 
                                     "time spent with friends vs grade", "travel time vs grade"]
    txt = "Figure 2 A series of plots examining the numeric features compared to predicted grade"
    plotSquareData.plot_square_data(x_train, y_train, desiredFeatures, titles, txt) 


def plot_categorical(x_train, y_train, out_path):
    desiredFeatures = ["Pstatus", "Mjob", "Fjob", "romantic"]
    titles = ["P status vs grade", "Mother job vs grade", "Father Job vs grade", "Relationship status vs grade"]
    txt = "Figure 3 A series of histograms examining the distribution of categorical features"
    plotSquareData.plot_square_data(x_train, y_train, desiredFeatures, titles, txt)
