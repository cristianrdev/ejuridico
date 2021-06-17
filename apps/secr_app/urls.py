from django.urls import path
from . import views


urlpatterns = [
    path('', views.secr_dashboard),
    path('create_lawsuit',views.create_lawsuit),
]