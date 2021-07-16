from django.http import HttpResponseRedirect
from django.shortcuts import render
from productin.models import prodcutin
from django import forms
from .models import inward_purchase
from django.views.generic import CreateView,ListView,DetailView,DeleteView, UpdateView
# Create your views here.

class NewInwardBill(CreateView):
    model = inward_purchase
    fields = ['date','spp','total','net_amount','gst','discount','due_amount']
    success_url = '/inward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = prodcutin.objects.filter(is_billed=False).all()
        result = prodcutin.objects.filter(is_billed=False).aggregate(Sum('price'))
        context["total"] = result['price__sum']
        return context

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodcutin.objects.filter(is_billed=False).all():
            self.object.products.add(product)
            product.productname.qun = int(product.productname.qun) + int(product.qun)
            product.is_billed=True
            product.save()


        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class ViewPurchaseBill(ListView):
    model = inward_purchase
    context_object_name = "bills"

class UpdatePurchaseBill(UpdateView):
    model = inward_purchase
    fields = ['date', 'spp', 'total', 'net_amount', 'gst', 'discount', 'due_amount']
    success_url = '/inward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = self.object.products.all()
        result = prodcutin.objects.filter(is_billed=False).aggregate(Sum('price'))
        context["total"] = result['price__sum']

class DeletePurchaseBill(DeleteView):
    model = inward_purchase
    success_url = '/inward_purchase/view'


class DetailPurchaseBill(DetailView):
    model = inward_purchase

def closewindow(request):
    return render(request,"inward_purchase/close_window.html")