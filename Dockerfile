# Use scipy notebook as default
FROM jupyter/scipy-notebook

#install python packages
RUN conda install -c conda-forge matplotlib>=3.4.0 \
    pandas>=1.3.0 \
    scikit-learn>=1.0.0 \
    numpy>=1.2.0 \
