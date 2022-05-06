from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import *
class NewEmployee(LoginRequiredMixin,CreateView):
    model = employee
    fields = '__all__'

class ViewEmployee(LoginRequiredMixin,ListView):
    model = employee
    context_object_name = 'employees'

class UpdateEmployee(LoginRequiredMixin,UpdateView):
    model = employee
    fields = '__all__'

class DeleteEmployee(LoginRequiredMixin,DeleteView):
    model = employee
    success_url = '/employee/view'

class Detail(LoginRequiredMixin,DetailView):
    model = employee
    success_url = '/employee/view'