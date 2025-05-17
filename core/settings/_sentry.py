import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from core.settings._environment import SENTRY_DSN, SENTRY_ENV

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        environment=SENTRY_ENV,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1,
        send_default_pii=True,
    )
