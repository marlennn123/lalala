from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.core.mail import send_mail

@receiver(user_signed_up)
def send_signup_email(sender, request, user, **kwargs):
    subject = 'Добро пожаловать на наш сайт!'
    message = f'Ваши учетные данные:\n\nИмя пользователя: {user.username}\nПароль: {request.POST["password1"]}'
    send_mail(subject, message, 'from@example.com', [user.email])
