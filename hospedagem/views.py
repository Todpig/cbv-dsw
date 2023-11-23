from typing import Any
from django.shortcuts import render
from .models import Hospedagem
from django.urls import reverse_lazy
from .forms import HospedagemForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class HospedagemCriar(CreateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

class HospedagemEditar(UpdateView):
    model = Hospedagem
    template_name = 'form.html'
    form_class = HospedagemForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy("index")

class HospedagemListar(ListView):
    model = Hospedagem
    template_name = 'index.html'
    context_object_name = 'hospedagens'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hospedagens"] = Hospedagem.objects.all()
        return context

class HospedagemDeletar(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class HospedagemDetalhe(DetailView):
    model = Hospedagem
    template_name = 'detalhar.html'
    context_object_name = 'hospedagem'