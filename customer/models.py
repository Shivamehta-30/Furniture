from django.db import models
from django.urls import reverse
# Create your models here.
class customer(models.Model):
    companyname=models.CharField(max_length=100,null=True,blank=True)
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
    DOB=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    GSTno=models.CharField(max_length=100,null=True,blank=True)
    emailid=models.CharField(max_length=100)
    contact_person_name=models.CharField(max_length=100)
    remark=models.TextField(null=True,blank=True)
    photo=models.ImageField(upload_to='photos',blank=True,default='default.jpg')
    documnets=models.FileField(upload_to='docs',default='')

    def __str__(self):
        return f"{self.companyname}"

    def get_absolute_url(self):
        return reverse("Customer-view")
