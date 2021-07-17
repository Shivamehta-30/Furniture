from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import supplier
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NewSupplier(LoginRequiredMixin,CreateView):
    model = supplier
    fields = '__all__'

class ViewSupplier(LoginRequiredMixin,ListView):
    model = supplier
    context_object_name = 'suppliers'

class UpdateSupplier(LoginRequiredMixin,UpdateView):
    model = supplier
    fields = '__all__'

class DeleteSupplier(LoginRequiredMixin,DeleteView):
    model = supplier
    success_url = '/supplier/view'