# Use scipy notebook as default 
FROM jupyter/scipy-notebook:hub-2.1.1

COPY . .

#install python packages
RUN conda install -c conda-forge matplotlib>=3.4.0 \
    pandas>=1.3.0 \
    scikit-learn>=1.0.0 \
    numpy>=1.2.0 \
    pytest>=7.0.1 \
    docopt>=0.6.2 \
    jupyter-book>=0.7.4 \
