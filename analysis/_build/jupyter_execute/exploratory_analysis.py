#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# In[1]:


import pandas as pd
pd.set_option("display.max_rows", 15, "display.max_columns", None)


# At the very first of the exploratory analysis process, it is always helpful to take a glance at the structures and details of the raw dataset we archived from the [UCI ML Repo](https://archive-beta.ics.uci.edu/ml/datasets/student+performance).

# In[2]:


pd.read_csv('../data/raw/student-mat.csv', sep = ";").iloc[:,1:]


# Then, we decided on a train test split of 80% training and 20% testing. This was because the number of samples in the dataset where moderately low (396) so we wanted more samples to train on. Using panda's describe all and styler to make a table, we can find many useful pieces of information for all of our features inside the training set. For numerical features, we can see interesting pieces of info such as the average mother education is higher than the average father education. Furthermore, for categorical variables, we can see interesting info such as the most frequent parent status in our training set is that they are still living together and most people are not in a romantic relationship.

# In[3]:


pd.read_csv('../results/exploratory-stu-mat.csv', sep = ",")


# From the numeric features represented in {numref}`Figure {number}: {name} <num-fig>`, we can see that for the most part, there is no relation between these features and predicted grade. The only truly interesting thing to note is that with higher travel time, it seems that the range of grades gets narrower and narrower such that the low end of the range is higher than lower values of travel time, but the high end of the range is also much lower compared to lower values of travel time. Of course, it is difficult to say whether this is true or not given the low number of samples for higher travel time.

# :::{figure-md} num-fig
# <img src="../results/figures/explore_numeric.png" alt="num" class="bg-primary mb-1" width="550px">
# 
# A series of plots examining the numeric features compared to predicted grade
# :::

# From the exploratory categorical variable analysis indicated by {numref}`Figure {number}: {name} <cat-fig>` , we can see that for some of these variables, we have a big imbalance between classes. This is especially prominent in P status and Father job. The consequence of this is that the coefficient end up not being very useful in terms of predicting grades as, for example, P status = t may have lots of representation in high and low categories. Furthermore, given the low amount of P status = A, the model we use might misrepresent the data if all of the "A" values end up being either high or low grades, and not a mix of both when we apply our model to the test set.

# :::{figure-md} cat-fig
# <img src="../results/figures/explore_cat.png" alt="cat" class="bg-primary mb-1" width="550px">
# 
# A series of plots examining the categorical features compared to predicted grade
# :::
