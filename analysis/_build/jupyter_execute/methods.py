#!/usr/bin/env python
# coding: utf-8

# # Methods

# In[1]:


import pandas as pd


# Since what we are trying to predict is a quantitative varible based on several variables, it is clear we are aiming for regression analysis. Particularly, the regresion methods from DSCI 100 were knn and least square, where we think the best of the two may be least squares regression. This is namely due to the fact that we hueristically expect quite linear result from many of these variables. Within the scikit-learn package, there are a few options for least squares regression, Linear Regression and Ridge Regression. We will be using Ridge regression, which is functionally similar to linear regression, but manages the coefficients in a manner where none are exceptionally large.
# 

# As we have a few categorical variables and binary variables, we need to encode the data in a manner our model can read, and we decided on one hot encoding given its simplicity. Lastly, while there is no missing data in the dataset, we thought it would be a good idea to use simple imputer in case we run into a situation were there is missing data in our test set or if we decide to use this model on another dataset with the same features.

# Therefore, we create the pipeline to pre-process our data and apply linear regression.
# 

# In[2]:


pd.read_csv('../results/cvtable.csv', sep = ";").sort_values("rank_test_score",ascending=True)


# Ridge Regression takes in 1 hyperparameter that controls the complexity of the model. With higher levels of alpha, we have lower model complexity. We do 5 fold cross validation because it is not too computationally expensive, and we do randomizedsearch because it is better at exploring hyperparameters than gridsearch. The default scoring method of sklearn regression is R^2 score, but it found that RMSE score is easier to interpret in the context of this dataset, therefore we pass in RMSE as the scoring function. While we pass in neg RMSE, it is just as easy to interpret since we just want to look for how close the score is to 0, where the closer it is to 0, the less error it has. Thanks to scikit-learn, we have an easy method of finding out what our best performing hyperparameters are. In this case, the best performing hpyerparameter was a Ridge_alpha value of [9.93], with a mean test error of [4.623]

# In[ ]:




