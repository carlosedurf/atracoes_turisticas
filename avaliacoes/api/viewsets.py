from avaliacoes.api.serializers import AvaliacaoSerializer
from rest_framework.viewsets import ModelViewSet

from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
