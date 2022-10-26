from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from db_videos.views import (
    VideosViewSet,
)


router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

