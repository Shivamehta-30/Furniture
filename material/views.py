from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import material
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class NewMaterial(LoginRequiredMixin,CreateView):
    model = material
    fields = '__all__'

class ViewMaterial(LoginRequiredMixin,ListView):
    model = material
    context_object_name = 'material'

class UpdateMaterial(LoginRequiredMixin,UpdateView):
    model = material
    fields = '__all__'

class DeleteMaterial(LoginRequiredMixin,DeleteView):
    model = material
    success_url = '/material/view'