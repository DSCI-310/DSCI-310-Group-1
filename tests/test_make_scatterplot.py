import matplotlib.pyplot as plt
import pytest
from src.make_scatterplot import *
from sklearn.datasets import make_blobs
import random

random.seed(2022)
x, y = make_blobs(n_samples=1000, centers=3, n_features=1)

class test_make_scatterplot:

    def test_with_default(self):
        f, ax = plt.subplots()
        make_scatterplot(x, y)
        plt.scatter(x, y)
        ax = plt.gca()
        offset = ax.collections[0].set_offset_position('data')

        np.testing.assert_array_equal(offset[0], x)
        np.testing.assert_array_equal(offset[1], y)

        assert ax.get_xlabel() == None
        assert ax.get_ylabel() == None
        assert ax.get_title() == None

    def test_normal_with_alpha_level(self):
        f, ax = plt.subplots()
        make_scatterplot(x, y, alpha_level=0.1)
        plt.scatter(x, y)
        ax = plt.gca()
        offset = ax.collections[0].set_offset_position('data')

        np.testing.assert_array_equal(offset[0], x)
        np.testing.assert_array_equal(offset[1], y)

        plt.rcParams["figure.alpha"] = 0.1

        assert ax.get_xlabel() is None
        assert ax.get_ylabel() is None
        assert ax.get_title() is None
        assert plt.rcParams["figure.figtext"] is None

    def test_normal_with_labels(self):
        f, ax = plt.subplots()
        make_scatterplot(x, y, labels={"xlabel": "x_test",
                                       "ylabel": "y_test",
                                       "title": "title_test",
                                       "figtext": "figtext_test"})
        plt.scatter(x, y)
        ax = plt.gca()
        offset = ax.collections[0].set_offset_position('data')

        plt.rcParams["figure.alpha"] = 1

        np.testing.assert_array_equal(offset[0], x)
        np.testing.assert_array_equal(offset[1], y)

        assert ax.get_xlabel() == "x_test"
        assert ax.get_ylabel() == "y_test"
        assert ax.get_title() == "title_test"
        assert plt.rcParams["figure.figtext"] == "figtext_test"

    def test_normal_with_wrong_labels(self):
        make_scatterplot(x, y, labels={"xlabel": "x_test",
                                       "ylabel": "y_test",
                                       "title": "title_test",
                                       "wrong_label": "wrong_test"})
        plt.scatter(x, y)
        ax = plt.gca()
        offset = ax.collections[0].set_offset_position('data')

        plt.rcParams["figure.alpha"] = 1

        np.testing.assert_array_equal(offset[0], x)
        np.testing.assert_array_equal(offset[1], y)

        assert ax.get_xlabel() == "x_test"
        assert ax.get_ylabel() == "y_test"
        assert ax.get_title() == "title_test"
        assert plt.rcParams["figure.figtext"] is None

    def test_invalid_alpha_level(self):
        with pytest.raises(TypeError):
            make_scatterplot(x, y, alpha_level="1")

        with pytest.raises(TypeError):
            make_scatterplot(x, y, alpha_level=[1, "alpha"])

        with pytest.raises(TypeError):
            make_scatterplot(x, y, alpha_level={})

        with pytest.raises(ValueError):
            make_scatterplot(x, y, alpha_level=-1)

        with pytest.raises(ValueError):
            make_scatterplot(x, y, alpha_level=20)

    def test_invalid_labels(self):
        with pytest.raises(TypeError):
            make_scatterplot(x, y, 1, 1)

        with pytest.raises(TypeError):
            make_scatterplot(x, y, 1, "label")

        with pytest.raises(TypeError):
            make_scatterplot(x, y, [1, "alpha"])




        
