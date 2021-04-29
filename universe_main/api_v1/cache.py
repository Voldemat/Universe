import redis
import json

from typing import Optional, Union


from django.conf import settings

from api_v1.serializers import UserSerializer
from modules.utils import str_to_json


class Redis(redis.StrictRedis):
    def get(self, name:str, **kwargs:dict) -> Optional[str]:
        if 'prefix' in kwargs:
            # add prefix to name "prefix:name" ex. "users_user:1d259df6-3e38-4h2b-13gb-51d0c3ctee01"
            name = kwargs['prefix'] + ':' + str(name)

        try:
            # get value from redis and decode it
            value = super().get(name).decode('UTF-8')
        except AttributeError:
            # if value does not exist return None
            return None

        if 'json' in kwargs:
            # parse json from str
            value:dict = str_to_json(value)

        return value

    def set(self, name:str, value:Union[str, dict], **kwargs:dict) -> None:
        if 'json' in kwargs:
            # stringify json format
            value = str(value)

            # delete json kwarg
            del kwargs['json']

        if 'prefix' in kwargs:
            # add prefix to name "prefix:name" ex. "users_user:1d259df6-3e38-4h2b-13gb-51d0c3ctee01"
            name = kwargs['prefix'] + ':' + str(name)
            
            # delete prefix kwarg
            del kwargs['prefix']
            
        # call parent set method with additional kwargs
        super().set(name, value, **kwargs)

redis_db = Redis(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT,
    db = 0
)

