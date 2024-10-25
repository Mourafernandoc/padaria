from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
]
