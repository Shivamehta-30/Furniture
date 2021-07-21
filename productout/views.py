from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Newproduct(LoginRequiredMixin,CreateView):
    model = prodoutward
    fields = ['productname', 'qun', 'rates', 'prices', 'discounts', 'GSTno','cgst']
    context_object_name = 'product'

class Viewproduct(LoginRequiredMixin,ListView):
    model = prodoutward
    context_object_name = 'prod'

class Updateproduct(LoginRequiredMixin,UpdateView):
    model = prodoutward
    fields = '__all__'

class Deleteproduct(LoginRequiredMixin,DeleteView):
    model = prodoutward
    success_url = '/outward_purchase/closed'