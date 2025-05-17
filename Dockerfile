FROM python:3.13.3-slim-bullseye

ENV UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /app/

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends curl gettext libpq-dev g++ libffi-dev

RUN curl -LsSf https://astral.sh/uv/0.7.3/install.sh | sh && \
    ln -s /root/.local/bin/uv /usr/local/bin/uv

COPY ./uv.lock ./pyproject.toml ./

RUN uv sync --locked --no-cache && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN SECRET_KEY=dummy ./manage.py compilemessages
