# from https://github.com/tash-f/sagemaker-studio-geopy-custom-image/blob/main/Dockerfile
FROM python:3.7

ARG NB_USER="sagemaker-user"
ARG NB_UID="1000"
ARG NB_GID="100"

# Setup the "sagemaker-user" user with root privileges.
RUN \
  apt-get update && \
  apt-get install -y sudo && \
  apt-get install -y libproj-dev proj-data proj-bin && \
  apt-get install -y libgeos++-dev && \
  apt-get install -y python3-dev && \
  useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
  chmod g+w /etc/passwd && \
  # give NB_USER passwordless sudo
  echo "${NB_USER}    ALL=(ALL)    NOPASSWD:    ALL" >> /etc/sudoers && \
  # Prevent apt-get cache from being persisted to this layer.
  rm -rf /var/lib/apt/lists/*

# Copy requirements, install and configure the kernel.
COPY --chown="${NB_UID}:${NB_GID}" "*.txt" "/tmp/"
RUN \
  pip install -r "/tmp/pip_req.txt" && \
  python -m ipykernel install --name 'geopython' --display-name \
  "Python (GeoPython)" --sys-prefix && pip install shapely \
  cartopy==0.18.0 --no-binary shapely --no-binary cartopy

# Make the default shell bash (vs "sh") for a better Jupyter terminal UX
ENV SHELL=/bin/bash

USER $NB_UID

WORKDIR "/home/${NB_USER}"

# download the data
RUN wget -q "https://cloudstor.aarnet.edu.au/plus/s/IfOvRpOXhJyqTT0/download" \
  -O "temp.zip" && unzip -qq "temp.zip" && rm -rf "temp.zip"
