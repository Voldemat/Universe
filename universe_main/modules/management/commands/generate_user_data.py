from django.core.management.base import BaseCommand, CommandError

from users.models import User

from modules.testdata import RandomData

random_data = RandomData()

class Command(BaseCommand):
	help = 'Generate users objects in database'

	def add_arguments(self, parser):
		parser.add_argument('count', type = int)

	def handle(self, *args, **options):
		for num in range(options['count']):
			User.objects.create_user(
				email       = random_data.type('email', nickname_length = 10, punctuation_use = False),
				password    = random_data.type(str, max_length = 10, punctuation_use = False),
				about_me    = random_data.type(str, max_length = 50, punctuation_use = False),
				birth_date  = random_data.type('date'),
				first_name  = random_data.type(str, max_length = 10, punctuation_use = False),
				surname     = random_data.type(str, max_length = 10, punctuation_use = False)
			)
			print('.', end = '')

		print('\n')
		print('Complete!', end = '\n')


