#!/usr/bin/env python
import os
import stat
import sys
from os import path
from shutil import copyfile

from django.core.management.utils import get_random_secret_key

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def create_dot_env():
    try:
        with open(path.join(ROOT_PATH, '.env'), 'x') as dot_env:
            dot_env.write(f'SECRET_KEY={get_random_secret_key()}')
    except FileExistsError:
        pass


def copy_executable(src, dst):
    copyfile(src, dst)
    os.chmod(dst, os.stat(dst).st_mode | stat.S_IEXEC)


def place_git_hooks():
    git_hooks_path = path.join(ROOT_PATH, '.git', 'hooks')
    if path.exists(git_hooks_path) and not path.exists(path.join(git_hooks_path, 'pre-commit')):
        hooks_path = path.join(ROOT_PATH, 'scripts', 'hooks')
        copy_executable(os.path.join(hooks_path, 'pre-push'), os.path.join(git_hooks_path, 'pre-push'))
        copy_executable(os.path.join(hooks_path, 'pre-commit'), os.path.join(git_hooks_path, 'pre-commit'))


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

    create_dot_env()
    place_git_hooks()

    execute_from_command_line(sys.argv)
