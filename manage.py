#!/usr/bin/env python
import os
import sys
from django.core.management.utils import get_random_secret_key

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        message = (
            "Couldn't import Django. Are you sure it's installed and "
            'available on your PYTHONPATH environment variable? Did you '
            'forget to activate a virtual environment?'
        )
        raise ImportError(message) from exc

    try:
        with open('.env', 'x') as dot_env:
            dot_env.write(f'SECRET_KEY={get_random_secret_key()}')
    except FileExistsError:
        pass

    execute_from_command_line(sys.argv)
