from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class Newproduct(LoginRequiredMixin,CreateView):
    model = prodinward
    fields = ['prod', 'quantity', 'rate', 'price', 'discount', 'gst','sgst']
    context_object_name = 'product'


class Viewproduct(LoginRequiredMixin,ListView):
    model = prodinward
    context_object_name = 'prod'

class Updateproduct(LoginRequiredMixin,UpdateView):
    model = prodinward
    fields = ['prod', 'quantity', 'rate', 'price', 'discount', 'gst','sgst']

class Deleteproduct(LoginRequiredMixin,DeleteView):
    model = prodinward
    success_url = '/inward_purchase/closed'