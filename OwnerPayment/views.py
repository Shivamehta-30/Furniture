from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NewPayment(LoginRequiredMixin,CreateView):
    model = OwnerPayment
    fields = '__all__'

class ViewPayment(LoginRequiredMixin,ListView):
    model = OwnerPayment
    context_object_name = ' OwnerPayments'

class UpdatePayment(LoginRequiredMixin,UpdateView):
    model = OwnerPayment
    fields = '__all__'

class DeletePayment(LoginRequiredMixin,DeleteView):
    model = OwnerPayment
    success_url = '/payment/view'