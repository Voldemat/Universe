import redis
import json

from typing import Optional, Union


from django.conf import settings

from api_v1.serializers import UserSerializer
from modules.utils import str_to_json


class Redis(redis.StrictRedis):
    def get(self, name:str, **kwargs:dict) -> Optional[str]:
        if 'prefix' in kwargs:
            name = kwargs['prefix'] + ':' + str(name)

        try:
            value = super().get(name).decode('UTF-8')
        except AttributeError:
            return None

        if 'json' in kwargs:
            value = str_to_json(value)

        return value

    def set(self, name:str, value:Union[str, dict], **kwargs:dict) -> None:
        if 'json' in kwargs:
            value = str(value)

            del kwargs['json']

        if 'prefix' in kwargs:
            name = kwargs['prefix'] + ':' + str(name)
            
            del kwargs['prefix']
            
        super().set(name, value, **kwargs)

        return None

redis_db = Redis(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT,
    db = 0,
    single_connection_client = True
)

