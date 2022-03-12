# Predicting students’ grades using multi-variable regression

**Contributors:** Andres, Daniel, Zizhen, Timothy



## Summary

For this project, we put our focus on predicting students’ final grades. Being able to efficiently predict the final grade allows a student to track their current progress and plan in advanced. The dataset being used is recorded at [UCI ML Repo](https://archive-beta.ics.uci.edu/ml/datasets/student+performance). We are particularly interested in how would the following features provided in the data could contribute to the prediction of students’ final grade `G3`:

- `study time`: The number of hours spend studying per week.
- `Pstatus`: Whether the parents are living together or seperated.
- `Medu`: Mother's education level.
- `Fedu`: Father's education level.
- `Mjob`: The mother's job.
- `Fjob`: The father’s job.
- `goout`: Frequency of that student hanging out with friends.
- `romantic`: Whether the student is in a romantic relationship.
- `travel time`: How long it takes for the student to get to school.


Since we are using a mixture of categorical variables and numeric variables to predict a quantitative result, the concept of least square regression analysis from DSCI 100 could be implemented and extended to fit our context.

We performed a 80-20 split on the dataset and trained a multi-variable least-square regression model on the training data with the 9 features we selected for the model. The simplest method of doing least squares regression is Ridge Regression, which is functionally similar to Linear Regression, but better at avoiding unexpected coefficients.

We test the model with cross validation and get an average cv-score of -4.61, which means an error of 4.61 and a final RMSE error of 3.83.



## How to run?

### From DockerHub

Our project is published at Dockerhub. Thus, it is convenient to run our repository directly in the terminal. Execute the following command:

```
docker pull danielhou13/dsci-310-project:latest

docker run -it danielhou13/dsci-310-project
```

### Clone the repository

If the first method does not work out, you can also clone the repository, and build the Docker image locally.

```
git clone https://github.com/DSCI-310/DSCI-310-Group-1

docker build --tag dsci-310-project DSCI-310-Group-1

docker run -it dsci-310-project
```

### Running the tests

To run the tests, please go to the root folder of the project and use the command `pytest`

## Dependencies

- Docker base image: `jupyter/scipy-notebook:hub-2.1.1` 

- Python dependencies:

  | Package      | Version |
  | ------------ | ------- |
  | pandas       | >= 1.3.0 |
  | matplotlib   | >= 3.4.0 |
  | scikit-learn | >= 1.0.0 |
  | numpy        | >= 1.2.0 |
  | pytest       | >= 7.0.1 |



---

*DSCI-310-Group1-Project Report © 2022 by DSCI-310-Gr1 is licensed under CC BY-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/*.

*DSCI-310-Group1-Project Code © 2022 by DSCI-310-Gr1 is licensed under MIT. To view a copy of this liscence, visit https://github.com/DSCI-310/DSCI-310-Group-1/blob/main/LICENSE.md*.
