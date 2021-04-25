from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ['last_login', 'is_active', 'is_staff', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}