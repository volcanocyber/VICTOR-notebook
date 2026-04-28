# VICTOR hub Image Template :paperclip:

This is the VICTOR image template for our hub hosted by 2i2c. Our machines host a number of computational models for various uses in the volcanology community. This image supports both conda (python) and R interactable coding environemnts, and will soon support a set of geoscience modeling tools on a virtual desktop, including QGIS and and Paraview. If further questions arise, please contact *victor@ldeo.columbia.edu* for additional project information and machine specific issues, and *support@2i2c.org* for platform-wide queries. Below, a brief outline of the technology behind this project, as well as some key links.

### In-depth guide

Checkout the 2i2c docs for an in-depth guide on how to use this template repository to create a custom user image and use it for your hub :arrow_right: https://docs.2i2c.org/en/latest/admin/howto/environment/hub-user-image-template-guide.html.

## About this template repository :information_source:

This template repository enables [jupyterhub/repo2docker-action](https://github.com/jupyterhub/repo2docker-action).
This GitHub action builds a Docker image using the contents of this repo and pushes it our the [Quay.io](https://quay.io/repository/volcanocyber/victor-notebook) repository.

### The environment

The repository defines several `environment.yml` files. These are compiled into a single-platform lockfile with `conda-lock`, e.g.
```shell
conda-lock -f ./environment-core.yml -f ./environment-geo.yml -f ./environment-mlviz.yml -p linux-64 -k explicit
```

The `repo2docker-action` will update the [base repo2docker](https://github.com/jupyterhub/repo2docker/blob/HEAD/repo2docker/buildpacks/conda/environment.yml) conda environment with the packages listed in this `environment.yml` file.

**Note:**
A complete list of possible configuration files that can be added to the repository and be used by repo2docker to build the Docker image, can be found in the [repo2docker docs](https://repo2docker.readthedocs.io/en/latest/config_files.html#configuration-files).   
