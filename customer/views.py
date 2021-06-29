from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import customer
# Create your views here.
class NewCustomer(CreateView):
    model = customer
    fields = '__all__'

class ViewCustomer(ListView):
    model = customer
    context_object_name = 'customers'

class UpdateCustomer(UpdateView):
    model = customer
    fields = '__all__'

class DeleteCustomer(DeleteView):
    model = customer
    success_url = '/customer/view'