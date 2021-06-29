from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import emp
# Create your views here.
class NewEmployee(CreateView):
    model = emp
    fields = '__all__'

class ViewEmployee(ListView):
    model = emp
    context_object_name = 'emps'

class UpdateEmployee(UpdateView):
    model = emp
    fields = '__all__'

class DeleteEmployee(DeleteView):
    model = emp
    success_url = '/Employee/view'