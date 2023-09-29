from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'customer'
