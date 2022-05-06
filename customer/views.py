from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import *
class NewCustomer(LoginRequiredMixin,CreateView):
    model = customer
    fields = '__all__'

class ViewCustomer(LoginRequiredMixin,ListView):
    model = customer
    context_object_name = 'customer'

class UpdateCustomer(LoginRequiredMixin,UpdateView):
    model = customer
    fields = '__all__'

class DeleteCustomer(LoginRequiredMixin,DeleteView):
    model = customer
    success_url = '/customer/view'

class Detail(LoginRequiredMixin,DetailView):
    model = customer
    success_url = '/customer/view'

    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     context["pay"] = outward_purchase.objects.all()
    #     return context