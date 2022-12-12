from .models import User, Ad
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from datetime import date, timedelta


def sending_mail(today):
    """
    Рассылка новых объявлений раз в неделю всем пользователям
    """
    start_week = today - timedelta(days=7)
    end_week = today

    for user_instance in User.objects.all():
        email = user_instance.email
        username = user_instance.username
        ad_list = Ad.objects.filter(published_date=(start_week, end_week))

        html_content = render_to_string(
            'boardApp/reminder_week.html',
            context=
            {'subscriber_posts': ad_list,
             'username': username,
             'domain_url': settings.DOMAIN,}
        )

        msg = EmailMultiAlternatives(
            subject="Новые объявления за неделю",
            from_email='django.testemail@yandex.ru',
            to=[email,]
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()