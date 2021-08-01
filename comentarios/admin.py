from django.contrib import admin

from comentarios.actions import aprova_comentarios, reprova_comentarios
from comentarios.models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data', 'aprovado')
    actions = [reprova_comentarios, aprova_comentarios]


admin.site.register(Comentario, ComentarioAdmin)
