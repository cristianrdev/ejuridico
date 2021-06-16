from django.db.models.base import Model
from django import forms
from django.forms import ModelForm
from apps.secr_app import Defendant

class DefendantForm(ModelForm):
    class Meta:
        model = Defendant
        fields = ['first_name1','first_name2','last_name1','last_name2','address','rut']
        #widgets = {
            #'first_name1': forms.Textarea(attrs = {"class":"form-control ", "rows":4, "cols": "50%" , "style":"resize: none;"})}

        labels = {
                'first_name1': 'Primer Nombre',
                'first_name2': 'Segundo Nombre',
                'last_name1': 'Primer Apellido',
                'last_name2': 'Segundo Apellido',
                'adress': 'Dirección Completa',
                'rut': 'RUT',
        }


        
