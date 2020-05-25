# Django Template

This project runs entirely on Docker containers. Make sure to [have it][docker-download] in your environment.

## Creating a project

We have 2 versions of this template: one for using a bare Django project and another for REST API services:

- Bare Django template: https://github.com/jourdanrodrigues/django-template/archive/django.zip
- REST API template: https://github.com/jourdanrodrigues/django-template/archive/django-rest.zip

Pick the template URL you need and replace the `[ZIP_FILE]` below with it:

```bash
$ pip install django
$ mkdir [your_project_name]
$ python -m django startproject --template=[ZIP_FILE] --extension=po,yml,md,py ${_} ./${_}
```

Note: You might have to use "python2" or "python3" instead of "python" in the command above depending on your
environment.
