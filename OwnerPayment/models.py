from django.db import models
from django.urls import reverse
# Create your models here.
class OwnerPayment(models.Model):
    choice = (
        ('cash', 'cash'), ('netbank', 'netbank'), ('upi', 'upi'), ('cheque', 'cheque')
    )
    type=models.CharField(max_length=80 , choices=choice)
    bankname=models.CharField(max_length=80)
    branchname=models.CharField(max_length=80)
    acc=models.CharField(max_length=15)
    ifsc=models.CharField(max_length=10)
    phono=models.CharField(max_length=10)
    upi=models.CharField(max_length=20)
    balance=models.CharField(max_length=10)
    cheque_no = models.CharField(max_length=50, default='')
    cheque_date = models.CharField(max_length=50, default='')
    cash=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.balance}"

    def get_absolute_url(self):
        return reverse("payment-view")