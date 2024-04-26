from django.db import models

# Create your models here.


class Choose(models.Model):
    chooseID = models.AutoField(primary_key=True, unique=True)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
