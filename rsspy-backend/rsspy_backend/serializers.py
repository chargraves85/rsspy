from rest_framework import serializers
from .models import Coin


# TODO: Update serializer to override create() method to allow relational/nested structures
class CoinSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

    class Meta:
        model = Coin
        fields = ('coinName', 'symbol', 'data', 'currentBuzzScore', 'previousBuzzScore')
