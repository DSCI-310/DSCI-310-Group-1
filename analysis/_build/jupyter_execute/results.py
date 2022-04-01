#!/usr/bin/env python
# coding: utf-8

# # Results

# In[1]:


import pandas as pd
from myst_nb import glue


# Now that we have our best performing hyperparameter, we can pass in the best param into our model. Then we can train that model on the entire training set and evaluate it on our testing set.

# In[2]:


finaltable = pd.read_csv('../results/finaltable.csv', sep = ";")

rmse = round(abs(finaltable.iloc[0, 8]), 3)
glue('rmse', rmse)


# In[3]:


finaltable


# According to our best model, our RMSE is {glue:}`rmse` which is better than the value we obtained from cross validation. This suggests one of two things:
# 1. Our model generalized well on this new dataset, or 
# 2. We happened to be lucky for the test set and the model wont generalize well to other datasets in practice.

# :::{figure-md} relation-fig
# <img src="../results/figures/predvsfinal.png" alt="cat" class="bg-primary mb-1" width="400px">
# 
# A plot displaying the relation between the predicted grade and the actual grade
# :::

# The regression graph {numref}`relation-fig` shows that we predict roughly the same values no matter what the true grade of the student happens to be. Only at the very high true grades do we see the predictions start to increase, albeit marginally. The range at low values is a bit larger at about 5-12.5 while at high true grades, it is about 8-13.

# Looking at what feature make the most impact in predicting high true grades, we see that the mother has a very large impact on the predicted grades. Depending on the mother's job, it can positively influence the final grade or it can negatively impact it. We also see that being in a romantic relationship seems to be the most impactful at predicting lower grades. Interestingly, study time isn't the most influential part feature despite intuition telling us that with higher study time, we would except to get higher grades.

# In[4]:


pd.read_csv('../results/coeff-table.csv', sep = ";").sort_values("coefficients", ascending=False)


# In[ ]:




