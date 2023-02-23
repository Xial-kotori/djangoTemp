from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, null=False)
    gender = models.BooleanField(null=False)
    age = models.IntegerField(null=False)
