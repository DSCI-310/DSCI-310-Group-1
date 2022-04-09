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

We test the model with cross validation and examine the average cv-score and final RMSE error. We expect the numeric figures to vary upon each round of replication. However, most of our results suggest that the actual grade may be about a letter grade off of what it actually is. As such, we see that there is clear difficulty in trying to predict student grades using mostly demographic features. 



## How to run?

Replicating our analysis is possible. Follow the instructions below to produce your own version of the report.


### Clone the repository

The first step to running our analysis is to clone the repository using the git clone command below, and navigate to the repository.

```bash
git clone https://github.com/DSCI-310/DSCI-310-Group-1

cd DSCI-310-Group-1
```

### From DockerHub

Our project is published at Dockerhub. Thus, it is convenient to run our repository directly in the terminal. Execute the following command:

#### 1. Achieve the Docker image

```bash
docker pull danielhou13/dsci-310-project:latest
```

#### 2. Run the environment for analysis

```bash
# For Powershell 
docker run --rm -p 8888:8888 -v ${PWD}:/home/jovyan/work danielhou13/dsci-310-project:latest

# For Git Bash, Linux or Mac
docker run --rm -p 8888:8888 -v /$(pwd):/home/jovyan/work danielhou13/dsci-310-project:latest
```
Afterwards you will find that there is a command in the terminal that looks something similar to `http://127.0.0.1:8888/lab?token={TOKEN}`. Copy paste it into your web browser of choice to load our notebook. Note, if you have another instance of Jupyter Lab open, it may cause issues.

### Build using the Dockerfile
Alternatively, if the first method does not work, then you can use the following commands to build the docker image via the dockerfile and run our analysis in this manner. You can open Jupyter Lab in the same manner as the previous method.

```bash
docker build -t dsci-310-group-1 .

# For Powershell
docker run --rm -p 8888:8888 -v ${PWD}:/home/jovyan/work dsci-310-group-1

# For Git Bash, Linux or Mac
docker run --rm -p 8888:8888 -v /$(pwd):/home/jovyan/work dsci-310-group-1
```
### Running via Makefile

When you successfully enter the interface of Jupyter Lab, there are several additional steps to follow to reproduce the report for this analysis.

#### 1. Enter the work directory

Under any `Launcher` tab in Jupyter Lab, select `Terminal` in the `Other` section. Then type input the command:

```bash
cd work
```

That takes you to the root folder of the analysis where the makefile can be run. 

#### 2. Reproduce the report

This analysis can be run using the makefile command. In the terminal, input the command:

```bash
makefile all
```

When the procedure completes, you can view the report of our analysis by openning the `index.html` file locating at `results/report/index.html` in the repository. You can also browse through the raw dataset and intermediate data used for the analysis under the `results/` directory.

If you encountered an error, or wanted to re-run the analysis, make sure to run `make clean` to clean the current work space.

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

Our specialized package `grouponefunctions` includes helper functions that smoothen the reproduceable process. You can find the documentation [here](https://github.com/DSCI-310/DSCI_310_group_1_package).



---

[![License: CC BY-SA  4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/) *DSCI-310-Group1-Project Report © 2022 by DSCI-310-Gr1 is licensed under CC BY-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/*.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) *DSCI-310-Group1-Project Code © 2022 by DSCI-310-Gr1 is licensed under MIT. To view a copy of this liscence, visit https://github.com/DSCI-310/DSCI-310-Group-1/blob/main/LICENSE.md*.
