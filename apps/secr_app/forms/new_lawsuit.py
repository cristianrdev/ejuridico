from django.forms import ModelForm
from django import forms
from ..models import Lawsuit


class LawsuitForm(ModelForm):
    class Meta:
        model = Lawsuit
        fields = ['num_promissory_notes','final_date','mount_to_pay','num_operation','suscription_date','demand_amount']

        labels ={
            'num_promissory_notes':'Número Pagaré',
            'final_date': 'Fecha MORA',
            'mount_to_pay': 'Monto a Pagar',
            'num_operation':'Número de Operación',
            'suscription_date':'Fecha Suscripción',
            'demand_amount':'Monto Demandado',
        }