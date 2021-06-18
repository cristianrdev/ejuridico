from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
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




class Administrator(models.Model): #super usuario que crea o elimina User (hay que hacer formulario!!!!)
    first_name1 = models.CharField(max_length=45, blank=False, null=False)
    first_name2 = models.CharField(max_length=45, blank=False, null=False)
    last_name1 = models.CharField(max_length=45, blank=False, null=False)
    last_name2 = models.CharField(max_length=45, blank=False, null=False)
    rut = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False, validators=[validarEmail])
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Administrator, self).save(*args, **kwargs)

    @staticmethod
    def authenticate(email, password):
        admin = Administrator.objects.filter(email = email)
        print ('user', admin)
        #buscar si hay un email en la base de datos
        if len(admin) == 1:
            #si existe un email asociado
            #se existe un el usuario (se supone que debe ser uno solo por sus validaciones)
            admin = admin[0]
            bd_password = admin.password
            if check_password(password, bd_password): #convierte los hash y los comparas
                return admin

        return None 

class UserType(models.Model):
    type_name = models.CharField(max_length=50, blank=False, null=False) #secretaria, abogado, o procuradora
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.type_name

    # def get_form_kwargs(self):
    #    kwargs = super().get_form_kwargs()
    #    kwargs.update({'type_name': self.request})
    #    return kwargs

class User(models.Model):
    first_name1 = models.CharField(max_length=45, blank=False, null=False)
    first_name2 = models.CharField(max_length=45, blank=False, null=False)
    last_name1 = models.CharField(max_length=45, blank=False, null=False)
    last_name2 = models.CharField(max_length=45, blank=False, null=False)
    rut = models.CharField(max_length=20, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False, validators=[validarEmail])
    password = models.CharField(max_length=100, validators=[ValidarLongitudPassword])
    type = models.ForeignKey(UserType, related_name="user_type", on_delete = models.CASCADE)
    users_created_by = models.ForeignKey(Administrator, related_name="administrator_create", on_delete = models.CASCADE)
    # user_manage_lawsuit = models.ManyToManyField(Lawsuit, related_name="lawsuit_managed_by")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    @staticmethod
    def authenticate(email, password):
        user = User.objects.filter(email = email)
        print ('user', user)
        #buscar si hay un email en la base de datos
        if len(user) == 1:
            #si existe un email asociado
            #se existe un el usuario (se supone que debe ser uno solo por sus validaciones)
            user = user[0]
            bd_password = user.password
            if check_password(password, bd_password): #convierte los hash y los comparas
                return user
        
        
        return None 




















