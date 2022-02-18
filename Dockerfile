# Use anaconda3 as the base image
FROM continuumio/anaconda3

# RUN conda install -y -c pandas \
#     matplot \
#     scikit-learn

RUN conda install -c conda-forge matplotlib \
    pandas\
    scikit-learn
    