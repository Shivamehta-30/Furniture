from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class NewCustomerPayment(CreateView,LoginRequiredMixin):
    model = customerpay
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        self.object.bill.due_amount = self.object.bill.net_amount - self.object.cash
        if self.object.bill.due_amount < 0:
            self.object.bill.due_amount = self.object.bill.net_amount
            self.object.delete()
            return HttpResponseRedirect('/Customerpayment/new/')
        else:
            self.object.bill.save()
            return HttpResponseRedirect(self.get_success_url())
class ViewCustomerPayment(ListView,LoginRequiredMixin):
    model = customerpay
    context_object_name = 'customerpay'

class UpdateCustomerPayment(UpdateView,LoginRequiredMixin):
    model = customerpay
    fields = '__all__'

class DeleteCustomerPayment(DeleteView,LoginRequiredMixin):
    model = customerpay
    success_url = '/Customerpayment/view'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.bill.due_amount = self.object.bill.due_amount + self.object.cash
        self.object.bill.save()
        return super(DeleteCustomerPayment, self).delete(request, *args, **kwargs)