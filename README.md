# {{ project_name }}

_Generated from [Jourdan's Django template](https://github.com/jourdanrodrigues/django-template)._

This project runs entirely on Docker containers. Make sure to [have it](https://www.docker.com/community-edition#/download) in your environment.

## Linter

This projects makes use of [`pre-commit`](https://pre-commit.com/#install). Make sure it's installed in your dev-environment with the following command:

```bash
pre-commit install
```

## Database

This project depends on PostgreSQL and the connection is established through an environment variable called
DATABASE_URL. Check the files [.env.example](.env.example) and [docker-compose.yml](docker-compose.yml) for details.

## Running the app

We use a compose project to build and run the necessary containers. Take a look at [its documentation](https://docs.docker.com/compose/reference/).

```bash
docker compose up
```
