#!/usr/bin/env bash

function print_green () {
  printf "\033[92m${1}\033[0m\n"
}

function print_blue () {
  printf "\033[94m${1}\033[0m\n"
}

PROJECT_PATH=$(dirname $(dirname ${0}))

PIP_BIN=$(which pip)

if [ ! ${?} -eq 0 ]; then
  print_blue 'Installing "pip"...'
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py && rm get-pip.py

  PIP_BIN=$(which pip)
fi

which flake8 > /dev/null

if [ ! ${?} -eq 0 ]; then
  print_blue 'Installing "flake8"...'
  ${PIP_BIN} install flake8 flake8-commas
fi


GIT_HOOKS_PATH=${PROJECT_PATH}/.git/hooks

if [ ! -f ${GIT_HOOKS_PATH}/pre-commit ]; then
  print_blue 'Putting "pre-commit" hook in place...'
  cp ${PROJECT_PATH}/.hooks/pre-commit ${GIT_HOOKS_PATH}
fi

DOT_ENV=${PROJECT_PATH}/.env

if [ ! -f ${DOT_ENV} ]; then
  print_blue 'Creating ".env" file...'
  echo "SECRET_KEY=$(python ${PROJECT_PATH}/bin/generate_secret_key.py)" > ${DOT_ENV}
fi

print_green 'All good!'
