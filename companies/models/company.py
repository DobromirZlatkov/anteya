from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='companies')
    bulstat = models.CharField(max_length=13)
    mol = models.CharField(max_length=100)
    town = models.CharField(max_length=200, default='Sofia')
    address = models.CharField(max_length=200)
    recipient = models.CharField(max_length=200, blank=True, null=True, default=None)
    bank_name = models.CharField(max_length=200, blank=True, null=True, default=None)
    bank_iban = models.CharField(max_length=200, blank=True, null=True, default=None)
    bank_bic = models.CharField(max_length=200, blank=True, null=True, default=None)
