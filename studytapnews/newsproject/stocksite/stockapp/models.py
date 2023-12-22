# stockapp/models.py

from django.db import models

class StockData(models.Model):
    symbol = models.CharField(max_length=10)
    date = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.symbol} - {self.date}"
