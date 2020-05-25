FROM python:3.8-alpine

WORKDIR /app/

RUN apk add -qU --no-cache postgresql-libs gettext && \
    apk add -q --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

COPY . .

RUN SECRET_KEY=dummy ./manage.py collectstatic --no-input
RUN SECRET_KEY=dummy ./manage.py compilemessages
