import string
import random
import datetime

class RandomData:
    def __init__(self:object) -> None:
        return None

    def _get_fields_from_dict_or_None(data:dict, *args:list[str]) -> tuple:
        
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

        return tuple(result)


    def email(length:int, email_services:list[str] = None, domain_names:list[str] = None) -> str:
        """
            Generate random email with nickaname defined length
            ex. email(10) return 'abfl23489g@gmail.com'

        """

        # define default length
        length = 7 if not length else length

        # define default email_services
        email_services = ['yandex', 'gmail', 'mail', 'mail'] if not email_services else email_servicesa

        # define domain names
        domain_names = ['.ru', '.com'] if not domain_names else domain_names

        # get nickname and turn it into lowercase
        nickname = generate_random_string(length, punctuation = False).lower()


        # random choice company from email_services
        email_company = random.choice(email_services)

        # random choice domain from domain_names
        domain = random.choice(domain_names)

        # return email
        # ex. nickname@email.com
        return nickname + '@' + email_company + domain


    def str(
        max_length:int       = 10, #defaults values
        letters:bool        = True,
        digits:bool         = True,
        punctuation:bool    = True) -> str: # type of return object
    

    # get all digits, letters, and punctuatuion characters
    letters:str     = str(string.ascii_letters) if letters else ''
    digits:str      = str(string.digits)        if digits else ''
    punctuation:str = str(string.punctuation)   if punctuation else ''

    
    # merge all characters into one string
    characters:str = letters + digits + punctuation


    # join random character to empty string for max_length
    result = ''.join( str(random.choice(characters)) for _ in range(max_length)  )

    return result


    def int(max_value:int = 1000, min_value:int = -1000) -> int:
        return random.randint(min_value, max_value)


    def float(max_value:int = 100.0, min_value:int = -100.0) -> float:
        return random.uniform(min_value, max_value)

def generate_random_type_data(datatype:Union[str,type], **kwargs:dict):
    if datatype == 'uuid':
        return uuid.uuid4

    if datatype == str:
        # get max_length from **kwargs or set to None 
        max_length:int = kwargs['max_length'] if 'max_length' in kwargs else None

        # return random string with defined max_length or with default length
        return generate_random_string(max_length)


    if datatype == int:
        # get max_value and min_value from kwargs or set it to None
        # max_value:int
        # min_value:int
        max_value, min_value = get_fields_from_dict_or_None(kwargs, 'max_value', 'min_value')

        return genetate_random_integer(max_value = max_value, min_value = min_value)

    if datatype == float:
        # get max_value and min_value from kwargs or set it to None
        # max_value:float
        # min_value:float
        max_value, min_value = get_fields_from_dict_or_None(kwargs, 'max_value', 'min_value')

        return generate_random_float(max_value = max_value, min_value = min_value)

    if datatype == bytes:
        length = get_fields_from_dict_or_None(kwargs, 'length')

        return random.randbytes(length if length else 10)

    if datatype == 'email':
        nickname_length = get_fields_from_dict_or_None(kwargs, 'nickname_length')[0]
        return generate_random_email(length = nickname_length)

    if datatype == bool:
        return bool(random.getrandbits(1))

    if datatype == 'date':
        return datetime.date.today()


def generate_user_data(count:int = 10) -> tuple:
    queryset = list()
    for item in range(count):
        obj = User.objects.create_user(
            email       = generate_random_type_data('email', nickname_length = 10),
            password    = generate_random_type_data(str, max_length = 10),
            about_me    = generate_random_type_data(str, max_length = 50),
            birth_date  = generate_random_type_data('date'),
            first_name  = generate_random_type_data(str, max_length = 10),
            surname     = generate_random_type_data(str, max_length = 10)
        )
        print(item)
        queryset.append(obj)

    return tuple(queryset)
