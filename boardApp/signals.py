from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_managers, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import Comments


@receiver(post_save, sender=Comments)
def notify_post_create(instance, **kwargs):

    comments = instance
    comment_text = comments.comment
    comment_pk = comments.pk
    ad_title = comments.ad.title

    email = User.objects.get(pk=comments.ad.user.pk).email
    username = User.objects.get(pk=comments.ad.user.pk)

    html_content = render_to_string(
        'boardApp/reminder.html',
        context=
        {'ad_title':ad_title,
         'comment_text': comment_text,
         'username': username,
         'comment_pk': comment_pk,
         'domain_url': settings.DOMAIN, }
    )

    msg = EmailMultiAlternatives(
        subject='Новый отзыв',
        from_email='django.testemail@yandex.ru',
        to=[email, ]
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()
