import json
import os

from core.helpers import DotEnvReader


def bool_env(key, default: bool) -> bool:
    value = os.getenv(key)
    return json.loads(value) if value in ['true', 'false'] else default


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DotEnvReader(os.path.join(BASE_DIR, '.env')).read()

SECRET_KEY = os.getenv('SECRET_KEY')

PRODUCTION = bool_env('PRODUCTION', False)
DEBUG = bool_env('DEBUG', not PRODUCTION)

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '' if PRODUCTION else '*').split(',')
