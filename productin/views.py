from  django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class Newproductin(CreateView):
    model = prodcutin
    fields = '__all__'

class Viewproductin(ListView):
    model = prodcutin
    context_object_name = 'product'

class Updateproductin(UpdateView):
    model = prodcutin
    fields = '__all__'

class Deleteproductin(DeleteView):
    model = prodcutin
    success_url = '/productin/view'