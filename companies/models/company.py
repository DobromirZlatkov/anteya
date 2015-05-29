from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='companies')
