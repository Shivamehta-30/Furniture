from  django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class Newproductout(CreateView):
    model = prodoutward
    fields = '__all__'

class Viewproductout(ListView):
    model = prodoutward
    context_object_name = 'product'

class Updateproductout(UpdateView):
    model = prodoutward
    fields = '__all__'

class Deleteproductout(DeleteView):
    model = prodoutward
    success_url = '/productout/view'