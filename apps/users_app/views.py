from django.shortcuts import render, redirect
from apps.users_app.forms.register import AdministratorForm
from apps.secr_app.forms.new_lawsuit import DefendantForm, LawsuitForm


def index(request):


    
    return render(request, 'landing.html')



def make_administrator(request):

    context = {

        'administratorform' : AdministratorForm(),
        'new_lawsuit' : DefendantForm(),
        'LawsuitForm' : LawsuitForm(),

    }
    



    return render(request, 'make_administrator.html', context)


def login_administrator(request):
    return render(request, 'login_administrator.html')