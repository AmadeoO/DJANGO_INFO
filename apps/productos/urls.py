from django.urls import path,include
from . import views

app_name = 'productos'

urlpatterns = [
    path('Listar/', views.List, name="listar"),    
]
