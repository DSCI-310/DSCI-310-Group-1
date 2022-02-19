# Use anaconda3 as the base image
FROM continuumio/anaconda3

#install python packages
RUN conda install -c conda-forge matplotlib=3.5.1 \
    pandas=1.4.1 \
    scikit-learn=1.0.2 \
    numpy=1.21.2