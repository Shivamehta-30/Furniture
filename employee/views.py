from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import emp
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class NewEmployee(LoginRequiredMixin,CreateView):
    model = emp
    fields = '__all__'

class ViewEmployee(LoginRequiredMixin,ListView):
    model = emp
    context_object_name = 'emps'

class UpdateEmployee(LoginRequiredMixin,UpdateView):
    model = emp
    fields = '__all__'

class DeleteEmployee(LoginRequiredMixin,DeleteView):
    model = emp
    success_url = '/Employee/view'