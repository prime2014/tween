from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("djapps")


app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()
