from django.db import models
from django import forms
from apps.users_app.models import User, Administrator
import re
import datetime

# Create your models here.


class Lawsuit_State(models.Model):
    name_state = models.CharField(max_length=45)
    demand_state = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Defendant(models.Model): 
    first_name1 = models.CharField(max_length=45, blank=False, null=False) #este campo
    first_name2 = models.CharField(max_length=45, blank=False, null=False) #este campo
    last_name1 = models.CharField(max_length=45, blank=False, null=False) #este campo
    last_name2 = models.CharField(max_length=45, blank=False, null=False) #este campo
    address = models.CharField(max_length=255, blank=False, null=False) #este campo
    rut = models.CharField(max_length=10, blank=False, null=False) #este campo

    # email = models.CharField(max_length=45, blank=False, null=False)
    # password = models.CharField(max_length=100, blank=False, null=False)
    defendant_created_by = models.ForeignKey(Administrator, related_name="user_create_defendant", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# def Validar_Num_Pagare(pagare):

def Validar_Fecha_Mora(fecha_final):
    DATE_REGEX = re.compile(r'^([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')
    if not EMAIL_REGEX.match(fecha_final):
        raise forms.ValidationError(
            f'Error de formato: {fecha_final} debe tener el siguiente formato dd-mm-aaaa'
        )
    if fecha_final >= datetime.datetime.now():
        raise forms.ValidationError(
            f'Error fecha: {fecha_final} no puede estar en el futuro'
        )

def Validar_Monto_a_Pagar(monto_a_pagar):
    MONTO_REGEX = re.compile(r"[+-]?\d+(?:\.\d+)?")
    if on MONTO_REGEX.match(monto_a_pagar):
        raise forms.ValidationError(
            f'Error de formato: {monto_a_pagar} debser un numero valido'
        )        

def Validar_Fecha_Suscripcion(fecha_suscripcion)
DATE_REGEX = re.compile(r'^([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')
    if not EMAIL_REGEX.match(fecha_suscripcion):
        raise forms.ValidationError(
            f'Error de formato: {fecha_suscripcion} debe tener el siguiente formato dd-mm-aaaa'
        )
    if fecha_suscripcion >= datetime.datetime.now():
        raise forms.ValidationError(
            f'Error fecha: {fecha_suscripcion} no puede estar en el futuro'
        )

def Validar_Monto_Demandado(monto_demandado):
    MONTO_REGEX = re.compile(r"[+-]?\d+(?:\.\d+)?")
    if on MONTO_REGEX.match(monto_demandado):
        raise forms.ValidationError(
            f'Error de formato: {monto_demandado} debser un numero valido'
        )  

class Lawsuit(models.Model):
    num_promissory_notes = models.CharField(max_length=45,blank=False, null=False,validators=[Validar_Num_Pagare])   #este campo
    final_date = models.DateField(validators=[Validar_Fecha_Mora])  #este campo
    mount_to_pay = models.IntegerField(validators=[Validar_Monto_a_Pagar]) #este campo
    num_operation = models.CharField(max_length=255, validators=[Validar_Num_Operacion]) #este campo
    suscription_date= models.DateField(validators=[Validar_Fecha_Suscripcion]) #este campo
    demand_amount= models.IntegerField(validators=[Validar_Monto_Demandado]) #este campo
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
