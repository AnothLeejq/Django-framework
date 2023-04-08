from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Item(models.Model):
    id = models.AutoField(primary_key = True)
    status = models.CharField(max_length = 20)
    optimized_circuit = models.CharField(max_length = 300)
    circuits = models.CharField(max_length = 300)
    result = models.JSONField()