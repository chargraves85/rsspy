from django.contrib import admin
from rsspy_backend.models import Coin


class CoinAdmin(admin.ModelAdmin):
    list_display = ('coinName', 'symbol', 'data', 'currentBuzzScore', 'previousBuzzScore')


# Register your models here.

admin.site.register(Coin, CoinAdmin)
