# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import Normatizador
from .serializers import NormatizadorSerializer

class NormatizadorList(generics.ListCreateAPIView):
    queryset = Normatizador.objects.all()
    serializer_class = NormatizadorSerializer
