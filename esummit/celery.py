import os
from celery import Celery

if os.environ.get('ENVIRONMENT') == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esummit.setting.production')
else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esummit.setting.devlopment')
app = Celery("esummit")
app.config_from_object("django.conf:settings", namespace="CELERY")
import user.tasks
app.autodiscover_tasks()