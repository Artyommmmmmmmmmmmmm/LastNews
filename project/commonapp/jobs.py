from apscheduler.schedulers.background import BackgroundScheduler
from commonapp.models import Category, Article
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

scheduler = BackgroundScheduler()

def send_weekly_mail():
    articles = Article.objects
    categories = Category.objects.all()
    subject = f'Еженеделльный отчет по новым статьям'
    for category in categories:
        emails = User.objects.filter(
        subscriptions__category=category
        ).values_list('email', flat=True)
        articles_set = articles.filter(
        category=category)
        for article in articles_set:
            text_content = (
                f'Новость: {article.title}\n'
                f'Цена: {article.text}\n\n'
                f'Ссылка на Новость: http://127.0.0.1:8000{article.get_absolute_url()}'
            )
            html_content = (
                f'Новость: {article.title}<br>'
                f'Цена: {article.text}<br><br>'
                f'<a href="http://127.0.0.1:8000{article.get_absolute_url()}">'
                f'Ссылка на Новость</a>'
            )
            for email in emails:
                msg = EmailMultiAlternatives(subject, text_content, None, [email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()