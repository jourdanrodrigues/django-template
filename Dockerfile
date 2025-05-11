FROM python:3.13.3-slim-bullseye

WORKDIR /app/

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends libpq-dev g++ libffi-dev \

RUN curl -LsSf https://astral.sh/uv/0.7.3/install.sh | sh

COPY uv.lock pyproject.toml ./

RUN uv sync --no-cache && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN SECRET_KEY=dummy ./manage.py compilemessages
