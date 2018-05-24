#!/usr/bin/env bash

if [ "${1}" = '-h' ]; then
  echo "${0} [compose args]"
  exit 0
fi

COMMAND='docker-compose'

if [ "${1}" = 'run' ]; then
  shift
  COMMAND="${COMMAND} run --rm"
fi

${COMMAND} ${@}
