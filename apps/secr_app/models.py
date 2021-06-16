from django.db import models
from django import forms
from apps.users_app.models import User, Administrator
import re

# Create your models here.
def ValidarLongitud(cadena):
    if len(cadena) < 8:
        raise forms.ValidationError(
            f'Error: Debe contener mínimo 3 caracteres'
        )
def ValidarRut(cadena):
    pass

class Lawsuit_State(models.Model):
    name_state = models.CharField(max_length=45)
    demand_state = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Defendant(models.Model): 
    first_name1 = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitud]) #este campo
    first_name2 = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitud]) #este campo
    last_name1 = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitud]) #este campo
    last_name2 = models.CharField(max_length=45, blank=False, null=False, validators=[ValidarLongitud]) #este campo
    address = models.CharField(max_length=255, blank=False, null=False,validators=[ValidarLongitud]) #este campo
    rut = models.CharField(max_length=10, blank=False, null=False,validators=[ValidarRut]) #este campo

    # email = models.CharField(max_length=45, blank=False, null=False)
    # password = models.CharField(max_length=100, blank=False, null=False)
    defendant_created_by = models.ForeignKey(Administrator, related_name="user_create_defendant", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Lawsuit(models.Model):
    num_promissory_notes = models.CharField(max_length=45)   #este campo
    final_date = models.DateField()  #este campo
    mount_to_pay = models.IntegerField() #este campo
    num_operation = models.CharField(max_length=255) #este campo
    suscription_date= models.DateField() #este campo
    demand_amount= models.IntegerField() #este campo
    cause_rol = models.CharField(max_length=45) 
    
    current_defendant = models.ForeignKey(Defendant, related_name="lawsuits", on_delete = models.CASCADE)
    current_demand_state = models.ForeignKey(Lawsuit_State, related_name="lawsuits", on_delete = models.CASCADE)
    current_court = models.ForeignKey(Lawsuit_State, related_name="lawsuits", on_delete = models.CASCADE)
    lawsuit_administrated_by = models.ManyToManyField(User, related_name="user_administrate_lawsuit")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # lawsuit_managed_by



    class Court(models.Model):
        name_court = models.CharField(max_length=45)
        comuna = models.CharField(max_length=45)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
