from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import category
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NewCategory(LoginRequiredMixin,CreateView):
    model = category
    fields = '__all__'

class ViewCategory(LoginRequiredMixin,ListView):
    model = category
    context_object_name = 'categories'

class UpdateCategory(LoginRequiredMixin,UpdateView):
    model = category
    fields = '__all__'

class DeleteCategory(LoginRequiredMixin,DeleteView):
    model = category
    success_url='/category/view'