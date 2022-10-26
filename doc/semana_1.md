# Alura Challenge Back-End
## Semana 01: Implementando uma API REST

### Índice 
* [História](#história)


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

Bom projeto!

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

#### 9° Instalar as bibliotecas djangorestframework e markdown
Essas bibliotecas são necessárias para criar a api REST
`pip install djangorestframework`  
`pip install markdown`



