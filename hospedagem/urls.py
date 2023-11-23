from django.urls import path
from .views import *

urlpatterns = [
    path("", HospedagemListar.as_view(), name="index"),
    path("criar/", HospedagemCriar.as_view(), name="criar"),
    path("editar/<int:id>/", HospedagemEditar.as_view(), name="editar"),
    path("deletar/<int:id>/", HospedagemDeletar.as_view(), name="deletar"),
     path('hospedagem/<int:pk>/', HospedagemDetalhe.as_view(), name='detalhar'),
]