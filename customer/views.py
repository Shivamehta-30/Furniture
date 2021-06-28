from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import customer
# Create your views here.
class NewSupplier(CreateView):
    model = customer
    fields = '__all__'

class ViewSupplier(ListView):
    model = customer
    context_object_name = 'customers'

class UpdateSupplier(UpdateView):
    model = customer
    fields = '__all__'

class DeleteSupplier(DeleteView):
    model = customer
    success_url = '/customer/view'