from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Corporate assets tracker API",
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogAPI.urls')),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]
