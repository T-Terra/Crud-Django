from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)