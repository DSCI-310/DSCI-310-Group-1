# Introduction

Education remains one of the most vital and fundamental resources in the world. There is an active body of research that works to explore the relation between education and other societal factors such as economic growth where current research suggests that better education lends itself to better economic growth, and perhaps more importantly for individuals, a higher individual income {cite:p}`owidglobaleducation`. 



There are many other reasons why people may care about their grade besides raw income. A student may want to get into a prestigious university where the entrance requirement is very high (of course, the underlying motivation could be income, but the current motivation is a top university). Alternatively, it may be as simple as getting the satisfaction of seeing a high mark on your report card. Being able to accurately predict your grade allows you to plan in advance to determine if you need extra assistance in a particular subject, or if you are currently on track to meet or exceed the grade you desire. Unfortunately, this is not an easy task. There are many potential factors that can affect your performance, and given that each student has their own unique circumstances, this makes the task of predicting monumental. On the other hand, there are also many features that are common among students, and helps serve as a common ground in being able to predict your final grade.



For this project, we're conducting a multi-variable regression analysis on the **Student Performance** dataset. The original dataset, which was recorded on the UCI ML Repo {cite:p}`schooldata`, was split into two individual datasets, respectively with students' final grades in Portuguese and Math. For this project, we're only focusing on the Math dataset. First used by Cortez and Silva [{cite:year}`sschoolperf`], this dataset was collected for use in decision trees, neural networks, SVMs and Random Forest. The dataset has an very large number of potentially useful features. There are 30 features and 3 outputs; however, for the purposes of this analysis, we will only focus on 9 features with varying levels of intuitive correlation with the final end of year grade G3, mostly consisting of social factors. For instance, the feature "study time", at a glance, seems like there will be a positive correlation with final grade while the feature "romantic" is not as straightforward to tell. 



The dataset we will be using contains the following features (the type of feature is given by the UCI ML Repo):

- `study time`: The number of hours spend studying per week. It is a numeric feature where each number is associated with a range of hours spent studying (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours).

- `Pstatus`: Whether the parents of the student are currently living together or seperated (Binary feature: T = living together, A = apart)

- `Medu`: Numeric representations of the mother's education level  (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education)

- `Fedu`: Numeric representations of the father's education level  (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education)

- `Mjob`: The mother's job (Categorical: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')

- `Fjob`: The father's job (Categorical: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')

- `goout`: A representation of how often the student goes out with friends (numeric: from 1 - very low to 5 - very high)

- `travel time`: how long it takes to get to school (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)

- `romantic`: Whether or not the student is in a romantic relationship (Binary: yes and no)

- `G3`: The final grade of the student at the end of the year represented by a 0-20 scale (numeric: from 0-20 where 0 represents 0-5% and 20 represents 95-100%)

 

Thus, we are interested in looking to answer the following question: **Can we predict a student's final grade (denoted by "G3" in the dataset) given the above features**.