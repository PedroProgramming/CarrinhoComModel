from django.urls import path
from . import views


urlpatterns = [
    path('add/<str:nome>', views.add, name="add"),
    path('ver_carrinho/', views.ver_carrinho, name="ver_carrinho"),
    path('excluir_produto/<int:id>', views.excluir_produto, name="excluir_produto"),
    path('limpar_tudo/', views.limpar_tudo, name="limpar_tudo"),
]