from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_notification_email(email, robot_model, robot_serial):
    subject = "Уведомление о наличии робота"
    message = render_to_string(
        "notification_email.html",
        {"robot_model": robot_model, "robot_version": robot_serial},
    )
    plain_message = strip_tags(message)
    from_email = "admin@example.com"

    send_mail(subject, plain_message, from_email, [email], html_message=message)
