from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.http import HttpResponseRedirect

# Create your views here.
class NewCustomerPayment(CreateView):
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
class ViewCustomerPayment(ListView):
    model = customerpay
    context_object_name = 'customerpay'

class UpdateCustomerPayment(UpdateView):
    model = customerpay
    fields = '__all__'

class DeleteCustomerPayment(DeleteView):
    model = customerpay
    success_url = '/Customerpayment/view'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.bill.due_amount = self.object.bill.due_amount + self.object.cash
        self.object.bill.save()
        return super(DeleteCustomerPayment, self).delete(request, *args, **kwargs)