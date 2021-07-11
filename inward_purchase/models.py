from django.db import models
from datetime import datetime
from productin.models import prodcutin
from supplier.models import supplier
from django.urls import reverse

# Create your models here.

class inward_purchase(models.Model):
    date = models.DateField(default=datetime.utcnow)
    spp = models.ForeignKey(supplier, on_delete=models.CASCADE, related_name="suppliers",default='')
    products = models.ManyToManyField(prodcutin, related_name='inward_purchase_bill')
    total = models.IntegerField()
    gst = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=9, decimal_places=2)
    due_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def _str_(self):
        return f"{self.id} - {self.date}"

    def get_absolute_url(self):
        return reverse('view-purchase')