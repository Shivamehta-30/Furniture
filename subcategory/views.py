from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Newsubcategory(LoginRequiredMixin,CreateView):
    model = subcategory
    fields = '__all__'

class Viewsubcategory(LoginRequiredMixin,ListView):
    model = subcategory
    context_object_name = 'subcategories'

class Updatesubcategory(LoginRequiredMixin,UpdateView):
    model = subcategory
    fields = '__all__'

class Deletesubcategory(LoginRequiredMixin,DeleteView):
    model = subcategory
    success_url='/subcategory/view'