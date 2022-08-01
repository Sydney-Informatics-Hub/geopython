#To build this docker file
#docker build -t nbutter/geopy:pesa2022 .
#To push to dockerhub
#docker push nbutter/geopy:pesa2022
#To run this with an interactive notebook:
#docker run -p 8888:8888 -it --rm nbutter/geopy:pesa2022 /bin/bash  -c "jupyter notebook --allow-root --ip=0.0.0.0 --no-browser"

FROM ubuntu:focal
MAINTAINER Nathaniel Butterworth

RUN apt-get update -y && \
	apt-get install git curl unzip -y && \
	rm -rf /var/lib/apt/lists/*

ENV PATH="/build/miniconda3/bin:${PATH}"
ARG PATH="/build/miniconda3/bin:${PATH}"

WORKDIR /build

RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh &&\
	mkdir /build/.conda && \
	bash Miniconda3-py39_4.11.0-Linux-x86_64.sh -b -p /build/miniconda3 &&\
	rm -rf /Miniconda3-py39_4.11.0-Linux-x86_64.sh

RUN conda install -c conda-forge python=3.9 pip=22.2 matplotlib=3.5 numpy=1.23 pygmt=0.7 seaborn=0.11 obspy=1.3 tensorflow=2.6 pyshp=2.3 mpi4py=3.1 scikit-learn=1.1 scipy=1.8 dask=2022.7 cartopy=0.20 upsetplot=0.6 pandas=1.4  jupyter=1.0 python-graphviz=0.20
RUN pip install lasio==0.30

RUN mkdir /data /notebooks
RUN cd /data && \
	curl -O https://cloudstor.aarnet.edu.au/plus/s/91HrHFMl4zWANZ6/download && \
	unzip download -d / && rm -rf download

RUN cd /notebooks && \
	curl -O https://cloudstor.aarnet.edu.au/plus/s/BkeCEYooVLyuLvm/download && \
	unzip download -d /notebooks && rm -rf download

WORKDIR /notebooks

CMD /bin/bash
