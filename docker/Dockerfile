FROM osgeo/gdal:ubuntu-full-3.4.1

# ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
# RUN chmod +x /tini
RUN apt update \
  && apt install -y --fix-missing --no-install-recommends \
    python3-pip cython3 python3-numpy python3-matplotlib python3-dev \
    # developer convenience
    postgresql-client-12 \
    postgresql-12 \
    less \
    wget \
    curl \
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
  && rm -rf /var/lib/apt/lists/*
RUN pip install pip-tools

COPY requirements.in /
RUN pip-compile --verbose \
  --extra-index-url=https://google-coral.github.io/py-repo/ \
  --extra-index-url=https://packages.dea.ga.gov.au \
  /requirements.in
# RUN pip install -r /requirements.txt

# COPY requirements2.in /
# RUN pip-compile --verbose \
#   --extra-index-url=https://google-coral.github.io/py-repo/ \
#   --extra-index-url=https://packages.dea.ga.gov.au \
#   /requirements2.in

# RUN jupyter labextension install jupyterlab-theme-toggle
# RUN jupyter server extension enable --py --sys-prefix jupyterlab_iframe jupyter_resource_usage

# ARG nb_user=jovyan
# ARG nb_uid=1000
# ARG nb_gid=100
# RUN useradd -m -s /bin/bash -N -g $nb_gid -u $nb_uid $nb_user

# RUN echo "Patching python env - hdstats" \
#   && pip install --force-reinstall \
#   --extra-index-url="https://packages.dea.ga.gov.au" hdstats==0.1.8.post1

# COPY assets/sync_repo assets/with_bootstrap assets/jupyterhub-singleuser /usr/local/bin/
# COPY assets/overrides.json $py_env_path/share/jupyter/lab/settings/

# WORKDIR "/home/$nb_user"

# ARG WITH_SUDO="no"
# RUN if [ "$WITH_SUDO" = "yes" ]; then \
#   echo "${nb_user} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
# ;fi

# USER $nb_user

# ENTRYPOINT ["/bin/tini", "-s", "--", "with_bootstrap"]
# CMD ["jupyter", "lab", \
# "--ip=0.0.0.0", \
# "--port=9988", \
# "--no-browser"]
