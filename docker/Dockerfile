FROM ghcr.io/osgeo/gdal:ubuntu-full-3.8.5

ENV SHELL=bash \
    DEBIAN_FRONTEND=non-interactive \
    USE_PYGEOS=0 \
    SPATIALITE_LIBRARY_PATH='mod_spatialite.so'

RUN apt update \
  && apt remove -y python3-numpy \
  && apt install -y curl \
  && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
  && apt install -y --fix-missing --no-install-recommends \
    python3-full python3-dev python3-venv python3-pip \
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
    libhdf5-serial-dev \
    # install ffmpeg the normal way
    ffmpeg \
    # Spatialite support
    libsqlite3-mod-spatialite \
    nodejs \
    # install texlive
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
  && apt clean autoclean \
  && apt autoremove \
  && rm -rf /var/lib/{apt,dpkg,cache}/

# Install tini
RUN wget -O /bin/tini https://github.com/krallin/tini/releases/download/v0.19.0/tini && \
  chmod +x /bin/tini

# Install yq
RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq &&\
  chmod +x /usr/bin/yq

# install pandoc 3.4.1
RUN wget https://github.com/jgm/pandoc/releases/download/3.4/pandoc-3.4-1-amd64.deb \
  && apt --fix-broken install \
  && dpkg -i pandoc-3.4-1-amd64.deb \
  && rm pandoc-3.4-1-amd64.deb

COPY requirements.txt /

# Create a non-root user
ARG nb_user=jovyan
ARG nb_uid=1000
ARG nb_gid=100
RUN useradd -m -s /bin/bash -N -g $nb_gid -u $nb_uid $nb_user

# Set up the python virtual environment PEP 668.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Change ownership of virtual environment folder from root to non-root user
RUN chown -R $nb_uid:$nb_gid  $VIRTUAL_ENV

USER $nb_user
RUN python -m pip install --upgrade pip pip-tools
RUN pip install --no-cache-dir -r requirements.txt
RUN jupyter server extension enable --py --sys-prefix jupyterlab_iframe jupyter_resource_usage

USER root
COPY assets/sync_repo assets/with_bootstrap assets/jupyterhub-singleuser /usr/bin/
COPY assets/overrides.json $VIRTUAL_ENV/share/jupyter/lab/settings/
COPY assets/jupyter_lab_config.py /etc/jupyter/

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
