#!/usr/bin/env bash

if [ "${1}" = '-h' ]; then
  echo "${0} [any command] [test]"
  exit 0
elif [ "${1}" = 'test' ]; then
  COMMAND="python manage.py test"
else
  COMMAND=${@}
fi

docker-compose run --rm server ${COMMAND}
