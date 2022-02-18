# Use anaconda3 as the base image
FROM continuumio/anaconda3

#install python packages
RUN conda install -c conda-forge matplotlib \
    pandas \
    scikit-learn \
    numpy