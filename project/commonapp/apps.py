from django.apps import AppConfig


class CommonappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commonapp'

    def ready(self):
        from . import signals 
        from . import execute
        execute.start() # выполнение модуля -> регистрация сигналов