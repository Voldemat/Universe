import json

from django.http import JsonResponse

from django.contrib.auth            import get_user_model
from django.views.decorators.csrf   import csrf_exempt

from rest_framework.viewsets            import ModelViewSet
from rest_framework.generics            import get_object_or_404
from rest_framework.response            import Response
from rest_framework.authtoken.views     import ObtainAuthToken
from rest_framework.authtoken.models    import Token

from api_v1.cache       import redis_db as redis
from api_v1.serializers import UserSerializer
from api_v1.permissions import UserObjOrReadOnly

from modules.utils import get_db_table_name

"""
    User endpoint with override retrieve method
    to cache user objects in redis.
"""


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        UserObjOrReadOnly,
    )


    def list(self, request):
        # get redis obj or None
        datalist = redis.get_list(prefix = 'users_user', json = True)
        status = 200

        # if redis obj does not exist
        if not datalist:
            queryset = self.get_queryset()
            print('ss')
            datalist = self.get_serializer(queryset, many = True).data

            redis.set_list(
                prefix = 'users_user',
                datalist = datalist,
                ex = 10
            )

            status = 201
        return Response(datalist, status = status)

    def retrieve(self, request, *args, **kwargs):
        # get user_id
        user_id:str = self.kwargs['pk']

        # get json object from redis
        obj_json:dict = redis.get(
            user_id,
            json = True,
            prefix = get_db_table_name( get_user_model() )
        )

        # if json object does not exist
        if not obj_json:

            # get object from db
            obj:object          = self.get_object()

            # parse it into json
            serializer:object   = self.get_serializer(obj)
            obj_json:dict       = serializer.data

            # set json object into redis db
            redis.set(
                name = obj_json['id'],
                value = obj_json,
                json = True,
                prefix = get_db_table_name( get_user_model() ),
                # ex = expiry
                ex = 60
            )

        return Response(obj_json)


class TokenAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # get serializer instance
        serializer:object = self.serializer_class(
            data = request.data,
            context = {"request":request}
        )

        # validating...
        serializer.is_valid(raise_exception = True)

        # get user object
        user:object = serializer.validated_data['user']

        # get or create Token for current user
        token, created = Token.objects.get_or_create(user = user)

        return Response( { 'token':token.key }, status = 201 if created else 200)


@csrf_exempt
def cache_api(request:object) -> object:
    if request.method == 'POST' and request.is_ajax:
        data:dict = json.loads(request.body.decode('UTF-8'))

        user_id:str = data['id']

        if not user_id:
            return JsonResponse({'error':"Id is not defined"}, status = 400)


        user:dict = redis.get(
            user_id,
            json = True,
            prefix = get_db_table_name( get_user_model() )
        )
        if user:
            return JsonResponse({'redis':user}, status = 200)

        else:
            user = get_user_model().objects.get(id = user_id)

            user_json = UserSerializer(user).data

            redis.set(
                name = user_id,
                value = user_json,
                json = True,
                prefix = get_db_table_name( get_user_model() ),
                ex = 10
            )
            
            return JsonResponse({'django':user_json}, status = 200)

        
    return JsonResponse({"error":"method must be post"}, status = 400)