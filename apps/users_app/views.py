from django.shortcuts import render, render
from apps.users_app.forms.register import AdministratorForm


def index(request):

    context = {

        'administratorform' : AdministratorForm()
    }
    
    return render(request, 'landing.html', context)



def make_administrator(request):
    return render(request, 'make_administrator.html')