import datetime

from django.db import models


# Create your models here.
class Transactions(models.Model):
    transaction_amount = models.DecimalField(max_digits=5, decimal_places=2)
    trans_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return str(self.transaction_amount)
