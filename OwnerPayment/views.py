from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class NewPayment(CreateView):
    model = payment
    fields = '__all__'

class ViewPayment(ListView):
    model = payment
    context_object_name = ' OwnerPayments'

class UpdatePayment(UpdateView):
    model = payment
    fields = '__all__'

class DeletePayment(DeleteView):
    model = payment
    success_url = '/payment/view'