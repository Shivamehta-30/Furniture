from  django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Newproductin(LoginRequiredMixin,CreateView):
    model = prodcutin
    fields = ['productname', 'qun', 'rate', 'price', 'discount', 'GSTno']
    context_object_name = 'product'
class Viewproductin(LoginRequiredMixin,ListView):
    model = prodcutin
    context_object_name = 'prod'

class Updateproductin(LoginRequiredMixin,UpdateView):
    model = prodcutin
    fields = '__all__'

class Deleteproductin(LoginRequiredMixin,DeleteView):
    model = prodcutin
    success_url = '/inward_purchase/closed'