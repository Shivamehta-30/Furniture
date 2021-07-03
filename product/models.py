from django.db import models
from django.urls import reverse
from category.models import *
from subcategory.models import *
from material.models import *
# Create your models here.

class product(models.Model):
    name=models.CharField(max_length=100)
    serno=models.CharField(max_length=100)
    maincategory=models.ForeignKey(category,on_delete=models.CASCADE,related_name='category')
    size=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    qun=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    materials=models.ForeignKey(material,on_delete=models.CASCADE,related_name='material')
    subcategory=models.ForeignKey(subcategory,on_delete=models.CASCADE,related_name=subcategory)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product-view")