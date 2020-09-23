FROM ubuntu:16.04 
# docker build . -t nbutter/daskdev
# docker push nbutter/daskdev
# docker run -it nbutter/daskdev 
# sudo singularity build dask.sing Singularity.dask
# singularity run dask.sing

LABEL MAINTAINER="Nathaniel Butterworth"
LABEL SRC=https://github.com/natbutter/dask
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

LABEL MAINTAINER="Anaconda, Inc"
ENV CONDA_VERSION 4.7.12
ENV CONDA_MD5 0dba759b8ecfc8948f626fa18785e3d8

RUN apt-get update -y && \
	apt-get install -y wget && \
	rm -rf /var/lib/apt/lists/*

# Create non-root user, install dependencies, install Conda
RUN  wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.7.12-Linux-x86_64.sh && \
    echo "${CONDA_MD5}  Miniconda3-4.7.12-Linux-x86_64.sh" > miniconda.md5 && \
    if [ $(md5sum -c miniconda.md5 | awk '{print $2}') != "OK" ] ; then exit 1; fi && \
    mv Miniconda3-$CONDA_VERSION-Linux-x86_64.sh miniconda.sh && \
    mkdir -p /opt && \
    sh ./miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh miniconda.md5 && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> /etc/profile && \
    echo "conda activate base" >> /etc/profile && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

ENV PATH "/bin:/sbin:/usr/bin:/opt/conda/bin"

# Install dask

RUN conda install --yes \
    -c conda-forge \
    python-blosc \
    cytoolz \
    dask==2.10.1 \
    lz4 \
    nomkl \
    numpy==1.17.3 \
    pandas==0.25.2 \
    tini==0.18.0 \
    && rm -rf /opt/conda/pkgs

COPY prepare.sh /usr/bin/prepare.sh

RUN mkdir /opt/app /project /scratch
WORKDIR /project

#ENTRYPOINT ["tini", "-g", "--", "/usr/bin/prepare.sh"]

#CMD [ "sh", "--login", "-i" ]