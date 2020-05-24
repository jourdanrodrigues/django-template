#!/usr/bin/env sh

bandit -r . -x ./app/tests,./venv
