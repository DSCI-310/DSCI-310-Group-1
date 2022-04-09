# Use scipy notebook as default 
FROM jupyter/scipy-notebook:hub-2.1.1

#install python packages
RUN conda install -c conda-forge matplotlib>=3.4.0 \
    pandas>=1.4.0 \
    scikit-learn>=1.0.0 \
    numpy>=1.21.0 \
    docopt>=0.6.2 \
    jupyter-book>=0.12.2 

#install custom package
RUN pip install grouponefunctions