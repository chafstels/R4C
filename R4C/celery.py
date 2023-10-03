from celery import Celery
from celery.schedules import crontab
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "R4C.settings")

app = Celery("R4C.celery")
app.config_from_object("R4C.celery_config")


app.conf.update(result_expires=3600)


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
