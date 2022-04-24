from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from product.models import product
from customer.models import customer
from supplier.models import suppliers
from outward_purchase.models import outward_purchase
from inward_purchase.models import inward_purchase
from loss.models import loss
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,"users/home.html")

def dashboard(request):

    no_of_products=product.objects.count()
    no_of_customer=customer.objects.count()
    no_of_supplier=suppliers.objects.count()
    from django.db.models import Sum
    total_outward=outward_purchase.objects.aggregate(Sum('net_amount'))
    total_outward=total_outward['net_amount__sum']
    total_outward_pending = outward_purchase.objects.aggregate(Sum('due_amount'))
    total_outward_pending = total_outward_pending['due_amount__sum']

    total_inward = inward_purchase.objects.aggregate(Sum('net_amount'))
    total_inward = total_inward['net_amount__sum']
    total_inward_pending = inward_purchase.objects.aggregate(Sum('due_amount'))
    total_inward_pending = total_inward_pending['due_amount__sum']

    losses = loss.objects.aggregate(Sum('price'))
    losses = losses['price__sum']

    return render(request,"users/dashboard.html",{
        "no_of_products":no_of_products,
        "no_of_customer":no_of_customer,
        "no_of_supplier" : no_of_supplier,
        "total_outward":total_outward,
        "total_outward_pending":total_outward_pending,
        "total_inward" : total_inward,
        "total_inward_pending" :total_inward_pending,
        "losses" : losses
    })

def get_total_sales_by_month(request):
    from datetime import datetime
    result = outward_purchase.objects.annotate(month=TruncMonth('date')).values('month').annotate( no_of_ad=Sum('net_amount'))
    rel = inward_purchase.objects.annotate(month=TruncMonth('date')).values('month').annotate(no_of_dd=Sum('net_amount'))
    data1 = {'label': [], 'values': []}
    data2 = {'label': [], 'values': []}

    # dat = {'label' : [], 'val':[]}
    for ex in result:
        data1['label'].append(datetime.strftime(ex['month'], '%B'))
        data1['values'].append(ex['no_of_ad'])
        # print(datetime.strftime(ex['month'], '%B'),ex['no_of_ad'] )
        # print(data)

    for e in rel:
        data2['label'].append(datetime.strftime(e['month'], '%B'))
        data2['values'].append(e['no_of_dd'])


    dataset={"data1":data1,"data2":data2}
    return  JsonResponse(dataset)



def loss_by_month(request):

    from datetime import datetime
    rel = loss.objects.annotate(month=TruncMonth('date')).values('month').annotate( no_of_loss=Sum('price'))
    dat = {'label': [], 'values': []}
    for val in rel:
        dat['label'].append(datetime.strftime(val['month'], '%B'))
        dat['values'].append(val['no_of_loss'])
    return JsonResponse(dat)


