from .models import Normatizador
from rest_framework import serializers
import json
from classificacao import Classificacao

class NormatizadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Normatizador
        fields = ('__all__')

    def create(self, data):
        classificador = Classificacao.Analise()
        normatizado = Normatizador()
        normatizado.text = classificador.classificar(data['text'])
        return normatizado