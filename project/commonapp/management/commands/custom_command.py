from django.core.management.base import BaseCommand, CommandError
from commonapp.models import New

class Command(BaseCommand):
    help = 'переименует все новости и их id'

    def handle(self, *args, **options):
        for new in New.objects.all():
            new.title = f'id:{new.id}'
        
            New.save()

            self.stdout.write(self.style.SUCCESS('successfully renamed new to a "%s"' % new.title))