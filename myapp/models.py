from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    foreign_key=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField(null=False,blank=False)
    phone=models.CharField(max_length=12,unique=False,null=False,blank=False)
    country=models.CharField(max_length=20,null=False,blank=False)
    state=models.CharField(max_length=20,null=False,blank=False)
    district=models.CharField(max_length=20,null=False,blank=False)
    
    place=models.CharField(max_length=20,null=False,blank=False)

    



class Catagory(models.Model):
    catagy_name=models.CharField(max_length=30,null=False,blank=False,unique=True)
    discription=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField()
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    

class Properties(models.Model):
    catagoryid=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    customerid=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    property_type=models.CharField(max_length=40,null=False,blank=False)
    property_image=models.FileField()
    property_country=models.CharField(max_length=40,null=False,blank=False)
    property_state=models.CharField(max_length=40,null=False,blank=False)
    property_district=models.CharField(max_length=40,null=False,blank=False)
    property_place=models.CharField(max_length=40,null=False,blank=False)
    property_country=models.CharField(max_length=40,null=False,blank=False)
    property_price=models.FloatField(max_length=40,null=False,blank=False)
    ploat_area=models.CharField(max_length=40,null=False,blank=False)
    phone=models.CharField(max_length=12)
    floar=models.IntegerField(null=True,blank=True)
    property_discription=models.CharField(max_length=300,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    comment=models.CharField(max_length=300,null=False,blank=False)
    key=models.ForeignKey(Properties,on_delete=models.CASCADE)