from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from db_videos.models import Video, Categoria
from db_videos.serializer import (
    VideoSerializer,
    CategoriaSerializer,
)


class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os dados Sitios"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']

class CategoriaViewSet(viewsets.ModelViewSet):
    """Exibindo todos os dados das Categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']