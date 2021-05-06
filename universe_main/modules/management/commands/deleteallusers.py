from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Delete all users'

    # def add_arguments(self, parser):
    #     parser.add_argument('model', type = int)

    def handle(self, *args, **options):
        for obj in User.objects.all():
            obj.delete()


