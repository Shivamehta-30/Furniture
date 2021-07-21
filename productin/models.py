from django.db import models
from django.urls import reverse
from product.models import product
# Create your models here.

class prodcutin(models.Model):
    productname=models.ForeignKey(product,on_delete=models.CASCADE,related_name='product')
    rate=models.FloatField(max_length=100)
    qun=models.IntegerField()
    price=models.FloatField(max_length=1000)
    GSTno=models.CharField(default=0,max_length=100,null=True,blank=True)
    cgst = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    discount=models.FloatField(default=0,max_length=100,null=True,blank=True)
    is_billed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.productname}"

    def get_absolute_url(self):
        return reverse("closed")