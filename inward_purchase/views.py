from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from prodinward.models import prodinward
from .models import inward_purchase
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


# Create your views here.

class NewInwardBill(LoginRequiredMixin, CreateView):
    model = inward_purchase
    fields = ['date', 'sup', 'sgst', 'total', 'net_amount', 'gst', 'discount', 'due_amount']
    success_url = '/inward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = prodinward.objects.filter(is_billed=False).all()
        result = prodinward.objects.filter(is_billed=False).aggregate(Sum('price'));
        context["to"] = result['price__sum'];
        return context

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodinward.objects.filter(is_billed=False).all():
            self.object.products.add(product)
            product.prod.quantity = int(product.prod.quantity) + int(product.quantity)
            product.prod.save()
            product.is_billed = True
            product.save()

        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class ViewPurchaseBill(LoginRequiredMixin, ListView):
    model = inward_purchase
    context_object_name = "bills"


class UpdatePurchaseBill(LoginRequiredMixin, UpdateView):
    model = inward_purchase
    fields = ['date', 'sup', 'total', 'sgst', 'net_amount', 'gst', 'discount', 'due_amount']
    success_url = '/inward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = self.object.products.all() | prodinward.objects.filter(is_billed=False).all()
        result = prodinward.objects.filter(is_billed=False).aggregate(Sum('price'));
        if result['price__sum'] == None:
            context["to"] = self.object.total
        else:
            context["to"] = self.object.total + result['price__sum'];
        return context

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodinward.objects.filter(is_billed=False).all():
            self.object.products.add(product)
            product.prod.quantity = int(product.prod.quantity) + int(product.quantity)
            product.prod.save()
            product.is_billed = True
            product.save()

        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class DeletePurchaseBill(LoginRequiredMixin, DeleteView):
    model = inward_purchase
    success_url = '/inward_purchase/view'

    def delete(self, request, *args, **kwargs):
        print("inside  form valid before save")
        print("inside  form valid")
        self.object = self.get_object()
        for product in self.object.products.all():
            print(product.prod.name);
            product.prod.quantity = int(product.prod.quantity) - int(product.quantity)
            product.prod.save()
            product.save()
        return super(DeletePurchaseBill, self).delete(request, *args, **kwargs)


class DetailPurchaseBill(LoginRequiredMixin, DetailView):
    model = inward_purchase


def closewindow(request):
    return render(request, "inward_purchase/close_window.html")


def invoice(request, billid):
    object = inward_purchase.objects.get(id=billid)
    return render(request, "inward_purchase/invoice_print.html", {
        "object": object
    })


from django.shortcuts import render

# Create your views here.
