import graphene
from django.db.models import F
from graphene_django import DjangoObjectType

from .models import Coin


class CoinType(DjangoObjectType):
    class Meta:
        model = Coin
        fields = ('coinName', 'symbol', 'data', 'currentBuzzScore', 'previousBuzzScore')


class Query(graphene.ObjectType):
    coins = graphene.List(CoinType)
    coin_by_name = graphene.Field(
        CoinType, name=graphene.String(required=True))
    coin_by_buzz_change = graphene.List(CoinType)

    def resolve_coins(self, info, **kwargs):
        # Querying a list
        return Coin.objects.all()

    def resolve_coin_by_name(self, info, **args):
        try:
            return Coin.objects.get(coinName=args)
        except Coin.DoesNotExist:
            return None

    def resolve_coin_by_buzz_change(self, info, **args):
        return Coin.objects.annotate(
            pctChange=(F('currentBuzzScore') - F('previousBuzzScore') / F('previousBuzzScore') * 100)).order_by('pctChange').reverse()

schema = graphene.Schema(query=Query)
