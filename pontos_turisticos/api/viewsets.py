from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pontos_turisticos.api.serializers import PontoTuristicoSerializer
from pontos_turisticos.models import PontoTuristico

# from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    # http_method_names = ['DELETE']
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    # search_fields = ('nome', 'descricao', '^endereco__linha1')    # Inicia com Ex: LIKE '%nome'
    # search_fields = ('nome', 'descricao', '=endereco__linha1')    # Igual Ex: = 'nome'
    search_fields = ('nome', 'descricao', 'endereco__linha1')   # Tenha Ex: LIKE '%nome%'
    # lookup_field = 'nome'   # Por padrão é id/pk
    # permission_classes = [IsAuthenticated]    # Autenticado para o conteudo
    # permission_classes = [IsAuthenticatedOrReadOnly]    # Somente leitura para endpoint com verbo GET
    permission_classes = [DjangoModelPermissions]    # De acordo com permissão no admin
    # permission_classes = [IsAdminUser]  # Somente usuários com permissão de Admin
    authentication_classes = (TokenAuthentication,)     # Informa o tipo de autenticação

    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'method': 'denunciar'})

    @action(methods=['post'], detail=False)
    def teste(self, request):
        return Response({'method': 'teste'})

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, pk=None):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=pk)

        ponto.atracoes.set(atracoes)

        ponto.save()

        return Response(status=status.HTTP_201_CREATED)
