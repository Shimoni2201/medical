from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from prodoutward.models import prodoutward
from .models import outward_purchase
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
# Create your views here.

class NewInwardBill(LoginRequiredMixin,CreateView):
    model = outward_purchase
    fields = ['date','cus','total','net_amount','gst','sgst','discount','due_amount']
    success_url = '/outward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = prodoutward.objects.filter(is_billed=False).all()
        result = prodoutward.objects.filter(is_billed=False).aggregate(Sum('price'));
        context["to"] = result['price__sum'];
        return context

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodoutward.objects.filter(is_billed=False).all():
            self.object.products.add(product)
            product.prod.quantity = product.prod.quantity - product.quantity
            product.prod.save()
            product.is_billed=True
            product.save()


        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class ViewPurchaseBill(LoginRequiredMixin,ListView):
    model = outward_purchase
    context_object_name = "bills"

class UpdatePurchaseBill(LoginRequiredMixin,UpdateView):
    model = outward_purchase
    fields = ['date', 'cus', 'total','sgst', 'net_amount', 'gst', 'discount', 'due_amount']
    success_url = '/outward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = self.object.products.all() |  prodoutward.objects.filter(is_billed=False).all()
        result= prodoutward.objects.filter(is_billed=False).aggregate(Sum('price'));
        if result['price__sum'] == None:
            context["to"]=self.object.total
        else :
            context["to"]=self.object.total+result['price__sum'];
        return context

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodoutward.objects.filter(is_billed=False).all():
            self.object.products.add(product)
            product.prod.quantity = int(product.prod.quantity) - int(product.quantity)
            product.prod.save()
            product.is_billed = True
            product.save()

        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class DeletePurchaseBill(LoginRequiredMixin,DeleteView):
    model = outward_purchase
    success_url = '/outward_purchase/view'

    def delete(self, request, *args, **kwargs):
        print("inside  form valid before save")
        print("inside  form valid")
        self.object = self.get_object()
        for product in self.object.products.all():
            print(product.prod.name);
            product.prod.quantity = int(product.prod.quantity) + int(product.quantity)
            product.prod.save()
            product.save()
        return super(DeletePurchaseBill, self).delete(request, *args, **kwargs)

class DetailPurchaseBill(LoginRequiredMixin,DetailView):
    model = outward_purchase

def closewindow(request):
    return render(request,"outward_purchase/close_window.html")

def invoice(request,billid):
    object=outward_purchase.objects.get(id=billid)
    return render(request,"outward_purchase/print.html",{
        "object":object
    })