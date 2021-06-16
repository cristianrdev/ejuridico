from django.forms import ModelForm
from apps.admin_app.models import Administrator, User



class AdministratorForm(ModelForm):

    class Meta:
        model = Administrator 
        fields = ['first_name1','first_name2','last_name1','last_name2','rut','email', 'password']
        # widgets = {
        #     'short_bio': forms.Textarea(attrs = {"class":"form-control ", "rows":4, "cols": "50%" , "style":"resize: none;"}),

        # }
        labels = {
                'first_name1': 'Breve descripción profesional:',
                'first_name2': 'Breve descripción profesional:',
                'last_name1': 'Breve descripción profesional:',
                'last_name2': 'Breve descripción profesional:',
                'rut': 'Breve descripción profesional:',
                'email': 'Breve descripción profesional:',
                'password': 'Breve descripción profesional:',
        }



class User(ModelForm):

    class Meta:
        model = User 
        fields = ['first_name1','first_name2','last_name1','last_name2','rut','type','email', 'password']
        # widgets = {
        #     'short_bio': forms.Textarea(attrs = {"class":"form-control ", "rows":4, "cols": "50%" , "style":"resize: none;"}),

        # }
        labels = {
                'first_name1': 'Breve descripción profesional:',
                'first_name2': 'Breve descripción profesional:',
                'last_name1': 'Breve descripción profesional:',
                'last_name2': 'Breve descripción profesional:',
                'rut': 'Breve descripción profesional:',
                'email': 'Breve descripción profesional:',
                'password': 'Breve descripción profesional:',
        }
