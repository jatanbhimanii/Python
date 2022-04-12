from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'jaybhimani',
    ['lucifergame234@gmail.com'],
    fail_silently=False,
)