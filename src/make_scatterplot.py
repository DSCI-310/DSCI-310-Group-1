import matplotlib.pyplot as plt
import numpy as np
import warnings as wa

# make_scatterplot
#
# draw a scatterplot using matplotlib.pyplot with regression line using desired configurations
#
# @param x an array-like object as x-axis for the scatter
# @param y another array-like object as y-axis for the scatter
# @param alpha_level the optional transparency settings
# @param labels the optional dictionary that includes settings for labels
# the available configuration for labels:
# - "xlabel": <label for x-axis>
# - "ylabel": <label for y-axis>
# - "title": <title for the plot>
# - "figtext": <text under the figure>
#
# @return a scatterplot with regression line with desired features
#
# @examples
# make_scatterplot(x_train, y_train)
# make_scatterplot(x_train, y_train, 0.5, {"xlabel": "x label", "title": "the title"})
def make_scatterplot(x, y, alpha_level=None, labels=None):
    if not (isinstance(x, np.ndarray) and isinstance(y, np.ndarray)):
        wa.warn("Input variables for scatterplot are not array-like objects", UserWarning)
    if (not isinstance(labels, dict)) or not (labels is None):
        raise TypeError("Incorrect type for label configuration")
    if (not (isinstance(alpha_level, int) or isinstance(alpha_level, float))) or not alpha_level is None:
        raise TypeError("Incorrect alpha level configuration")

    if (alpha_level is not None):
        plt.scatter(x, y, alpha=alpha_level)
    else:
        plt.scatter(x, y)

    if (labels is not None):
        for key, value in labels.items():
            if not (isinstance(key, str) and isinstance(value, str)):
                raise TypeError("Incorrect type for individual label")
            if key == "xlabel":
                plt.xlabel(value)
            if key == "ylabel":
                plt.ylabel(value)
            if key == "title":
                plt.title(value)
            if key == "figtext":
                plt.figtext(0.5, -0.05, value, wrap=True, horizontalalignment='center', fontsize=12)

        grid = np.linspace(y_train.min(), y_train.max(), 1000)
        plt.plot(grid, grid, "--k")
