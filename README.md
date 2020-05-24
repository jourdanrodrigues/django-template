# {{ project_name }}

_Generated from [this Django template][template-link]._

This project runs entirely on Docker containers. Make sure to [have it][docker-download] in your environment.

## Using this template

_Note_: If you intend to create an API, [head here][django-rest-template].

Run the following to create a Django project with this repo as template:

```bash
$ pip install django
$ mkdir [your_project_name]
$ python -m django startproject \
  --template=https://github.com/jourdanrodrigues/django-template/archive/master.zip \
  --extension=po,yml,md,py \
  ${_} ./${_}
$ # If it doesn't work, try "python2" or "python3" instead of "python".
```

You may remove this section from the `README.md` generated for your project.

## Setting up development environment

Before doing anything, run the following:

```bash
./scripts/setup_dev_env.sh
```

## Database

This project is setup on top of PostgreSQL, and the connection is established through an environment variable
called DATABASE_URL. For more details, check the files [.env.example](.env.example) and
[docker-compose.yml](docker-compose.yml).

## Running the app

To make your life slightly easier, the script [`compose.sh`](compose.sh) is there for you to run commands in your
container. It's just a wrapper for `docker-compose`, so you might want to take a look at
[its documentation][docker-compose-docs].

### Production mode

```bash
./compose.sh up
```

### Development mode

```bash
./compose.sh dev up
```

[template-link]: https://github.com/jourdanrodrigues/django-template
[docker-download]: https://www.docker.com/community-edition#/download
[docker-compose-docs]: https://docs.docker.com/compose/reference/
[django-rest-template]: https://github.com/jourdanrodrigues/django-template/blob/django-rest/README.md
