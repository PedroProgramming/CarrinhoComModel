from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('criar_produto/', views.criar_produto, name="criar_produto"),
]