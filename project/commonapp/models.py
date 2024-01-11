from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Товар для нашей витрины 
class New(models.Model):
    # ARTICLE = 'AR'
    # NEW = 'NE'
    # AVAILABLE_TYPES = ((ARTICLE, 'Статья'), (NEW, 'Новость'))
    title = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    text = models.TextField()
    type = 'Новость'
    made_at = models.DateTimeField(
        auto_now=True,)
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='News', # все продукты в категории будут доступны через поле products
    )

    # type = models.CharField(max_length=2, choices=AVAILABLE_TYPES, default=NEW)
    def so_cool(self):
        return 'so cool'

    def __str__(self):
        return self.title
    # date = models.CharField(auto_now_add=datetime.strftime())
    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])   # def __str__(self):
    #     return f'{self.title.title()}: {self.text[:20]}'

class Article(models.Model):
    # ARTICLE = 'AR'
    # NEW = 'NE'
    # AVAILABLE_TYPES = ((ARTICLE, 'Статья'), (NEW, 'Новость'))
    title = models.CharField(
        max_length=50,
        unique=True, # названия товаров не должны повторяться
    )
    text = models.TextField()
    type = 'Статья'
    made_at = models.DateTimeField(
        auto_now=True,)
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='Articles', # все продукты в категории будут доступны через поле products
    )

    # type = models.CharField(max_length=2, choices=AVAILABLE_TYPES, default=NEW)
    def so_cool(self):
        return 'so_cool'

    def __str__(self):
        return self.title
    # date = models.CharField(auto_now_add=datetime.strftime())
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])   # def __str__(self):
    #     return f'{self.title.title()}: {self.text[:20]}'

# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name.title()
    
class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )