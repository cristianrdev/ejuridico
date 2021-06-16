from django.db import models
from django import forms
from apps.users_app.models import User, Administrator
import re

# Create your models here.


class Lawsuit_State(models.Model):
    name_state = models.CharField(max_length=45)
    demand_state = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Defendant(models.Model): 
    first_name1 = models.CharField(max_length=45, blank=False, null=False)
    first_name2 = models.CharField(max_length=45, blank=False, null=False)
    last_name1 = models.CharField(max_length=45, blank=False, null=False)
    last_name2 = models.CharField(max_length=45, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    rut = models.CharField(max_length=10, blank=False, null=False)
    email = models.CharField(max_length=45, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    defendant_created_by = models.ForeignKey(Administrator, related_name="user_create_defendant", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Lawsuit(models.Model):
    num_promissory_notes = models.CharField(max_length=45)
    final_date = models.DateField()
    mount_to_pay = models.IntegerField()
    num_operation = models.CharField(max_length=255)
    suscription_date= models.DateField()
    demand_amount= models.IntegerField()
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
