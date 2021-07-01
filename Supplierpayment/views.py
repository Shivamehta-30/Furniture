from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class NewPayment(CreateView):
    model = suppayment
    fields = '__all__'

class ViewPayment(ListView):
    model = suppayment
    context_object_name = 'supps'

class UpdatePayment(UpdateView):
    model = suppayment
    fields = '__all__'

class DeletePayment(DeleteView):
    model = suppayment
    success_url = '/supplierpay/view'