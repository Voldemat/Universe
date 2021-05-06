import string
import uuid
import random
import datetime

from typing import (
	Union,
	Any
)

class RandomData:
	def __init__(self) -> None:
		return None

	def _get_fields_from_dict_or_None(self, data:dict, *args:list[str]) -> Union[tuple, Any]:
		
		"""
			Example:
			
			With this example data:

			data = {
				'max_length':10,
				'other_key':'a',
				'nickname_length':7,
			}
			
			This args   = ['other_key', 'dog_length', 'nickname_length'],
			will return = (    'a'    ,     None    ,       '7'        )

			Current function will return tuple:('a', None, 'nickname_length')
			
			

		"""


		# init result list
		result = list()

		# iterate all args
		for key in args:

			# append value of given key or set it to None
			result.append(data[key] if key in data.keys() else None)

		return tuple(result) if len(result) != 1 else result[0]


	def email(self, length:int, email_services:list[str] = None, domain_names:list[str] = None) -> str:
		"""
			Generate random email with nickaname defined length
			ex. email(10) return 'abfl23489g@gmail.com'

		"""

		# define default length
		length = 7 if not length else length

		# define default email_services
		email_services = ['yandex', 'gmail', 'mail', 'mail'] if not email_services else email_services

		# define domain names
		domain_names = ['.ru', '.com'] if not domain_names else domain_names

		# get nickname and turn it into lowercase
		nickname = self.str(length, punctuation_use = False).lower()


		# random choice company from email_services
		email_company = random.choice(email_services)

		# random choice domain from domain_names
		domain = random.choice(domain_names)

		# return email
		# ex. nickname@email.com
		return nickname + '@' + email_company + domain


	def str(
		self, 
		max_length:int      = 10  , #defaults values
		letters_use:bool        = True,
		digits_use:bool         = True,
		punctuation_use:bool    = False) -> str: # type of return object
	

		# get all digits, letters, and punctuatuion characters
		letters:str     = str(string.ascii_letters) if letters_use else ''
		digits:str      = str(string.digits)        if digits_use else ''
		punctuation:str = str(string.punctuation)   if punctuation_use else ''

		
		# merge all characters into one string
		characters:str = letters + digits + punctuation


		# join random character to empty string for max_length
		result = ''.join( str(random.choice(characters)) for _ in range(max_length)  )

		return result


	def int(self, max_value:int = 1000, min_value:int = -1000) -> int:
		return random.randint(min_value, max_value)


	def float(self, max_value:int = 100.0, min_value:int = -100.0) -> float:
		return random.uniform(min_value, max_value)

	def type(self, datatype:Union[str, type], **kwargs:dict) -> Any:
		"""
			Return random value for given datatype

		"""

		if datatype == 'uuid':
			return uuid.uuid4

		if datatype == str:
			# get max_length from **kwargs or set to None
			max_length:int = self._get_fields_from_dict_or_None(kwargs,'max_length')

			# return random string with defined max_length or with default length
			return self.str(max_length)


		if datatype == int:
			# get max_value and min_value from kwargs or set it to None
			max_value_int:int
			min_value_int:int
			max_value_int, min_value_int = self._get_fields_from_dict_or_None(kwargs, 'max_value', 'min_value')

			return self.int(max_value = max_value_int, min_value = min_value_int)

		if datatype == float:
			# get max_value and min_value from kwargs or set it to None
			max_value_float:float
			min_value_float:float
			max_value_float, min_value_float = self._get_fields_from_dict_or_None(kwargs, 'max_value', 'min_value')

			return self.float(max_value = max_value_float, min_value = min_value_float)

		if datatype == bytes:
			length = self._get_fields_from_dict_or_None(kwargs, 'length')

			return random.randbytes(length if length else 10)

		if datatype == 'email':

			nickname_length = self._get_fields_from_dict_or_None(kwargs, 'nickname_length')
			return self.email(length = nickname_length)

		if datatype == bool:
			return bool(random.getrandbits(1))

		if datatype == 'date':
			return datetime.date.today()

	
# def generate_user_data(count:int = 10) -> tuple:
# 	queryset = list()
# 	for item in range(count):
# 		obj = User.objects.create_user(
# 			email       = generate_random_type_data('email', nickname_length = 10),
# 			password    = generate_random_type_data(str, max_length = 10),
# 			about_me    = generate_random_type_data(str, max_length = 50),
# 			birth_date  = generate_random_type_data('date'),
# 			first_name  = generate_random_type_data(str, max_length = 10),
# 			surname     = generate_random_type_data(str, max_length = 10)
# 		)
# 		print(item)
# 		queryset.append(obj)

# 	return tuple(queryset)
