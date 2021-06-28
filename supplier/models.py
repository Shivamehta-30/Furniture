from django.db import models
from django.urls import reverse
# Create your models here.
class supplier(models.Model):
    companyname=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    middlename=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    house_no=models.CharField(max_length=100)
    streetname=models.CharField(max_length=100)
    areaname=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    phoneno=models.CharField(max_length=10)
    officeno=models.CharField(max_length=10)
    GSTno=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100)
    contact_person_name=models.CharField(max_length=100)
    remark=models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.companyname}"
    def get_absolute_url(self):
        return reverse("supplier-view")
