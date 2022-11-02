from rest_framework import serializers
from db_videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'url']
        