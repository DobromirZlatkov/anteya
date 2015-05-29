from django.db import models
from companies.models import Company


# Create your models here.
class Order(models.Model):
    company = models.ForeignKey(Company, related_name='orders')
    date = models.DateField()

    def __unicode__(self):
        return self.company.name + ' ' + self.date
