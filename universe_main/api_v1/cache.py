import redis
import json

from django.conf import settings

from api_v1.serializers import UserSerializer


redis_instance = redis.StrictRedis(
    host = settings.REDIS_HOST,
    port = settings.REDIS_PORT,
    db = 0
)

def set_user_model(obj:object) -> tuple:
    # Parse obj into json
    obj_json = UserSerializer(obj, many = False).data

    # create redis_object_prototype = (id, json_content)
    redis_object_instance = {
        'name'   :   f"users_user-{obj_json['id']}",
        'value' :   str(obj_json)
    }

    # set object in database
    redis_instance.set(**redis_object_instance)

    # return representation of redis object
    return redis_object_instance['value']

redis_instance.set_user_model = set_user_model