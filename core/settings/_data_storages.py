from dj_database_url import config as database_config
from django_cache_url import config as cache_config

CACHES = {"default": cache_config()}
DATABASES = {"default": database_config()}
