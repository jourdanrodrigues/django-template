#!/usr/bin/env bash

if [ "${1}" = '-h' ]; then
  echo "${0} [any command]"
  exit 0
fi

docker-compose run --rm server ${@}
