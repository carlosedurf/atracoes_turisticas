from rest_framework.serializers import ModelSerializer, SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
# from avaliacoes.api.serializers import AvaliacaoSerializer
# from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco
from pontos_turisticos.models import DocIdentificacao, PontoTuristico


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'


class PontoTuristicoSerializer(ModelSerializer):
    # atracoes = AtracaoSerializer(many=True, read_only=True)
    atracoes = AtracaoSerializer(many=True)
    # comentarios = ComentarioSerializer(many=True)
    # avaliacoes = AvaliacaoSerializer(many=True)
    # endereco = EnderecoSerializer(read_only=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        read_only_fields = ('comentarios', 'avaliacoes')
        fields = (
            'id',
            'nome',
            'descricao',
            'aprovado',
            'foto',
            'atracoes',
            # 'comentarios',
            # 'avaliacoes',
            'endereco',
            'descricao_completa',
            'descricao_completa_model',
            'doc_identificacao',
        )

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj: PontoTuristico) -> str:
        return '%s - %s' % (obj.nome, obj.descricao)
