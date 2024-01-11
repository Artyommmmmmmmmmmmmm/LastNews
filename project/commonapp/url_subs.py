from django.urls import path
# Импортируем созданные нами представления
from .views import subscriptions
urlpatterns = [
   path('', subscriptions, name='subscriptions'),
]