from django.db import models
from django.urls import reverse
from customer.models import customer
from datetime import datetime
from outward_purchase.models import outward_purchase
# Create your models here.
class customerpay(models.Model):
    choice = (
        ('cash','cash'), ('netbank','netbank'), ('upi','upi'), ('cheque', 'cheque')
    )
    type = models.CharField(max_length=80, choices=choice,default='')
    bank_name = models.CharField(max_length=80, null=True, blank=True,default='')
    bank_branch = models.CharField(max_length=400, null=True, blank=True,default='')
    account_no = models.CharField(max_length=80, null=True, blank=True,default='')
    ifsc_code = models.CharField(max_length=80, null=True, blank=True,default='')
    phone = models.CharField(max_length=15, null=True, blank=True,default='')
    upi = models.CharField(max_length=80, null=True, blank=True,default='')
    cash = models.IntegerField(default=0, null=True, blank=True)
    check_no = models.CharField(max_length=30, default='', null=True, blank=True)
    check_date = models.CharField(max_length=35, default='', null=True, blank=True)
    cus = models.ForeignKey(customer, on_delete=models.CASCADE, related_name="customer")
    date = models.DateField(default=datetime.utcnow())
    bill = models.ForeignKey(outward_purchase, on_delete=models.CASCADE, related_name='bills', default='')


    def __str__(self):
        return f"{self.cash}"

    def get_absolute_url(self):
        return reverse("Customerpayment-view")