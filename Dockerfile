# Use anaconda3 as the base image
FROM continuumio/anaconda3

#install python packages
RUN conda install -c conda-forge matplotlib>=3.4.0 \
    pandas>=1.3.0 \
    scikit-learn>=1.0.0 \
    numpy>=1.2.0 \
    Jupyter \
    Jupyterlab=3.2.6

# Install JupyterLab Git Extension
RUN pip install jupyterlab-git

# Make port 8888 available for JupyterLab
EXPOSE 8888
