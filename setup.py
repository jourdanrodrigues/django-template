from codecs import open
from os import path

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from core.helpers import Installer

project_path = path.abspath(path.dirname(__file__))

try:
    # Get the long description from the README file
    with open(path.join(project_path, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    # When installing dependencies inside a container,
    # this file probably won't be there
    long_description = ''


class DevelopCommand(develop):
    def run(self):
        super().run()
        Installer('gettext').install()


class InstallCommand(install):
    def run(self):
        super().run()
        Installer('gettext').install()


setup(
    name='{{ project_name }}',
    version='0.0.0',
    description='Track your pantry smartly.',
    long_description=long_description,
    classifiers=[],
    packages=find_packages(),
    cmdclass={
        'develop': DevelopCommand,
        'install': InstallCommand,
    },
    install_requires=[
        'dj-database-url==0.4.2',
        'Django==2.0.1',
        'psycopg2==2.7.4',
    ],
)
