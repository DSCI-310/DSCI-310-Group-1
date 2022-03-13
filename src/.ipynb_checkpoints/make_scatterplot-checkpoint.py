import matplotlib.pyplot as plt
import numpy as np
import warnings as wa

def make_scatterplot(x, y, alpha_level=None, labels=None):
    if not (isinstance(x, np.ndarray) and isinstance(y, np.ndarray)):
        wa.warn("Input variables for scatterplot are not array-like objects", UserWarning)
    if not isinstance(labels, dict):
        raise TypeError("Incorrect type for label configuration")
    if not (isinstance(alpha_level, int) or isinstance(alpha_level, float)):
        raise TypeError("Incorrect alpha level configuration")
        
    plt.scatter(x, y, alpha=alpha_level)
    grid = np.linspace(y_train.min(), y_train.max(), 1000)
    plt.plot(grid, grid, "--k")
    
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
