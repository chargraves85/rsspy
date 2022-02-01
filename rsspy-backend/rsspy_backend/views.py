from django.shortcuts import render
from rest_framework import viewsets
from rsspy_backend.serializers import CoinSerializer
from rsspy_backend.models import Coin


# Create your views here.

class CoinView(viewsets.ModelViewSet):
    serializer_class = CoinSerializer
    queryset = Coin.objects.all()
