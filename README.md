# streamlitnginx

## Description
This is a blueprint for a streamlit app that can be used with a Nginx reverse proxy. It will enable the user to use streamlit with SSL certificates and therefore encrypt the data transfer.

It contains these elements:
- A sample streamlit app "sample/ui.py"
- Configfiles for streamlit "config/config.toml" and Nginx "config/streamlitnginxconf"
- Certificates (Public & Private) "certificates/" (need to be replaced with own certificates)
- A dockerfile "Dockerfile" that builds a container

It is inspired by this [tutorial](https://ngbala6.medium.com/deploy-streamlit-app-on-nginx-cfa327106050).

## Implementation
The first step is to clone the repository:

    git clone https://github.com/dpleus/streamlitnginx.git

Second step is executing the Docker container. Docker needs to be preinstalled. https://docs.docker.com/get-docker/

    docker run . -p 9000:9000

You will be able to access the app via: https://localhost:9000
