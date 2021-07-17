from django.shortcuts import render
from product.models import product
from customer.models import customer
from outward_purchase.models import outward_purchase
# Create your views here.
def home(request):
    return render(request,"users/home.html")

def dashboard(request):
    no_of_products=product.objects.count()
    no_of_customer=customer.objects.count()
    from django.db.models import Sum
    total_outward=outward_purchase.objects.aggregate(Sum('net_amount'))
    total_outward=total_outward['net_amount__sum']
    total_outward_pending = outward_purchase.objects.aggregate(Sum('due_amount'))
    total_outward_pending = total_outward_pending['due_amount__sum']

    return render(request,"users/dashboard.html",{
        "no_of_products":no_of_products,
        "no_of_customer":no_of_customer,
        "total_outward":total_outward,
        "total_outward_pending":total_outward_pending
    })