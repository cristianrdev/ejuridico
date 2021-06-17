from apps.users_app.models import Administrator, User, UserType
from django.shortcuts import redirect, render
from apps.users_app.forms.register import UserForm

def secr_dashboard(request):
    if not 'id' in request.session or request.session['user_type'] != "administrator":
        return redirect('/')
    this_user= User.objects.get(id = int(request.session['id'])) 
    all_users = User.objects.all()


    context = {
        'this_user' : this_user,
    }
    return render(request, 'dashboard_secretary.html', context)


def create_lawsuit(request):
    lawsuitform = LawsuitForm(request.POST)
    if lawsuitform.is_valid():
         new_lawsuit =lawsuitform.save(commit=False)
         return redirect('/')
    
    context = {
        'lawsuitform' : lawsuitform,
    }
    return render(request, 'new_lawsuit.html',context)
