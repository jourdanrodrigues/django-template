import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv


def bool_env(key, default: bool) -> bool:
    value = os.getenv(key)
    return json.loads(value) if value in ["true", "false"] else default


def get_host_env(key: str, default: list[str]) -> list[str]:
    value = os.getenv(key)
    if value:
        return value.split(",")
    return default


BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")

PRODUCTION = bool_env("PRODUCTION", False)
DEBUG = bool_env("DEBUG", not PRODUCTION)
TESTING = "test" in sys.argv

ALLOWED_HOSTS = get_host_env("ALLOWED_HOSTS", [] if PRODUCTION else ["*"])
ALLOWED_CLIENTS = get_host_env("ALLOWED_CLIENTS", [])

SENTRY_DSN = os.getenv("SENTRY_DSN")
SENTRY_ENV = os.getenv("SENTRY_ENV")

if not PRODUCTION and not SECRET_KEY:
    from django.core.management.utils import get_random_secret_key

    SECRET_KEY = get_random_secret_key()
    try:
        with open(BASE_DIR / ".env", "x") as dot_env:
            dot_env.write(f"SECRET_KEY='{SECRET_KEY}'")
    except FileExistsError:
        pass
