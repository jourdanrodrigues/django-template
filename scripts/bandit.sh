#!/usr/bin/env sh

echo 'Running Bandit...'

bandit --quiet --recursive . --exclude ./app/tests
