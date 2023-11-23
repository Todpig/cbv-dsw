from django.contrib import admin
from .models import Cliente, Quarto, Hospedagem, Consumo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'endereco')

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('apartamento', 'valor')

@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'quarto', 'data_entrada', 'data_saida', 'valor')

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'valor', 'Hospedagem')
