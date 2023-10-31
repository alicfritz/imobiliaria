from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_imoveis/', views.lista_imoveis, name='lista_imoveis'),
]