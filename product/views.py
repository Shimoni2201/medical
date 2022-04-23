from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView, DetailView
from .models import *
# Create your views here.
class Newproduct(LoginRequiredMixin,CreateView):
    model = product
    fields = '__all__'

class Viewproduct(LoginRequiredMixin,ListView):
    model = product
    context_object_name = 'products'

class Updateproduct(LoginRequiredMixin,UpdateView):
    model = product
    fields = '__all__'

class Deleteproduct(LoginRequiredMixin,DeleteView):
    model = product
    success_url = '/product/view'

class Detail(LoginRequiredMixin,DetailView):
    model = product
    success_url = '/product/view'