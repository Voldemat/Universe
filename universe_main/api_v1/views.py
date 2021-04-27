import json

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework.viewsets import ModelViewSet

from api_v1.cache import redis_instance as redis
from api_v1.serializers import UserSerializer
from api_v1.permissions import UserObjOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        UserObjOrReadOnly,
    )

@csrf_exempt
def cache_api(request):
    if request.method == 'POST' and request.is_ajax:
        data = json.loads(request.body.decode('UTF-8'))

        user_id = data['id']

        if not user_id:
            return JsonResponse({'error':"Id is not defined"}, status = 400)

        if redis.get(f'users_user-{user_id}'):
            user = redis.get(f'users_user-{user_id}')
            print('redis',user)
            return JsonResponse({str(user_id):user.decode('UTF-8')}, status = 200)
        else:
            user = get_user_model().objects.get(id = user_id)
            redis.set_user_model(user)
            print('django', user)
            return JsonResponse({str(user.id):user.email}, status = 200)

        
    return JsonResponse({"error":"method must be post"}, status = 400)