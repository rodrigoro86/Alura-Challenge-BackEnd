from django.test import TestCase
from db_videos.models import Video, Categoria
from db_videos.serializer import VideoSerializer, CategoriaSerializer


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

class CategoriaSerializerTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(
                titulo = 'Alura Video 1',
                cor = '#FFF',
            )
    
        self.serializer_test = CategoriaSerializer(instance=self.categoria)

    def test_verifica_campos_serializados_CategoriaSerializer(self):
        """Valida os campos serializados no CategoriaSerializer"""
        data = self.serializer_test.data
        self.assertEqual(set(data.keys()), set(['id', 'titulo', 'cor']))
    
    def test_verica_conteudo_campos_serializados_CategoriaSerializer(self):
        """Verifica o conteúdo dos campos serializados se estão iguais ao do teste"""
        data = self.serializer_test.data
        self.assertEqual(data['titulo'], self.categoria.titulo)
        self.assertEqual(data['cor'], self.categoria.cor)