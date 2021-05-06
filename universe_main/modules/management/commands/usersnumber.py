from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Return len of Users objects list'

    # def add_arguments(self, parser):
    #     parser.add_argument('model', type = int)

    def handle(self, *args, **options):
        print(len(User.objects.all()))
        return None
