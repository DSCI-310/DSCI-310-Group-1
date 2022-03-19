import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_square_data(x_df, y_df, desiredFeatures, titles, txt):
    # Create plots to display in a square manner ( tiles of plots in 2x2, 3x3 or (n)by(n-1) configuration
    #
    # Takes in the required x and y dataframes that will be used to display the desired features in x_df 
    # alongside the data in y_df and the respective titles 
    #
    # @param x_df dataframe containing dependent variables
    # @param y_df dataframe containing independent variables
    # @param desiredFeatures Target feature(s) in x_df you desire for your analysis in list form
    # @param titles The respective titles(s) desired for your plot(s) in list form
    # @param txt the text to display as a string over the plot
    #
    # @return axy for testing purposes on the features of the plot
    # @return fig which is a copy of the plot able to be used in other functions
    #
    # @examples
    # plot_square_data(X_train, y_train, ["feature1", "feature2", "feature3"], ["title1", "title2", "title3], "This is Plot 1")
    # plot_square_data(dependent, independednts, ["income"], ["retirement_age"], "Income and Retirement Age Relation")
    

    if isinstance(x_df, pd.DataFrame) and isinstance(y_df, pd.Series) and x_df.shape[0] == y_df.shape[0]:
        if isinstance(desiredFeatures, list) and len(desiredFeatures) > 0 and isinstance(desiredFeatures[0], str):
            if isinstance(titles, list) and len(titles) > 0 and isinstance(titles[0], str) and len(titles) == len(desiredFeatures):
                if not isinstance(txt, str):
                    raise TypeError("The last argument is not a string")

                # This will form a minimum sized box for the plots to go in, preferring horizontal boxes
                # will aways preffer to create a box rather than make vertical spanning blocks if there are many
                side_length_x = int(len(titles)**(1/2))
                side_length_y = int(len(titles)**(1/2))
                if side_length_x * side_length_y < len(titles):
                    side_length_x += 1
                    if side_length_x * side_length_y < len(titles):
                        side_length_y += 1


                fig, axs = plt.subplots(side_length_y, side_length_x, figsize=(10,10))

                x = 0
                y = 0
                try:
                    for i, feature in enumerate(desiredFeatures):
                        #print(desiredFeatures[i])
                        axs[y, x].scatter(x_df[desiredFeatures[i]], y_df)
                        axs[y, x].set_title(titles[i])
                        x += 1
                        if x >= side_length_x:
                            x = 0
                            y += 1
                except:
                    raise TypeError("desiredFeature is not in dependent dataframe")


                # plt.figtext(0.5, 0.05, txt, wrap=True, horizontalalignment='center', fontsize=12)
                fig1 = plt.gcf()
                plt.show()
                
                return axs,fig1
            else:
                raise TypeError("titles is not a list of strings of length equal to desiredFeatures")
        else:
            raise TypeError("desiredFeatures is not a list of strings length at least 1")
    else:
        raise TypeError("The first two arguments are not dataframes of equal length")
      
