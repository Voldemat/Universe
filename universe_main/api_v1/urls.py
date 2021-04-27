from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from rest_framework_swagger.views import get_swagger_view

from api_v1.views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename = 'users')

swagger_view = get_swagger_view(title = 'API')

urlpatterns = [
    path('docs/', swagger_view, name = 'docs'),
    path('api-token-auth/', obtain_auth_token, name = 'token-auth')
]
urlpatterns += router.urls