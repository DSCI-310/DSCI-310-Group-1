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

We test the model with cross validation and get an average cv-score of -4.61, which means an error of 4.61 and a final RMSE error of 3.83. As the final grade `G3` is in a 20 point scale, we find that an error of 3.83 roughly equates to an average of a 19.15 percent difference between your predicted grade and the actual grade. In other words, your actual grade may be about a letter grade off of what it actually is. As such, we see that there is clear difficulty in trying to predict student grades using mostly demographic features.



## How to run?




### Clone the repository

The first step to running our analysis is to clone the repository using the git clone command below, and navigate to the repository.

```
git clone https://github.com/DSCI-310/DSCI-310-Group-1

cd DSCI-310-Group-1
```

### From DockerHub

Our project is published at Dockerhub. Thus, it is convenient to run our repository directly in the terminal. Execute the following command:

```
docker pull danielhou13/dsci-310-project:latest

<!-- Powershell -->
docker run --rm -p 8888:8888 -v ${PWD}:/home/jovyan/work danielhou13/dsci-310-project:latest

<!-- Git Bash -->
docker run --rm -p 8888:8888 -v /$(pwd):/home/jovyan/work danielhou13/dsci-310-project:latest
```
Afterwards you will find that there is a command in the terminal that looks something like this: http://127.0.0.1:8888/lab?token={TOKEN}. Copy paste it into your web browser of choice to load our notebook. Note, if you have another instance of Jupyter Lab open, it may cause issues.

Once you are in Jupyter Lab, please open the terminal and run the following command:

```
pip install grouponefunctions
```

This will install the necessary functions to run our analysis.

### Build using the Dockerfile
Alternatively, if the first method does not work, then you can use the following commands to build the docker image via the dockerfile and run our analysis in this manner. You can open Jupyter Lab in the same manner as the previous method.

```
docker build -t dsci-310-group-1 .

<!-- Powershell -->
docker run --rm -p 8888:8888 -v ${PWD}:/home/jovyan/work dsci-310-group-1

<!-- Git Bash -->
docker run --rm -p 8888:8888 -v /$(pwd):/home/jovyan/work dsci-310-group-1
```
**Note**: you do not need to run `pip install grouponefunctions` using this method as the dockerfile will install it for you.

### Running via Makefile

The analysis can be run using the makefile with the command `make all` after using the command `cd work` in the Jupyter Terminal. That takes you to the root folder of the analysis, where the commands for both the tests and the makefile can be run. After you run the makefile using `make all`, you can see the results of our analysis by going to your LOCAL repository at **results/report/index.html**, and opening the html file there. After opening using index.html, you can navigate to different parts of our analysis using the sidebar.

If you are getting an error, please run make clean first, before runnning make all.

### Running the tests

To run the tests, please go to the root folder of the project and use the command `pytest`.

## Dependencies

- Docker base image: `jupyter/scipy-notebook:hub-2.1.1` 

- Python dependencies:

  | Package      | Version |
  | ------------ | ------- |
  | python | >= 3.9.10 |
  | pandas       | >= 1.3.0 |
  | matplotlib   | >= 3.4.0 |
  | scikit-learn | >= 1.0.0 |
  | numpy        | >= 1.2.0 |
  | pytest       | >= 7.0.1 |
  | docopt       | >= 0.6.2 |
  | jupyter-book | >= 0.12.2 |
  | grouponefunctions | >= 0.1.4 |

You can find the documentation for our specialized package "grouponefunctions" here: https://github.com/DSCI-310/DSCI_310_group_1_package

---

[![License: CC BY-SA  4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/) *DSCI-310-Group1-Project Report © 2022 by DSCI-310-Gr1 is licensed under CC BY-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/*.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) *DSCI-310-Group1-Project Code © 2022 by DSCI-310-Gr1 is licensed under MIT. To view a copy of this liscence, visit https://github.com/DSCI-310/DSCI-310-Group-1/blob/main/LICENSE.md*.
