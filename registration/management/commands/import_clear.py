from django.core.management.base import BaseCommand

from api.models import Organization, User


class Command(BaseCommand):
    help = 'clear imported Organization data'

    def handle(self, *args, **kwargs):
        user = User.objects.filter(is_superuser=True).first()
        deleted, rows_count = Organization.objects.filter(inspector=user).delete()
        if deleted > 0:
            self.stdout.write('operation completed, deleted rows count as below:')
            for model_name in rows_count:
                self.stdout.write('{0}: {1}'.format(model_name, rows_count[model_name]))
        else:
            self.stdout.write('operation completed, no data to delete')