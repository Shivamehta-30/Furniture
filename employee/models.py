from django.db import models
from django.urls import reverse
# Create your models here.
class emp(models.Model):
    choice = (
        ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
    )
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
    gender=models.CharField(max_length=10 ,choices=choice)
    emailid=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    DOJ=models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos', blank=True, default='default.jpg')
    documnets = models.FileField(upload_to='docs', default='')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def get_absolute_url(self):
        return reverse("Employee-view")
