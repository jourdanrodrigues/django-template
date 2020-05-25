# {{ project_name }}

_Generated from [Jourdan's Django template][template-link]._

This project runs entirely on Docker containers. Make sure to [have it][docker-download] in your environment.

## Setting up development environment

Before doing anything, run the following:

```bash
./scripts/setup_dev_env.sh
```

## Database

This project depends on PostgreSQL and the connection is established through an environment variable called
DATABASE_URL. Check the files [.env.example](.env.example) and [docker-compose.yml](docker-compose.yml) for details.

## Running the app

The script [`compose.sh`](compose.sh) is there for you to run commands in the container. It's just a wrapper for
 `docker-compose`, so you might want to take a look at [its documentation][docker-compose-docs].

```bash
./compose.sh up
```

### `./compose.sh` shortcuts

The script has the same API as docker-compose, with a few adjustments:

```bash
# Running development setup
./compose.sh dev up  # becomes the below
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

# "run"
./compose.sh run server sh  # becomes the below
docker-compose run --rm server sh

# Scripts
./compose.sh run ./scripts/pylint.sh  # becomes the below
docker-compose run --rm server ./scripts/pylint.sh

# "manage.py" commands
./compose.sh run manage.py test  # becomes the below
docker-compose run --rm server python manage.py test
```

- `~ dev ~` = `~ -f docker-compose.yml -f docker-compose.dev.yml ~`
- `~ run ~` = `~ run --rm ~`
- `~ ./scripts/* ~` = `~ server ./scripts/* ~`
- `~ manage.py ~` = `~ server manage.py ~`

[template-link]: https://github.com/jourdanrodrigues/django-template
[docker-download]: https://www.docker.com/community-edition#/download
[docker-compose-docs]: https://docs.docker.com/compose/reference/
