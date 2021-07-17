from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class NewPayment(LoginRequiredMixin,CreateView):
    model = suppayment
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        self.object.bill.due_amount = self.object.bill.net_amount - self.object.cash
        if self.object.bill.due_amount < 0:
            self.object.bill.due_amount = self.object.bill.net_amount
            self.object.delete()
            return HttpResponseRedirect('/supplierpay/new/')
        else:
            self.object.bill.save()
            return HttpResponseRedirect(self.get_success_url())

class ViewPayment(LoginRequiredMixin,ListView):
    model = suppayment
    context_object_name = 'supps'

class UpdatePayment(LoginRequiredMixin,UpdateView):
    model = suppayment
    fields = '__all__'

class DeletePayment(LoginRequiredMixin,DeleteView):
    model = suppayment
    success_url = '/supplierpay/view'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.bill.due_amount = self.object.bill.due_amount + self.object.cash
        self.object.bill.save()
        return super(DeletePayment, self).delete(request, *args, **kwargs)