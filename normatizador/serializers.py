from .models import Normatizador
from rest_framework import serializers
import json

class NormatizadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Normatizador
        fields = ('__all__')

    def create(self, data):
        print(data['text'])
        normatizado = Normatizador()
        normatizado.text = data['text']
        return normatizado