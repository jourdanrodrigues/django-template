#!/usr/bin/env sh

./scripts/flake8.sh && ./scripts/bandit.sh && ./scripts/pylint.sh

exit ${?}
