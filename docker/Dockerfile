FROM osgeo/gdal:ubuntu-full-3.6.3

ENV SHELL=bash

ENV DEBIAN_FRONTEND=non-interactive

RUN apt update \
  && apt install -y curl \
  && apt remove -y python3-numpy \
  && curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
  && apt update \
  && apt install -y --fix-missing --no-install-recommends \
    python3-pip python3-dev \
  && python -m pip install --upgrade pip \
  && apt update \
  && apt install -y --fix-missing --no-install-recommends \
    # developer convenience
    postgresql-client \
    postgresql \
    less \
    wget \
    vim \
    tmux \
    htop \
    fish \
    tig \
    git \
    jq \
    xz-utils \
    zip \
    unzip \
    file \
    time \
    openssh-client \
    graphviz \
    sudo \
    iproute2 \
    iputils-ping \
    net-tools \
    simpleproxy \
    rsync \
    libtiff-tools \
    # rgsislib dependencies
    libboost-date-time1.74.0 \
    libboost-dev \
    libboost-filesystem1.74.0 \
    libboost-system1.74.0 \
    libcgal-dev \
    libgsl-dev \
    libgeos-dev \
    libmuparser2v5 \
    libpq-dev \
    libproj-dev \
    # for cython to work need compilers
    build-essential \
    # for pyRAT install or something
    libfftw3-dev \
    liblapack-dev \
    # install libhdf5
    libhdf5-serial-dev\
    # install ffmpeg the normal way
    ffmpeg \
    nodejs \
    # install texlive
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic\
  && apt clean autoclean \
  && apt autoremove \
  && rm -rf /var/lib/{apt,dpkg,cache}/

COPY requirements0.txt /
COPY requirements.txt /

# install pytables 3.6.1
ENV HDF5_DIR=/usr/lib/x86_64-linux-gnu/hdf5/serial/
RUN pip install Cython && pip install numpy
RUN wget -O pytables.zip https://github.com/PyTables/PyTables/archive/refs/tags/v3.6.1.zip
RUN unzip pytables.zip
WORKDIR "/PyTables-3.6.1"
RUN python3 setup.py bdist_wheel
RUN cd dist/ && python -m pip install tables-3.6.1-cp310-cp310-linux_x86_64.whl
WORKDIR "/../.."
RUN rm -rf PyTables-3.6.1 pytables.zip

# install pandoc 3.1.2
RUN wget https://github.com/jgm/pandoc/releases/download/3.1.2/pandoc-3.1.2-1-amd64.deb
RUN dpkg -i pandoc-3.1.2-1-amd64.deb
RUN rm pandoc-3.1.2-1-amd64.deb

RUN pip install -r /requirements0.txt && pip install -r /requirements.txt && rm -rf /root/.cache/pip

RUN jupyter labextension install jupyterlab-theme-toggle
RUN jupyter server extension enable --py --sys-prefix jupyterlab_iframe jupyter_resource_usage

COPY assets/sync_repo assets/with_bootstrap assets/jupyterhub-singleuser /usr/bin/
COPY assets/overrides.json /env/share/jupyter/lab/settings/

ARG nb_user=jovyan
ARG nb_uid=1000
ARG nb_gid=100
RUN useradd -m -s /bin/bash -N -g $nb_gid -u $nb_uid $nb_user

RUN wget -O /bin/tini https://github.com/krallin/tini/releases/download/v0.19.0/tini && \
  chmod +x /bin/tini

WORKDIR "/home/$nb_user"

ARG WITH_SUDO="no"
RUN if [ "$WITH_SUDO" = "yes" ]; then \
  echo "${nb_user} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
;fi

USER $nb_user

ENTRYPOINT ["/bin/tini", "-s", "--", "with_bootstrap"]
CMD ["jupyter", "lab", \
"--ip=0.0.0.0", \
"--port=9988", \
"--no-browser"]

