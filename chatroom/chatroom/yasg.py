from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Chat Room',
        default_version='v1',
        description='Testt Task public chat room(only RESTful API)'
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)

urlpatterns = [
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0),
        name='schema-swagger-ui'),
]
