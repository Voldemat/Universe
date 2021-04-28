import json

from django.http import JsonResponse

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_v1.cache import redis_db as redis
from api_v1.serializers import UserSerializer
from api_v1.permissions import UserObjOrReadOnly

from modules.utils import get_db_table_name


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        UserObjOrReadOnly,
    )

    def get_object(self):
        """
        Returns the object the view is displaying.
        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        obj = get_object_or_404(queryset, **filter_kwargs)


        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs['pk']

        obj_json = redis.get(
            user_id,
            json = True,
            prefix = get_db_table_name( get_user_model() )
        )
        status = 200
        if not obj_json:
            obj = self.get_object()
            serializer = self.get_serializer(obj)
            obj_json = serializer.data

            redis.set(
                name = obj_json['id'],
                value = obj_json,
                json = True,
                prefix = get_db_table_name( get_user_model() ),
                ex = 60
            )
            status = 201

        return Response(obj_json, status = status)


@csrf_exempt
def cache_api(request):
    if request.method == 'POST' and request.is_ajax:
        data = json.loads(request.body.decode('UTF-8'))

        user_id = data['id']

        if not user_id:
            return JsonResponse({'error':"Id is not defined"}, status = 400)


        user = redis.get(
            user_id,
            json = True,
            prefix = get_db_table_name( get_user_model() )
        )
        if user:
            print('redis',user)
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
            

            print('django', user)

            return JsonResponse({'django':user_json}, status = 200)

        
    return JsonResponse({"error":"method must be post"}, status = 400)