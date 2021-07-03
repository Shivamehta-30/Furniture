from django.db import models
from django.urls import reverse
from product.models import product
# Create your models here.

class prodcutin(models.Model):
    productname=models.ForeignKey(product,on_delete=models.CASCADE,related_name='product')
    rate=models.FloatField(max_length=100)
    qun=models.CharField(max_length=1000)
    price=models.FloatField(max_length=1000)
    GSTno=models.CharField(max_length=100,null=True,blank=True)
    discount=models.FloatField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.productname}"

    def get_absolute_url(self):
        return reverse("prodinward-view")

