from django.contrib import admin
from db_videos.models import Video

# @Dm14 
class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')
    list_display_links = ('id', 'titulo', 'url')
    search_fields = ('titulo',)
    list_per_page = 50

admin.site.register(Video, Videos)