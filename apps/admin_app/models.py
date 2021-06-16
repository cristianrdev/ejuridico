from django.db import models

# Create your models here.
class Administrador(models.Model):
    admin_fname1=models.Charfield(max_length=45, blank=False, null=False)
    admin_fname2=models.Charfield(max_length=45, blank=False, null=False)
    admin_lname1=models.Charfield(max_length=45, blank=False, null=False)
    admin_lname2=models.Charfield(max_length=45, blank=False, null=False)
    rut_admin = models.Charfield(max_length=45, blank=False, null=False)
    email_admin = models.Charfield(max_length=45, blank=False, null=False)
    admin_password = models.Charfield(max_length=45, blank=False, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)



class User(models.Model):
    user_fname1=models.Charfield(max_length=45, blank=False, null=False)
    user_fname2=models.Charfield(max_length=45, blank=False, null=False)
    user_lname1=models.Charfield(max_length=45, blank=False, null=False)
    user_lname2=models.Charfield(max_length=45, blank=False, null=False)
    user_admin = models.ForeignKey(Admin, related_name='users', on_delete=models.CASCADE)
    user_type = models.Charfield(max_length=45, blank=False, null=False)
