from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class NewCustomerPayment(CreateView):
    model = customerpay
    fields = '__all__'

class ViewCustomerPayment(ListView):
    model = customerpay
    context_object_name = 'customerpay'

class UpdateCustomerPayment(UpdateView):
    model = customerpay
    fields = '__all__'

class DeleteCustomerPayment(DeleteView):
    model = customerpay
    success_url = '/Customerpayment/view'