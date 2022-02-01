import datetime

from django.db import models


# TODO: Eventually we will change this to panel data with every row being unique to track changes over long periods
#  of time. First iteration has static timestamp fields for 3 days in 6 hour intervals.
class Coin(models.Model):
    coinName = models.CharField(primary_key=True, max_length=128)
    symbol = models.CharField(max_length=128)
    data = models.JSONField()
    currentBuzzScore = models.IntegerField(default=0)
    previousBuzzScore = models.IntegerField(default=0)

# {
#     coinName: example,
#     symbol: exp,
#     data: {
#         someTimeStamp: {\
#             buzzScore: 23,
#             articleCount: 5,
#             value: 20.20
#         },
#         someTimeStamp2: {
#             buzzScore: 23,
#             articleCount: 5,
#             value: 20.20
#         }
#     }
# }
