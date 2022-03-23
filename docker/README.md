# Sandbox Docker

- Uses `osgeo/gdal` images as base
- Username is `jovyan` to match "typical python notebook dockers"
- The Python environment is global, and the `jovyan` user has access to it's own home directory.
- This is a complete system, so a user can access anything available.


### Extending

Currently all libraries are pre-compiled into a single list. We are using
the file `requirements.in` as the required libraries to install, if any new
libraries are required it can be added to this file. Note that any changes to
the `requirements.in` file will not be taken into account until after you run
the command `pip-compile` that is available in the `Makefile`.

If it's only single libraries that you want to add, then you can add it right
after the current `pip install`.

For other `jupyterlab` extensions this can be added to the `Dockerfile` after
where it currently has them.
