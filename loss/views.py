from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import loss
from django.views.generic import CreateView, ListView, DeleteView, UpdateView


# Create your views here.
class NewLoss(LoginRequiredMixin, CreateView):
    model = loss
    fields = '__all__'

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        self.object.product.quantity = self.object.product.quantity - self.object.quantity
        self.object.product.save()
        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class ViewLoss(LoginRequiredMixin, ListView):
    model = loss
    context_object_name = 'losses'


class UpdateLoss(LoginRequiredMixin, UpdateView):
    model = loss
    fields = '__all__'

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        self.object.product.quantity = self.object.product.quantity - self.object.quantity
        self.object.product.save()
        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class DeleteLoss(LoginRequiredMixin, DeleteView):
    model = loss
    success_url = '/loss/view'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.product.quantity = self.object.product.quantity + self.object.quantity
        self.object.product.save()
        return super(DeleteLoss, self).delete(request, *args, **kwargs)