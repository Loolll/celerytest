from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set default settings to celery from django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

app = Celery('weather')
app.config_from_object('django.conf::settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def task(self):
    print('Request: {0!r}'.format(self.request))