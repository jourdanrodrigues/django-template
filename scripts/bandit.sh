#!/usr/bin/env sh

echo 'Running Bandit...'

bandit -r . -x ./app/tests
