from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from db_videos.views import (
    VideosViewSet,
    CategoriaViewSet,
)


router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categoria', CategoriaViewSet, basename='Categoria')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

