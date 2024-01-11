from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

from .models import New, Article

@receiver(post_save, sender=New)
def New_created(instance, created, **kwargs):
    if not created:
        print('adadadadadadad')
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новый Новость в категории {instance.category}'

    text_content = (
        f'Новость: {instance.title}\n'
        f'Цена: {instance.text}\n\n'
        f'Ссылка на Новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новость: {instance.title}<br>'
        f'Цена: {instance.text}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на Новость</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@receiver(post_save, sender=Article)
def Article_created(instance, created, **kwargs):
    if not created:
        print('adadadadadadad')
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новый статья в категории {instance.category}'

    text_content = (
        f'статья: {instance.title}\n'
        f'Цена: {instance.text}\n\n'
        f'Ссылка на статья: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'статья: {instance.title}<br>'
        f'Цена: {instance.text}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на статья</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()