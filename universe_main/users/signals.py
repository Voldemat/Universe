from django.db.models.signals import post_save
from django.dispatch import receiver


from api_v1.cache import redis_db as redis
from api_v1.serializers import UserSerializer

from users.models import User

from modules.utils import get_db_table_name



@receiver(post_save, sender = User)
def cache_user(sender, instance, *args, **kwargs):
    obj_json = UserSerializer(instance).data
    prefix = get_db_table_name(User)

    redis.set(
        name = obj_json['id'],
        value = obj_json,
        json = True,
        prefix = prefix,
        ex = 60
    )
    print('post_save redis')

