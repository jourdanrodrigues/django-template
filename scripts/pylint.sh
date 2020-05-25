#!/usr/bin/env sh

for plugin in pylint_django pylint_django.checkers.db_performance; do
  PLUGINS="${PLUGINS} --load-plugins ${plugin}"
done

echo 'Gathering Python files for PyLint...'
FILES=$(find . -type f -name "*.py" ! -path "./manage.py" ! -path "./app/tests/*" ! -path "./app/migrations/*" ! -path "./core/tests.py")

echo 'Running PyLint...'
pylint ${PLUGINS} ${FILES} --rcfile=setup.cfg -j 4
