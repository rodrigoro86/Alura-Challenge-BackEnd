from dataclasses import field
from django.test import TestCase
from django.db import IntegrityError
from db_videos.models import Video


class VideoTestCase(TestCase):
    def setUp(self):
        Video.objects.create(
                titulo = 'Alura Video 1',
                descricao = 'Video Teste',
                url = 'http://127.0.0.1/videos/alura_video_1',
            )
    
    def test_validacao_parametros_model_video(self):
        """Verifica o nome dos atributos do modelo Video"""
        video = Video.objects.get(id=1)
        self.assertEquals(video._meta.get_field('titulo').verbose_name, 'titulo')
        self.assertEquals(video._meta.get_field('descricao').verbose_name, 'descricao')
        self.assertEquals(video._meta.get_field('url').verbose_name, 'url')    

    def test_max_length_parametros_model_video(self):
        """Verifica a quantidade de caracterer dos atributos tituto e url"""
        video = Video.objects.get(id=1)
        self.assertEquals( video._meta.get_field('titulo').max_length, 30)
        self.assertEquals( video._meta.get_field('url').max_length, 300)
    
