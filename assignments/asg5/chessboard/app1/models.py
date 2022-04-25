from django.db import models

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=2, primary_key=True)
    value = models.CharField(max_length=7)
