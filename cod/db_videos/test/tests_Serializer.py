from django.test import TestCase
from db_videos.models import Video
from db_videos.serializer import VideoSerializer


class VideoSerializerTestCase(TestCase):
    def setUp(self):
        self.video = Video.objects.create(
                titulo = 'Alura Video 1',
                descricao = 'Video Teste',
                url = 'http://127.0.0.1/videos/alura_video_1',
            )
    
        self.serializer_test = VideoSerializer(instance=self.video)

    def test_verifica_campos_serializados_VideoSerializer(self):
        """Valida os campos serializados no VideoSerializer"""
        data = self.serializer_test.data
        self.assertEqual(set(data.keys()), set(['id', 'titulo', 'descricao', 'url']))
    
    def test_verica_conteudo_campos_serializados_VideoSerializer(self):
        """Verifica o conteúdo dos campos serializados se estão iguais ao do teste"""
        data = self.serializer_test.data
        self.assertEqual(data['titulo'], self.video.titulo)
        self.assertEqual(data['descricao'], self.video.descricao)
        self.assertEqual(data['url'], self.video.url)