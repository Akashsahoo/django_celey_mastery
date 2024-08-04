import os
from datetime import timedelta
from celery import Celery
from sentry_sdk import init
from sentry_sdk.integrations.celery import CeleryIntegration

SENTRY_DSN = os.environ.get("SENTRY_DSN")
init(dsn=SENTRY_DSN,integrations=[CeleryIntegration()])
app = Celery('task')
app.config_from_object('celeryconfig')
app.conf.imports = ('newapp.tasks')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task1':{
        'task': 'newapp.tasks.check_webpage',
        'schedule': timedelta(seconds=30)
    }
}