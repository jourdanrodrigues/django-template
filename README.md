# {{ project_name }}

This project runs entirely on Docker containers. Make sure to [have it][docker-download] in your environment.

## Using this template

Run the following to create a Django project with this repo as template:

```bash
pip install django
mkdir <your_project_name> && django-admin startproject \
  --template=https://github.com/jourdanrodrigues/django-template/archive/master.zip \
  --extension=po,yml,md,py \
  ${_} ./${_}
```

You may remove this section from the `README.md` generated for your project.  

## Setting up development environment

Before doing anything, run the following:

```bash
./bin/setup_dev_env.sh
```

To make your life slightly easier, the script [`run.sh`](run.sh) is there for you to run commands in your container.
It's just a wrapper for the `run` command from `docker-compose`, so you might want to take a look at
[its documentation][docker-compose-run].

### Running the server

```bash
./run.sh up
```

[docker-download]: https://www.docker.com/community-edition#/download
[docker-compose-run]: https://docs.docker.com/compose/reference/run/
