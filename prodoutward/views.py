from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from product.models import product
# Create your views here.
class Newproduct(LoginRequiredMixin,CreateView):
    model = prodoutward
    fields = ['prod', 'quantity', 'rate', 'price', 'discount', 'gst','sgst']
    context_object_name = 'product'



class Viewproduct(LoginRequiredMixin,ListView):
    model = prodoutward
    context_object_name = 'prod'

class Updateproduct(LoginRequiredMixin,UpdateView):
    model = prodoutward
    fields = ['prod', 'quantity', 'rate', 'price', 'discount', 'gst','sgst']

class Deleteproduct(LoginRequiredMixin,DeleteView):
    model = prodoutward
    success_url = '/outward_purchase/closed'