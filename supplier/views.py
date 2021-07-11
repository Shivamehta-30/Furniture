from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import supplier
# Create your views here.
class NewSupplier(CreateView):
    model = supplier
    fields = '__all__'

class ViewSupplier(ListView):
    model = supplier
    context_object_name = 'suppliers'

class UpdateSupplier(UpdateView):
    model = supplier
    fields = '__all__'

class DeleteSupplier(DeleteView):
    model = supplier
    success_url = '/supplier/view'