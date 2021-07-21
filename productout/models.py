from django.db import models
from django.urls import reverse
from product.models import product
# Create your models here.
class prodoutward(models.Model):
    productname = models.ForeignKey(product, on_delete=models.CASCADE, related_name="products")
    qun = models.CharField(max_length=100)
    rates = models.FloatField(max_length=100)
    prices = models.FloatField(max_length=100)
    discounts = models.FloatField(default=0,max_length=100, blank=True, null=True)
    GSTno = models.CharField(default=0,max_length=100, blank=True, null=True)
    cgst = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    is_billed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prices}"

    def get_absolute_url(self):
        return reverse("closed")