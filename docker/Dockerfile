FROM osgeo/gdal:ubuntu-full-3.4.2

RUN apt update \
  && apt install -y curl \
  && apt remove -y python3-numpy \
  && curl -fsSL https://deb.nodesource.com/setup_12.x | bash - \
  && apt update \
  && apt install -y --fix-missing --no-install-recommends \
    python3-pip python3-dev \
    # developer convenience
    postgresql-client-12 \
    postgresql-12 \
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
    libboost-date-time1.71.0 \
    libboost-dev \
    libboost-filesystem1.71.0 \
    libboost-system1.71.0 \
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
     #install ffmpeg the normal way
    ffmpeg \
    nodejs \
  && apt clean autoclean \
  && apt autoremove \
  && rm -rf /var/lib/{apt,dpkg,cache}/

COPY requirements.txt /
RUN pip install -r /requirements.txt && rm -rf /root/.cache/pip

RUN wget -O /tmp/main.zip https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/archive/refs/heads/main.zip && \
  unzip /tmp/main.zip -d /tmp && \
  pip install -e /tmp/deafrica-sandbox-notebooks-main/Tools/ && \
  rm -rf /tmp/main.zip /tmp/deafrica-sandbox-notebooks-main

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
