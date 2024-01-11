from django.core.management.base import BaseCommand, CommandError
from commonapp.models import New


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        self.stdout.write('are u sure u want to delete all news? (yes/no)')

        answer = input()
        if answer == 'yes':
            for new in New.objects.all():
                new.delete()
                New.save()
                self.stdout.write(self.style.SUCCESS(f'{new.title} has been deleted'))
        else:
            self.stdout.write('command interrupted')

        


