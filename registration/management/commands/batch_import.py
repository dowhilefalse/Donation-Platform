import os

from django.core.management.base import BaseCommand

from registration.import_helper import parse_excel_file


class Command(BaseCommand):
    help = 'Batch import Organization data form Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel', type=str, help='Excel file path')

    def handle(self, *args, **kwargs):
        excel_path = os.path.realpath(kwargs['excel'])
        if os.path.exists(excel_path):
            parse_excel_file(excel_path)
            self.stdout.write('excel [{0}] import completed'.format(excel_path))
        else:
            self.stdout.write('excel [{0}] not exist'.format(excel_path))