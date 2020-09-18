from django.db import models
from datetime import date,datetime

class Customers(models.Model):
    DateTransaction=models.DateField(auto_now_add=True,auto_now=True)
    Amount=models.IntegerField()
    OrderNo=models.IntegerField()
    CountomerID=models.IntegerField()
    UDDI=models.CharField(max_length=1000)
    Status=models.CharField(max_length=100)
    DateReceived=models.DateField(auto_now_add=True,auto_now=True)
    TrasactionCode=models.IntegerField()
    TrasactionText=models.CharField(max_length=1000)

