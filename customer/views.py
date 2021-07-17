from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import customer
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class NewCustomer(LoginRequiredMixin,CreateView):
    model = customer
    fields = '__all__'

class ViewCustomer(LoginRequiredMixin,ListView):
    model = customer
    context_object_name = 'customers'

class UpdateCustomer(LoginRequiredMixin,UpdateView):
    model = customer
    fields = '__all__'

class DeleteCustomer(LoginRequiredMixin,DeleteView):
    model = customer
    success_url = '/customer/view'

class DetailCustomer(LoginRequiredMixin,DetailView):
    model = customer
    success_url = '/customer/view'
