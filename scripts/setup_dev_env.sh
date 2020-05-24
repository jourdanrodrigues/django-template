#!/usr/bin/env bash

function print_green () {
  printf "\033[92m${1}\033[0m\n"
}

function print_blue () {
  printf "\033[94m${1}\033[0m\n"
}

PROJECT_PATH=$(dirname $(dirname ${0}))

DOT_ENV=${PROJECT_PATH}/.env

if [[ ! -f ${DOT_ENV} ]]; then
  print_blue 'Creating ".env" file...'
  echo "SECRET_KEY=$(python ${PROJECT_PATH}/scripts/generate_secret_key.py)" > ${DOT_ENV}
fi

print_green 'All good!'
