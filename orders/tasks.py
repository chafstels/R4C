from R4C.celery import app
from orders.send_email import send_notification_email


@app.task()
def send_email_task(email, robot_model, robot_serial):
    send_notification_email(email, robot_model, robot_serial)
