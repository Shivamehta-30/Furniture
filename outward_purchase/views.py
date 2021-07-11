from django.http import HttpResponseRedirect
from django.shortcuts import render
from productout.models import prodoutward
from django import forms
from .models import outward_purchase
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
# Create your views here.

class NewInwardBill(CreateView):
    model = outward_purchase
    fields = ['date','cus','total','net_amount','gst','discount','due_amount']
    success_url = '/outward_purchase/view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = prodoutward.objects.filter(is_billed=False).all()
        return context

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodoutward.objects.filter(is_billed=False).all():
            self.object.products.add(product)
            product.is_billed=True
            product.save()


        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class ViewPurchaseBill(ListView):
    model = outward_purchase
    context_object_name = "bills"

class UpdatePurchaseBill(UpdateView):
    model = outward_purchase
    fields = ['date', 'cus', 'total', 'net_amount', 'gst', 'discount', 'due_amount']
    success_url = '/outward_purchase/view'

class DeletePurchaseBill(DeleteView):
    model = outward_purchase
    success_url = '/outward_purchase/view'


class DetailPurchaseBill(DetailView):
    model = outward_purchase

def closewindow(request):
    return render(request,"outward_purchase/close_window.html")