# Introduction

Education remains one of the most vital and fundamental resources in the world. There is an active body of research that works to explore the relation between education and other societal factors such as economic growth where current research suggests that better education lends itself to better economic growth, and perhaps more importantly for individuals, a higher individual income {cite:p}`owidglobaleducation`. 



There are many other reasons why people may care about their grade besides raw income. A student may want to get into a prestigious university where the entrance requirement is very high (of course, the underlying motivation could be income, but the current motivation is a top university). Alternatively, it may be as simple as getting the satisfaction of seeing a high mark on your report card. Being able to accurately predict your grade allows you to plan in advance to determine if you need extra assistance in a particular subject, or if you are currently on track to meet or exceed the grade you desire. Unfortunately, this is not an easy task. There are many potential factors that can affect your performance, and given that each student has their own unique circumstances, this makes the task of predicting monumental. On the other hand, there are also many features that are common among students, and helps serve as a common ground in being able to predict your final grade.



For this project, we're conducting a multi-variable regression analysis on the **Student Performance** dataset. The original dataset, which was recorded on the UCI ML Repo {cite:p}`schooldata`, was split into two individual datasets, respectively with students' final grades in Portuguese and Math. For this project, we're only focusing on the Math dataset. First used by Cortez and Silva [{cite:year}`sschoolperf`], this dataset was collected for use in decision trees, neural networks, SVMs and Random Forest. The dataset has an very large number of potentially useful features. There are 30 features and 3 outputs; however, for the purposes of this analysis, we will only focus on 9 features with varying levels of intuitive correlation with the final end of year grade G3, mostly consisting of social factors. For instance, the feature "study time", at a glance, seems like there will be a positive correlation with final grade while the feature "romantic" is not as straightforward to tell. 



The dataset we will be using contains the following features (the type of feature is given by the UCI ML Repo):

| Variable                                                     | Type (Unit)                      | Response 1         | Response 2           | Response 3        | Response 4             | Response 5          |
| ------------------------------------------------------------ | -------------------------------- | ------------------ | -------------------- | ----------------- | ---------------------- | ------------------- |
| `study time`: The number of hours spend studying per week.   | numeric (time)                   | Less than 2 hours  | 2 to 5 hours         | 3 to 5 hours      | 4 to 10 hours          | More than 10 hours  |
| `Pstatus`: Whether the parents of the student are currently living together or seperated | binary                           | T: Living together | A: Living apart      | -                 | -                      | -                   |
| `Medu`: Numeric representations of the mother's education level | scale (education level)          | 0: None            | 1: Primary education | 2: Grade 5 to 9   | 3: Secondary education | 4: Higher education |
| `Fedu`: Numeric representations of the father's education level | scale (education level)          | 0: None            | 1: Primary education | 2: Grade 5 to 9   | 3: Secondary education | 4: Higher education |
| `Mjob`: The mother's job                                     | category (job type)              | Teacher            | Health care related  | Civil services    | At home                | Other               |
| `Fjob`: The father's job                                     | category (job type)              | Teacher            | Health care related  | Civil services    | At home                | Other               |
| `goout`: A representation of how often the student goes out with friends | scale (frequency)                | 1: Very low        | 2: Low               | 3: Moderate       | 4: High                | 5: Very high        |
| `travel time`: how long it takes to get to school            | numeric (time)                   | Less than 15 mins  | 15 to 30 mins        | 30 mins to 1 hour | More than 1 hour       | -                   |
| `romantic`: Whether or not the student is in a romantic relationship | binary                           | Yes                | No                   | -                 | -                      | -                   |
| `G3`: The final grade of the student at the end of the year  | scale (final grade, 0-20 levels) | 0: 0% to 5%        | 1: 5% to 10%         | …                 | 19: 90% to 95%         | 20: 95% to 100%     |

 

Thus, we are interested in looking to answer the following question: **Can we predict a student's final grade (denoted by "G3" in the dataset) given the above features**.