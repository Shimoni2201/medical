from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView, DetailView
from .models import *

class NewSupplier(LoginRequiredMixin,CreateView):
    model = suppliers
    fields = '__all__'

class ViewSupplier(LoginRequiredMixin,ListView):
    model = suppliers
    context_object_name = 'supply'

class UpdateSupplier(LoginRequiredMixin,UpdateView):
    model = suppliers
    fields = '__all__'

class DeleteSupplier(LoginRequiredMixin,DeleteView):
    model = suppliers
    success_url = '/supplier/view'

class Detail(LoginRequiredMixin,DetailView):
    model = suppliers
    success_url = '/supplier/view'