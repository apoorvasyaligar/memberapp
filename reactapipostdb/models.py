from django.db import models
from django.utils import translation

# Create your models here.
class infomodel(models.Model):
    fullname=models.CharField(max_length=50,null=True)
    dob=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    address1=models.CharField(max_length=50,null=True)
    address2=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=20,null=True)
    phonenumber=models.CharField(max_length=12,null=True)
    healthplanchoice=models.CharField(max_length=20,null=True)
    insurer=models.CharField(max_length=20,null=True)
    healthplanname=models.CharField(max_length=30,null=True)
    yourname=models.CharField(max_length=40,null=True)
    memberid=models.CharField(max_length=20,null=True)
    subscriberid=models.CharField(max_length=20,null=True)
    groupid=models.CharField(max_length=20,null=True)
    planid=models.CharField(max_length=20,null=True)
    phonenumber=models.CharField(max_length=12,null=True)
    datacategories=models.CharField(max_length=20,null=True)
    optionalyourname=models.CharField(max_length=50,null=True)
    dateofsignature=models.CharField(max_length=10,null=True)
    signatureurl=models.CharField(max_length=200,null=True)
    datetimeofupdate=models.DateTimeField(auto_now=True)




