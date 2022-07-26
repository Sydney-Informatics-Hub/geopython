
FROM ubuntu:bionic
MAINTAINER Nathaniel Butterworth

RUN apt-get update -y && \
	apt-get install git curl unzip -y && \
	rm -rf /var/lib/apt/lists/*

ENV PATH="/build/miniconda3/bin:${PATH}"
ARG PATH="/build/miniconda3/bin:${PATH}"

WORKDIR /build

RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh &&\
	mkdir /build/.conda && \
	bash Miniconda3-py37_4.8.3-Linux-x86_64.sh -b -p /build/miniconda3 &&\
	rm -rf /Miniconda3-py37_4.8.3-Linux-x86_64.sh

WORKDIR /build

#conda create -n geopy python=3.7
#conda activate geopy

RUN conda install pip
RUN pip install numpy==1.18 pandas==1.0.1 matplotlib==3.3.2 pyshp==2.1.2 lasio==0.28 scipy==1.4.1 scikit-learn==0.23 
RUN conda install -c conda-forge cartopy=0.18
RUN conda install -c conda-forge obspy=1.2.2
RUN pip install tensorflow==2.3 
RUN python -m pip install dask==2.30
RUN pip install jupyter==1.0

RUN mkdir /data /notebooks 
RUN cd /data && \
	curl -O https://cloudstor.aarnet.edu.au/plus/s/IfOvRpOXhJyqTT0/download && \
	unzip download -d / && rm -rf download

WORKDIR /notebooks

CMD /bin/bash 
