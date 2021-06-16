from django.db import models

from django import forms
import re

# Create your models here.



def ValidarLongitudPassword(cadena):
    if len(cadena) < 8:
        raise forms.ValidationError(
            f'Error: la contraseña al menos debe contener 8 caracteres'
        )



def validarEmail(cadena):
    #valida que el email tenga el formato correcto
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if not EMAIL_REGEX.match(cadena):          
        raise forms.ValidationError(
            f'Error de formato: {cadena} no es un e-mail valido'
        )
    #valida que el email no se repita
    
    for s in Administrator.objects.all():
            # se usa .lower() para ovbiar las mayúsculas en la comparación de palabras
            if cadena.lower() == s.email.lower(): 
                raise forms.ValidationError(
                f'Error: el email {cadena} ya existe en nuestros registros!'
                )




class Administrator(models.Model): #super usuario que crea o elimina User
    first_name1 = models.CharField(max_length=45, blank=False, null=False)
    first_name2 = models.CharField(max_length=45, blank=False, null=False)
    last_name1 = models.CharField(max_length=45, blank=False, null=False)
    last_name2 = models.CharField(max_length=45, blank=False, null=False)
    rut = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False, validators=[validarEmail])
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserType(models.Model):
    type_name = models.CharField(max_length=50, blank=False, null=False) #secretaria, abogado, o procuradora
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class User(models.Model):
    first_name1 = models.CharField(max_length=45, blank=False, null=False)
    first_name2 = models.CharField(max_length=45, blank=False, null=False)
    last_name1 = models.CharField(max_length=45, blank=False, null=False)
    last_name2 = models.CharField(max_length=45, blank=False, null=False)
    rut = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False, validators=[validarEmail])
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    users_created_by = models.ForeignKey(Administrator, related_name="administrator_create", on_delete = models.CASCADE)
    user_manage_lawsuit = models.ManyToManyField(Lawsuit, related_name="lawsuit_managed_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Defendant(models.Model):
    first_name1 = models.CharField(max_length=45, blank=False, null=False)
    first_name2 = models.CharField(max_length=45, blank=False, null=False)
    last_name1 = models.CharField(max_length=45, blank=False, null=False)
    last_name2 = models.CharField(max_length=45, blank=False, null=False)
    address = models.CharField(max_length=45, blank=False, null=False)
    rut = models.CharField(max_length=10, blank=False, null=False)
    email = models.CharField(max_length=45, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    defendant_created_by = models.ForeignKey(Administrator, related_name="user_create_defendant", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


