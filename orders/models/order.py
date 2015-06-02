from django.db import models
from companies.models import Company
from utils import datetime_utils
from decimal import Decimal


# Create your models here.
class Order(models.Model):
    company = models.ForeignKey(Company, related_name='orders')
    date = models.DateField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.company.company_name + ' ' + datetime_utils.string_from_date(self.date, '%d.%m.%Y')

    @property
    def total_amount(self):
        result = Decimal(0)
        for product in self.products.all():
            result += product.total_amount
        return result
