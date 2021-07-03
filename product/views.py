from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import product
# Create your views here.

class Newproduct(CreateView):
    model = product
    fields = '__all__'

class Viewproduct(ListView):
    model = product
    context_object_name = 'product'

class Updateproduct(UpdateView):
    model = product
    fields = '__all__'

class Deleteproduct(DeleteView):
    model = product
    success_url = '/product/view'