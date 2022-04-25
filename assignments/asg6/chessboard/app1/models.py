from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=2, primary_key=True)
    value = models.CharField(max_length=7)
    class Meta:
        unique_together = (("user", "name"))
