from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class meriDukan(models.Model):
    name=models.CharField(max_length=100)
    varity=models.CharField(max_length=100)
    cost=models.IntegerField()
    city=models.CharField(max_length=100)
