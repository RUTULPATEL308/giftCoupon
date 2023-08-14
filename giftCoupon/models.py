from django.db import models
import uuid
from .static import *

# Create your models here.


class redeemTbl(models.Model):

    code_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField(null=False)
    Ccode = models.CharField(max_length=50, null=False, unique=True)
    upi_address = models.CharField(max_length=30, null=False)
    review = models.TextField(null=True)
    cus_crated_at = models.DateTimeField(auto_now_add=True)
    cus_updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class couponCodes(models.Model):
    Ccode = models.CharField(max_length=50)
    expire_date = models.DateField(blank=True)
    cus_crated_at = models.DateTimeField(auto_now_add=True)
    cus_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Ccode
    
