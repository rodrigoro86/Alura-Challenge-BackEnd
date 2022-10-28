from dataclasses import field
from rest_framework.test import APITestCase
from rest_framework import status
from db_videos.models import Video
from django.urls import reverse
import json, requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class URL_API_TestCase(APITestCase):
    def __init__(self, basename:str):
        self.user = User.objects.create_user(username='teste', password='teste')
        self.list_url = reverse(basename)
        
    def get_URL(self, client):
        resposta_api = client.get(self.list_url)
        data_videos = json.dumps(resposta_api.data, indent=4)
        data_videos = json.loads(data_videos)
        return resposta_api, data_videos

    def post_URL(self, client, comando):
        resposta_api = client.post(self.list_url, data=comando)
        return resposta_api
    
    def delete_URL(self, client, id):
        resposta_api = client.delete(self.list_url+f'{id}/')
        return resposta_api

    def put_URL(self, client, id, comando):
        resposta_api = client.put(self.list_url+f'{id}/', data=comando)
        return resposta_api

class URL_Videos_TestCase(APITestCase):
    def setUp(self):
        self.video_teste_1 = Video.objects.create(
            titulo = 'Alura Video 1',
            descricao = 'Video Teste',
            url = 'http://127.0.0.1/videos/alura_video_1',
        )
        Video.objects.create(
            titulo = 'Alura Video 2',
            descricao = 'Video Teste 2',
            url = 'http://127.0.0.1/videos/alura_video_2',
        )

        self.obj_test = URL_API_TestCase('Videos-list')
        self.client.force_authenticate(self.obj_test.user)

    def test_get_para_listar_todos_os_videos(self):
        """Teste da requisição GET para listar todos os videos"""
        resposta_api, data_videos =  self.obj_test.get_URL(self.client)
        self.assertEqual(resposta_api.status_code, status.HTTP_200_OK)
    
    def test_get_verifica_se_retorna_uma_lista(self):
        """Teste da requisição GET verificar se retorna uma lista com os dados dos videos"""
        resposta_api, data_videos =  self.obj_test.get_URL(self.client)
        self.assertEqual(type(data_videos), list)

    def test_get_verifica_se_retorna_dados_do_primeiro_video(self):
        """Teste da requisição GET verificar se retorna os dados do primeiro vídeo"""
        response = self.client.get(self.obj_test.list_url+'1/')
        self.assertEqual(response.data['titulo'], self.video_teste_1.titulo)
        self.assertEqual(response.data['descricao'], self.video_teste_1.descricao)
        self.assertEqual(response.data['url'], self.video_teste_1.url)

    def test_post_cria_video_e_valida_video_criado(self):
        """Esse teste além de criar um video pelo post ele valida se o video foi criado corretamente"""
        data_video_teste = {
            'titulo': 'Alura Video 3',
            'descricao': 'Video Teste 3',
            'url': 'http://127.0.0.1/videos/alura_video_3',
        }
        response = self.obj_test.post_URL(self.client, data_video_teste)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        resp = self.client.get(self.obj_test.list_url+'3/')
        self.assertEqual(resp.data['titulo'], data_video_teste['titulo'])
        self.assertEqual(resp.data['descricao'], data_video_teste['descricao'])
        self.assertEqual(resp.data['url'], data_video_teste['url'])
    
    def test_delete_video_e_verifica_se_nao_e_encontrado(self):
        """Remove um video e verifica se não é encontrado"""
        response = self.obj_test.delete_URL(self.client, 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        resp = self.client.get(self.obj_test.list_url+'1/')
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_put_edita_dados_video(self):
        """Edita o titulo do video ID 1 e valida os dados com o modelo"""
        data_video_teste = {
            'titulo': 'Alura Video 1 Alterado',
            'descricao': 'Video Teste 3',
            'url': 'http://127.0.0.1/videos/alura_video_3',
        }
        response = self.obj_test.put_URL(self.client, 1, data_video_teste)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        resp = self.client.get(self.obj_test.list_url+'1/')
        self.assertEqual(resp.data['titulo'], data_video_teste['titulo'])
        self.assertEqual(resp.data['descricao'], data_video_teste['descricao'])
        self.assertEqual(resp.data['url'], data_video_teste['url'])