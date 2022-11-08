from django.contrib import admin
from db_videos.models import Video, Categoria

# @Dm14 
class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url', 'categoriaId')
    list_display_links = ('id', 'titulo', 'url', 'categoriaId')
    search_fields = ('titulo',)
    list_per_page = 50

admin.site.register(Video, Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')
    list_display_links = ('id', 'titulo', 'cor')
    search_fields = ('titulo',)
    list_per_page = 50

admin.site.register(Categoria, Categorias)