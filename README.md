# {{ project_name }}

### Using this template

Run the following to create a Django project with this repo as template:

```bash
pip install django
mkdir <your_project_name> && django-admin startproject \
  --template=https://github.com/jourdanrodrigues/django-template/archive/master.zip \
  --extension=po,yml,md,py \
  ${_} ./${_}
```

You may remove this section from the `README.md` generated for your project.  

### Setup development environment

Before doing anything, run the following:

```bash
./bin/setup_dev_env.sh
```

### Running the server

```bash
./run.sh up # run with "-d" for detached
```
