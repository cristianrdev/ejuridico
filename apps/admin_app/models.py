from django.db import models


class Defendant(models.Model):
    first_name1 = models.CharField(max_length=45)
    first_name2 = models.CharField(max_length=45)
    last_name1 = models.CharField(max_length=45)
    last_name2 = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    rut = models.CharField(max_length=10)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

