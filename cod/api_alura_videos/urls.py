from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from db_videos.views import (
    VideosViewSet,
    CategoriaViewSet,
    ListaCategoriaVideosViewSet,
)
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Análise de Desempenho",
      default_version='v1',
      description="API Análise de Desempenho",
      terms_of_service="#",
      contact=openapi.Contact(email="rdoliveira@atech.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categorias', CategoriaViewSet, basename='Categorias')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("categorias/<int:id>/videos", ListaCategoriaVideosViewSet.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

