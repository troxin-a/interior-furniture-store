from django.core.mail import send_mail

def send_email(
    "Subject here",
    "Here is the message.",
    "from@example.com",
    ["troxin@yandex.ru"],
    fail_silently=False,
)
