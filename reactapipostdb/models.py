from django.db import models

# Create your models here.
class infomodel(models.Model):
    fullname=models.CharField(max_length=50)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=12)
    healthplanchoice=models.CharField(max_length=20,null=True)
    insurer=models.CharField(max_length=20,null=True)
    healthplanname=models.CharField(max_length=30,null=True)
    yourname=models.CharField(max_length=40,null=True)
    memberid=models.CharField(max_length=20,null=True)
    subscriberid=models.CharField(max_length=20,null=True)
    groupid=models.CharField(max_length=20,null=True)
    planid=models.CharField(max_length=20,null=True)
    datacategories=models.CharField(max_length=20)
    optionalyourname=models.CharField(max_length=50)
    dateofsignature=models.CharField(max_length=10)
    signatureurl=models.CharField(max_length=200)
    datetimeofupdate=models.DateTimeField(auto_now=True)




