from rest_framework.viewsets import ModelViewSet

from comentarios.api.serializers import ComentarioSerializer
from comentarios.models import Comentario


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.filter(aprovado=True)
    serializer_class = ComentarioSerializer
