from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import UserSerializer
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer