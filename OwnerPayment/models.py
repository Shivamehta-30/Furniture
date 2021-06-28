from django.db import models
from django.urls import reverse
# Create your models here.
class OwnerPayment(models.Model):
    type=models.CharField(max_length=80)
    bankname=models.CharField(max_length=80)
    branchname=models.CharField(max_length=80)
    acc=models.CharField(max_length=15)
    ifsc=models.CharField(max_length=10)
    phono=models.CharField(max_length=10)
    upi=models.CharField(max_length=20)
    balance=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.balance}"

    def get_absolute_url(self):
        return reverse("payment-view")