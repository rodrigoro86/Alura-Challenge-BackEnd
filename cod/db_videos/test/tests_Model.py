from dataclasses import field
from django.test import TestCase
from django.db import IntegrityError
from db_videos.models import Video, Categoria


class VideoTestCase(TestCase):
    def setUp(self):
        Categoria.objects.create(
                titulo = 'LIVRE',
                cor = '#FFF',
            )

        Video.objects.create(
                titulo = 'Alura Video 1',
                descricao = 'Video Teste',
                url = 'http://127.0.0.1/videos/alura_video_1',
            )
    
    def test_validacao_parametros_model_video(self):
        """Verifica o nome dos atributos do modelo Video"""
        video = Video.objects.get(id=1)
        self.assertEquals(video._meta.get_field('titulo').verbose_name, 'titulo', msg='Atributo titulo não encontrado')
        self.assertEquals(video._meta.get_field('descricao').verbose_name, 'descricao', msg='Atributo descricao não encontrado')
        self.assertEquals(video._meta.get_field('url').verbose_name, 'url', msg='Atributo url não encontrado')
        self.assertEquals(video._meta.get_field('categoriaId').verbose_name, 'categoriaId', msg='Atributo categoriaId não encontrado')        

    def test_max_length_parametros_model_video(self):
        """Verifica a quantidade de caracterer dos atributos tituto e url"""
        video = Video.objects.get(id=1)
        self.assertEquals( video._meta.get_field('titulo').max_length, 100)
        self.assertEquals( video._meta.get_field('url').max_length, 300)
    
class CategoriaTestCase(TestCase):
    def setUp(self):
        Categoria.objects.create(
                titulo = 'Alura Video 1',
                cor = '#FFF',
            )
    
    def test_validacao_parametros_model_categoria(self):
        """Verifica o nome dos atributos do modelo Video"""
        categoria = Categoria.objects.get(id=1)
        self.assertEquals(categoria._meta.get_field('titulo').verbose_name, 'titulo')
        self.assertEquals(categoria._meta.get_field('cor').verbose_name, 'cor') 

    def test_max_length_parametros_model_categoria(self):
        """Verifica a quantidade de caracterer dos atributos tituto e url"""
        categoria = Categoria.objects.get(id=1)
        self.assertEquals(categoria._meta.get_field('titulo').max_length, 30)
        self.assertEquals(categoria._meta.get_field('cor').max_length, 30)