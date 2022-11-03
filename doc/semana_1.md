# Alura Challenge Back-End
## Semana 01: Implementando uma API REST

### Índice 
* [História](#história)
* [Iniciando o projeto](#iniciando_o_projeto)
* [Tests](#tests)


### História
---------------------------------------------------------------------------------------
**Após alguns testes com protótipos feitos pelo time de UX de uma empresa, foi requisitada a primeira versão de uma plataforma para compartilhamento de vídeos.** A plataforma deve permitir ao usuário montar playlists com links para seus vídeos preferidos, separados por categorias.

Os times de frontend e UI já estão trabalhando no layout e nas telas. Para o backend, as principais funcionalidades a serem implementadas são:

1. **API com rotas implementadas segundo o padrão REST**;
2. **Validações feitas conforme as regras de negócio**;
3. **Implementação de base de dados para persistência das informações**;
4. **Serviço de autenticação para acesso às rotas GET, POST, PUT e DELETE**.

Temos um período de tempo de 4 semanas para desenvolver o projeto. Nas 3 primeiras, teremos tarefas a serem feitas e a última semana para ajustes ou para completar as tarefas pendentes. Vamos trabalhar com o sistema ágil de desenvolvimento, utilizando o Trello da seguinte forma:

1. A coluna **Pronto pra iniciar** apresenta os cartões com os elementos ainda não desenvolvidos.
2. Já na coluna **Desenvolvendo** ficarão os elementos que você estiver desenvolvendo no momento. Ao iniciar uma tarefa, você poderá mover o cartão que contém a tarefa para esta coluna.
3. No **Pausado** estarão os elementos que você começou a desenvolver, mas precisou parar por algum motivo.
4. Por fim, a coluna **Concluído** terá os elementos já concluídos.

O Trello é uma ferramenta de uso individual para você controlar o andamento das suas atividades, mas ela não será avaliada.

### Iniciando o projeto

#### 1° Criar um ambiente virtual
`python -m venv venv`  
`source venv/bin/activate`

#### 2° Instalar a bibloteca do django
`pip install django`

#### 3° Iniciar o projeto do django
`django-admin startproject api_alura_videos .`

#### 4° Configurar o horário e idioma no arquivo settings. 
```
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"
```  
#### 5° Criar um app para a api 
`python manage.py startapp db_videos`

#### 6° Adicionar o app no settings 
```
INSTALLED_APPS = [
    .
    .
    .
    "db_videos",
]
```  

#### 7° Criar um modelo exigido no card do banco de dados
Para criar um modelo é utilizado o arquivo models.py da pasta do app db_videos. 
```
class Video(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    url = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.nome
```
**Obs :** Por enquanto defini as colunas dessa forma

#### 8° Adicionar os campos do modelo do Video no arquivo admin.py para poder ser editado
```
from django.contrib import admin
from db_videos.models import Video

class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')
    list_display_links = ('id', 'titulo', 'url')
    search_fields = ('titulo',)
    list_per_page = 50

admin.site.register(Video, Videos)
```
#### 9° Criar o banco de dados 
`python manage.py makemigrations`  
`python manage.py migrate`

#### 10° Criar um usuário para o projeto
`python manage.py createsuperuser` 

#### OBS: Nesse momento já dá para rodar o projeto e ver como está o banco 
`python manage.py runserver`

#### 10° Instalar as bibliotecas djangorestframework e markdown
Essas bibliotecas são necessárias para criar a api REST
`pip install djangorestframework`  
`pip install markdown`

#### 11° Criar o Serializer
Criar um arquivo chamado serializer.py. 
Os Serializers permitem que dados complexos, como querysets e model instances, sejam convertidos em tipos de dados Python nativos que podem ser facilmente renderizados em JSON, XML ou outros tipos de conteúdo.  
Conteúdo do serializer: 
```
from rest_framework import serializers
from db_videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'url']
```
#### 12° Criar uma view para o o VideoSerializer
No arquivo views.py criar uma view para que seja apresentado o VideoSerializer.
```
from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from db_videos.models import Video
from db_videos.serializer import VideoSerializer


class VideosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os dados Sitios"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo']
```
Para acessar essa view precisa da autenticação e foi adicionando um filtro. 

#### 13° Criar as url's para a api 
No arquivo urls.py criar rotas para a api
```
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
```
Na página index desse projeto terá aurl dos vídeos 

### Tests 
Testes são muito importantes, eu não entendi o porque de criar um teste visto que eu já sei como vou chamar a função e oque vai retornar masssss entendi que hoje eu crio um teste e no futuro o código pode mudar e a alteração de uma função pode quebrar outra os testes são necessários para validar isso e manter a extrutura do código. 
Outra coisa é que dá para entender um pouco do funcionamento do código. 

Para criar os testes criei uma pasta chamada test com o os seguites arquivos: 
- __init__.py
- tests_Model.py

Comando para rodar os testes é `python manage.py test` o django é muito bom com os tests porque ele criar uma base de dados nova só para validar os testes e depois remove.  

#### Teste Models
Vou criar vários testes do modelo Vídeos visando validar e manter a extrutura desse modelo 
Criei dois testes para o meu modelo Video: 
```
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
        self.assertEquals( video._meta.get_field('url').max_length, 30)
```
O primeiro teste valida o nome dos atributos e o segundo a quantidade máxima de caracter

#### Teste Serializer 

```
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
```

#### Teste URL 

```
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
```
